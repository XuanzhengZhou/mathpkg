"""
Layer 2: Lean 4 translation — convert expanded proofs to Lean code.

Takes an expanded, gap-free proof and translates it to Lean 4 code
using Mathlib4. The absence of mathematical gaps means compilation
errors are almost always API/type issues that the self-heal loop can fix.
"""

import json
import logging
from dataclasses import dataclass, field
from typing import List, Optional

from .deepseek_client import get_client, LLMResponse

logger = logging.getLogger(__name__)

LEAN_TRANSLATE_SYSTEM = """You are an expert Lean 4 programmer specializing in Mathlib4.

Translate the given expanded mathematical proof into Lean 4 code.

RULES:
1. Use Mathlib4 theorem names whenever possible — do NOT re-implement existing lemmas.
2. Use standard tactics: apply, rcases, intro, refine, simp, rw, exact, have, calc
3. Each step of the expanded proof should map to 1-3 lines of Lean.
4. Write clean, well-indented code.
5. If a theorem is already in Mathlib4, you may just reference it with `exact`.
6. Annotate with comments matching the proof step numbers.

The file already has `import Mathlib` and appropriate `open` statements.
You only need to write the `theorem` declaration with its proof.

FORMAT: Return a JSON object:
{
  "lean_code": "theorem name ... := by\\n  ...",
  "mathlib4_theorems_used": ["Subgroup.card_subgroup_dvd_card", ...],
  "tactics_used": ["rw", "simp", "exact", ...]
}"""


@dataclass
class LeanTranslateResult:
    concept_id: str
    lean_code: str
    mathlib4_theorems_used: List[str]
    tactics_used: List[str]
    tokens_in: int
    tokens_out: int
    cost_yuan: float


def translate_to_lean(concept_id: str,
                      statement_latex: str,
                      expanded_proof: str,
                      lean_context: str = "",
                      model: str = "deepseek-v4-pro") -> LeanTranslateResult:
    """
    Translate an expanded proof into Lean 4 code.

    Parameters
    ----------
    concept_id : str
        Unique concept identifier.
    statement_latex : str
        LaTeX statement of the theorem.
    expanded_proof : str
        Gap-free expanded proof from gap_fill.py.
    lean_context : str
        Additional context (e.g., "open Subgroup\\nopen Fintype").
    model : str
        DeepSeek model. Pro recommended.

    Returns
    -------
    LeanTranslateResult with Lean code.
    """
    client = get_client()

    user_prompt = f"""Theorem statement (LaTeX):
{statement_latex}

Expanded proof (numbered steps):
{expanded_proof}

{lean_context}

Write the Lean 4 theorem declaration with a complete proof."""

    messages = [
        {"role": "system", "content": LEAN_TRANSLATE_SYSTEM},
        {"role": "user", "content": user_prompt},
    ]

    schema = {
        "type": "object",
        "properties": {
            "lean_code": {"type": "string"},
            "mathlib4_theorems_used": {
                "type": "array",
                "items": {"type": "string"}
            },
            "tactics_used": {
                "type": "array",
                "items": {"type": "string"}
            }
        },
        "required": ["lean_code", "mathlib4_theorems_used"]
    }

    response = client.chat_with_schema(messages, schema, model=model, max_tokens=65536)

    content = response.content.strip()
    if content.startswith("```"):
        content = content.split("\n", 1)[1].rsplit("```", 1)[0]
    data = json.loads(content)

    return LeanTranslateResult(
        concept_id=concept_id,
        lean_code=data.get("lean_code", ""),
        mathlib4_theorems_used=data.get("mathlib4_theorems_used", []),
        tactics_used=data.get("tactics_used", []),
        tokens_in=response.tokens_in,
        tokens_out=response.tokens_out,
        cost_yuan=response.cost_yuan,
    )
