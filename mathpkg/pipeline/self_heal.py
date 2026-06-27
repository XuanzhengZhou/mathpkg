"""
Layer 3+4: Lean compilation + self-heal loop.

Writes Lean code into the MathPkg lake project and uses `lake build`
(which reuses cached Mathlib4 .olean files — 8560 jobs cached).

Self-heal loop: compile → parse errors → LLM fix → recompile (max 20 rounds).
"""

import os
import re
import subprocess
import logging
from dataclasses import dataclass, field
from typing import List, Optional, Tuple

from .deepseek_client import get_client

logger = logging.getLogger(__name__)

# Paths
LEAN_PROJECT_DIR = os.path.expanduser("~/文档/mathpkg/lean/MathPkg")
LEAN_BIN = os.path.expanduser("~/.elan/bin")
PIPELINE_FILE = os.path.join(LEAN_PROJECT_DIR, "MathPkg/Algebra/Group/Pipeline.lean")

SELF_HEAL_SYSTEM = """You are an expert Lean 4 debugger. Fix ALL compilation errors.

RULES:
1. Read each error CAREFULLY — it tells you the EXACT file, line, and column.

2. SPECIFIC FIX PATTERNS (apply these EXACTLY):
   - "failed to synthesize Fintype ↥H" → Add [Fintype H] to theorem arguments
   - "failed to synthesize Fintype G" → Add [Fintype G] or [Fintype α]
   - "Nat.card vs Fintype.card" → Add `simpa [Nat.card_eq_fintype_card] using`
   - "noncomputable" error → Add `noncomputable` before `def` or `theorem`
   - "type mismatch, expected ?m, got ?n" → Check if you confused Nat.card with Fintype.card
   - "Group (ZMod 7)" fails → Use (ZMod 7)ˣ (units) for multiplicative group

3. DO NOT change the theorem statement unless the error says it's ill-typed.
4. Keep the proof structure — fix only what's broken.
5. If the same error persists after 2 rounds, try a DIFFERENT approach.

Return ONLY the corrected Lean code."""


@dataclass
class SelfHealResult:
    concept_id: str
    success: bool
    rounds: int
    final_code: str
    errors: List[str]
    total_cost_yuan: float


def compile_and_heal(concept_id: str,
                     lean_code: str,
                     max_rounds: int = 20,
                     model: str = "deepseek-v4-pro") -> SelfHealResult:
    """
    Compile Lean code using lake build and iteratively fix errors.

    The code is written into the MathPkg lake project (Pipeline.lean),
    which reuses the 8560 cached .olean files from Mathlib4.
    """
    client = get_client()
    total_cost = 0.0
    all_errors: List[str] = []
    current_code = lean_code.strip()

    for round_num in range(1, max_rounds + 1):
        # Write to the pipeline file
        os.makedirs(os.path.dirname(PIPELINE_FILE), exist_ok=True)
        with open(PIPELINE_FILE, "w") as f:
            f.write(f"import Mathlib\n\n{current_code}")

        # Build using lake (reuses cached mathlib)
        success, errors = _lake_build()

        if success:
            logger.info(f"[{concept_id}] ✅ Compiled in round {round_num}")
            return SelfHealResult(
                concept_id=concept_id,
                success=True,
                rounds=round_num,
                final_code=current_code,
                errors=all_errors,
                total_cost_yuan=total_cost,
            )

        all_errors.extend(errors)
        unique_errors = _deduplicate_errors(errors)

        if round_num == max_rounds:
            logger.warning(f"[{concept_id}] ❌ Failed after {max_rounds} rounds")
            break

        # Build fix prompt for LLM
        error_text = "\n".join(unique_errors[:12])
        prompt = (
            f"Compilation FAILED. Fix these {len(unique_errors)} errors:\n\n"
            f"{error_text}\n\n"
            f"Current code:\n```lean\n{current_code}\n```\n\n"
            f"Return the COMPLETE corrected Lean code."
        )

        messages = [
            {"role": "system", "content": SELF_HEAL_SYSTEM},
            {"role": "user", "content": prompt},
        ]

        try:
            response = client.chat(messages, model=model, max_tokens=16384)
            total_cost += response.cost_yuan
        except Exception as e:
            logger.error(f"[{concept_id}] API error in round {round_num}: {e}")
            all_errors.append(f"API error: {e}")
            break

        # Extract code from response
        new_code = _extract_lean_code(response.content)
        if new_code:
            current_code = new_code
            logger.info(f"[{concept_id}] Round {round_num}: {len(unique_errors)} errors, "
                       f"¥{response.cost_yuan:.4f}")

    return SelfHealResult(
        concept_id=concept_id,
        success=False,
        rounds=max_rounds,
        final_code=current_code,
        errors=all_errors,
        total_cost_yuan=total_cost,
    )


def _lake_build() -> Tuple[bool, List[str]]:
    """Run lake build. Returns (success, error_messages)."""
    env = os.environ.copy()
    env["PATH"] = f"{LEAN_BIN}:{env.get('PATH', '')}"

    try:
        proc = subprocess.run(
            ["lake", "build"],
            capture_output=True, text=True,
            timeout=180,
            cwd=LEAN_PROJECT_DIR, env=env,
        )
    except subprocess.TimeoutExpired:
        return False, ["lake build timed out (>180s)"]

    stderr = proc.stderr
    stdout = proc.stdout

    if proc.returncode == 0:
        return True, []

    # Parse errors — only extract errors for our Pipeline file
    errors = []
    in_our_file = False
    for line in (stderr + "\n" + stdout).split("\n"):
        line = line.strip()
        if not line:
            continue

        # Track which file we're seeing errors for
        if "Pipeline.lean" in line:
            in_our_file = True
        elif ".lean:" in line and "Pipeline.lean" not in line:
            in_our_file = False
            # But if the error message continues, keep it
            if "error:" in line.lower():
                in_our_file = False

        if "error:" in line and "trace:" not in line:
            if "Pipeline.lean" in line or in_our_file:
                # Clean: remove the long trace prefix, keep error message
                clean = line.split("error:")[-1].strip()
                errors.append(f"Pipeline.lean error: {clean}"[:300])
            elif "MathPkg.Algebra.Group.Pipeline" in line:
                clean = line.split("error:")[-1].strip()
                errors.append(f"Pipeline.lean error: {clean}"[:300])

    # If no Pipeline-specific errors found, show all errors (might be import errors)
    if not errors:
        for line in (stderr + "\n" + stdout).split("\n"):
            if "error:" in line:
                errors.append(line[:400])
        errors = errors[:15]

    return False, errors


def _extract_lean_code(text: str) -> Optional[str]:
    """Extract Lean code from LLM response text."""
    text = text.strip()

    # Try ```lean ... ``` blocks first
    if "```lean" in text:
        parts = text.split("```lean", 1)
        if len(parts) > 1:
            code = parts[1].split("```", 1)[0]
            return code.strip()
    if "```" in text:
        parts = text.split("```")
        for i in range(1, len(parts), 2):
            code = parts[i].strip()
            if code.startswith("lean\n") or code.startswith("lean"):
                code = code[4:].strip()
            if "import" in code or "theorem" in code or "def" in code:
                return code

    # If no code blocks, return the whole thing
    if "import Mathlib" in text:
        return text

    return None


def _deduplicate_errors(errors: List[str]) -> List[str]:
    """Remove duplicate error messages."""
    seen = set()
    result = []
    for e in errors:
        # Normalize for dedup: extract the core error message
        core = re.sub(r'\d+', 'N', e.split(":")[-1].strip() if ":" in e else e)
        if core not in seen:
            seen.add(core)
            result.append(e)
    return result[:15]
