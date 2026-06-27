"""
Lightweight Mathlib4 theorem verification bridge.

Grep the Mathlib4 source tree to verify that the Lean theorem names
claimed in concept YAML files actually exist. This is the first layer
of the Lean feedback loop — telling us whether a concept's Lean mapping
is real or hallucinated.

Full Lean compilation verification comes in Day 5-6.
"""

from __future__ import annotations

import logging
import os
import subprocess
from dataclasses import dataclass, field
from typing import List, Optional, Tuple, TYPE_CHECKING

if TYPE_CHECKING:
    from mathpkg.graph.cache import KnowledgeCache

logger = logging.getLogger(__name__)

# Default Mathlib4 source root
DEFAULT_MATHLIB_PATH = os.path.expanduser(
    "~/lean-demo/.lake/packages/mathlib/Mathlib/"
)


@dataclass
class LeanCheckResult:
    """Result of verifying a concept's Lean theorem against Mathlib4 source."""
    concept_id: str
    theorem_name: Optional[str]   # the claimed theorem name, or None
    found: bool
    file_path: Optional[str]      # relative path within Mathlib4 source
    line_number: Optional[int]
    match_type: str               # "exact" | "partial" | "none" | "not_declared"


# ── public API ────────────────────────────────────────────────────────────────

def verify_concept(concept_id: str,
                   cache: KnowledgeCache,
                   mathlib_path: Optional[str] = None) -> LeanCheckResult:
    """
    Verify that the Lean theorem referenced by *concept_id* exists in Mathlib4.

    Reads concept metadata from *cache*, greps for its ``lean_mathlib4_theorem``
    in the Mathlib4 source tree, and returns a LeanCheckResult.
    """
    info = cache.find_concept(concept_id)
    if info is None:
        return LeanCheckResult(
            concept_id=concept_id,
            theorem_name=None,
            found=False,
            file_path=None,
            line_number=None,
            match_type="none",
        )

    # Try known mapping first (Phase 0 hand-verified), then versions metadata
    theorem_name = KNOWN_LEAN_MAPPINGS.get(concept_id)
    if theorem_name is None:
        versions = cache.get_versions(concept_id)
        theorem_name = _extract_theorem_from_versions(versions)

    if theorem_name is None:
        return LeanCheckResult(
            concept_id=concept_id,
            theorem_name=None,
            found=False,
            file_path=None,
            line_number=None,
            match_type="not_declared",
        )

    ml_path = mathlib_path or DEFAULT_MATHLIB_PATH
    found, fpath, lineno = _grep_theorem(theorem_name, ml_path)

    match_type = "exact" if found else "none"
    return LeanCheckResult(
        concept_id=concept_id,
        theorem_name=theorem_name,
        found=found,
        file_path=fpath,
        line_number=lineno,
        match_type=match_type,
    )


def verify_all(cache: KnowledgeCache,
               mathlib_path: Optional[str] = None) -> List[LeanCheckResult]:
    """Verify ALL concepts in the cache. Returns a list of results."""
    ml_path = mathlib_path or DEFAULT_MATHLIB_PATH
    results: List[LeanCheckResult] = []
    for cid in sorted(cache.get_all_concepts()):
        try:
            result = verify_concept(cid, cache, ml_path)
            results.append(result)
        except Exception:
            logger.exception("Failed to verify %s", cid)
            results.append(LeanCheckResult(
                concept_id=cid,
                theorem_name=None,
                found=False,
                file_path=None,
                line_number=None,
                match_type="error",
            ))
    return results


# ── internal helpers ──────────────────────────────────────────────────────────

# Known Mathlib4 theorem/definition mappings for our 21 concepts
KNOWN_LEAN_MAPPINGS = {
    "set_and_function": "Set",
    "binary_operation": "Mul",
    "semigroup": "Semigroup",
    "monoid": "Monoid",
    "group": "Group",
    "abelian_group": "CommGroup",
    "subgroup": "Subgroup",
    "group_homomorphism": "MonoidHom",
    "kernel_of_homomorphism": "MonoidHom.ker",
    "image_of_homomorphism": "MonoidHom.range",
    "normal_subgroup": "Subgroup.Normal",
    "coset": "Subgroup",
    "quotient_group": "QuotientGroup",
    "group_isomorphism": "MulEquiv",
    "first_isomorphism_theorem": "QuotientGroup.quotientKerEquivRange",
    "symmetric_group": "Equiv.Perm",
    "cyclic_group": "IsCyclic",
    "group_action": "MulAction",
    "lagrange_theorem": "Subgroup.card_subgroup_dvd_card",
    "cayley_theorem": "Equiv.Perm.subgroupOfMulAction",
    "orbit_stabilizer_theorem": "MulAction.card_orbit_mul_card_stabilizer_eq_card_group",
}


def _extract_theorem_from_versions(versions: List[dict]) -> Optional[str]:
    """
    Extract the Mathlib4 theorem name for a concept.

    Uses a known mapping (Phase 0 hand-verified).
    Phase 1 will auto-populate this from concept extraction.
    """
    # Try version metadata first
    for v in versions:
        tn = v.get("theorem_number", "")
        if tn and "." in tn:
            return tn
    return None


def _grep_theorem(theorem_name: str,
                   mathlib_path: str) -> Tuple[bool, Optional[str], Optional[int]]:
    """
    Grep Mathlib4 source for *theorem_name*.

    Returns (found, relative_file_path, line_number).
    Uses subprocess with a 30-second timeout to avoid hanging on huge trees.

    The grep searches for patterns like:
        theorem card_subgroup_dvd_card
        def card_subgroup_dvd_card
        lemma card_subgroup_dvd_card
    in all .lean files under mathlib_path.
    """
    if not os.path.isdir(mathlib_path):
        logger.warning("Mathlib4 path not found: %s", mathlib_path)
        return False, None, None

    try:
        # Use ripgrep if available (much faster), fall back to grep
        proc = subprocess.run(
            [
                "rg", "--no-heading", "--line-number",
                "--max-filesize", "500K",
                rf"\b(theorem|def|lemma|instance)\s+{theorem_name}\b",
                mathlib_path,
            ],
            capture_output=True, text=True, timeout=30,
        )
    except FileNotFoundError:
        # ripgrep not available, use grep -r
        try:
            proc = subprocess.run(
                [
                    "grep", "-rn", "--include=*.lean",
                    "--max-count=1",
                    theorem_name,
                    mathlib_path,
                ],
                capture_output=True, text=True, timeout=30,
            )
        except subprocess.TimeoutExpired:
            logger.warning("grep timed out for %s", theorem_name)
            return False, None, None

    if proc.returncode != 0 or not proc.stdout.strip():
        return False, None, None

    # Parse first match: "path/to/file.lean:123:  theorem name ..."
    first_line = proc.stdout.strip().split("\n")[0]
    parts = first_line.split(":", 2)
    if len(parts) >= 2:
        rel_path = parts[0]
        try:
            lineno = int(parts[1])
        except ValueError:
            lineno = None
        # Make path relative to mathlib_path
        if rel_path.startswith(mathlib_path):
            rel_path = rel_path[len(mathlib_path):]
        return True, rel_path, lineno

    return True, None, None
