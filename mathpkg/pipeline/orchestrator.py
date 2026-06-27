"""
Pipeline orchestrator — ties together all stages.

For a single concept:
  concept YAML → gap_fill → lean_translate → self_heal → result

For a book:
  PDF → Markdown → chapter split → concept extraction → ... → Lean verified

Can be invoked from Python or from Claude Code Workflow.
"""

import os
import logging
from dataclasses import dataclass, field
from typing import List, Optional, Dict, Any

from .gap_fill import fill_gaps, GapFillResult
from .lean_translate import translate_to_lean, LeanTranslateResult
from .self_heal import compile_and_heal, SelfHealResult

logger = logging.getLogger(__name__)


@dataclass
class PipelineResult:
    """Complete result for one concept through the full pipeline."""
    concept_id: str
    success: bool
    gap_fill: Optional[GapFillResult] = None
    lean_translate: Optional[LeanTranslateResult] = None
    self_heal: Optional[SelfHealResult] = None
    total_cost_yuan: float = 0.0
    error: Optional[str] = None


def process_concept(concept_data: Dict[str, Any],
                    skip_gap_fill: bool = False,
                    lean_context: str = "",
                    model: str = "deepseek-v4-pro") -> PipelineResult:
    """
    Run the full pipeline on a single concept.

    Parameters
    ----------
    concept_data : dict with keys:
        id, name_en, type, statement_latex, proof_sketch
    skip_gap_fill : bool
        If True, skip gap-filling (use proof_sketch directly).
        Set to True when the proof is already detailed enough.
    lean_context : str
        Extra context for Lean translation (imports, open statements).
    model : str
        DeepSeek model for Pro steps.

    Returns
    -------
    PipelineResult
    """
    concept_id = concept_data["id"]
    statement = concept_data.get("statement_latex", "")
    sketch = concept_data.get("proof_sketch", "")

    total_cost = 0.0

    # Layer 1: Gap-filling
    gap_result = None
    expanded_proof = sketch  # fallback
    if not skip_gap_fill and sketch:
        try:
            gap_result = fill_gaps(concept_id, statement, sketch, model=model)
            total_cost += gap_result.cost_yuan
            expanded_proof = gap_result.expanded_proof
            logger.info(f"[{concept_id}] Gap-fill: {gap_result.steps_count} steps, "
                        f"¥{gap_result.cost_yuan:.4f}")
        except Exception as e:
            logger.warning(f"[{concept_id}] Gap-fill failed: {e}")
            # Continue with original sketch
    elif not sketch:
        return PipelineResult(
            concept_id=concept_id,
            success=False,
            error="No proof sketch available",
        )

    # Layer 2: Lean translation
    lean_result = None
    try:
        lean_result = translate_to_lean(
            concept_id, statement, expanded_proof, lean_context, model=model
        )
        total_cost += lean_result.cost_yuan
        logger.info(f"[{concept_id}] Lean translate: "
                    f"{len(lean_result.lean_code)} chars, ¥{lean_result.cost_yuan:.4f}")
    except Exception as e:
        logger.error(f"[{concept_id}] Lean translate failed: {e}")
        return PipelineResult(
            concept_id=concept_id,
            success=False,
            gap_fill=gap_result,
            error=f"Lean translate: {e}",
            total_cost_yuan=total_cost,
        )

    # Layer 3+4: Compile + self-heal
    heal_result = None
    try:
        heal_result = compile_and_heal(
            concept_id, lean_result.lean_code, model=model
        )
        total_cost += heal_result.total_cost_yuan
        logger.info(f"[{concept_id}] Self-heal: {'✅' if heal_result.success else '❌'} "
                    f"({heal_result.rounds} rounds, ¥{heal_result.total_cost_yuan:.4f})")
    except Exception as e:
        logger.error(f"[{concept_id}] Self-heal failed: {e}")
        return PipelineResult(
            concept_id=concept_id,
            success=False,
            gap_fill=gap_result,
            lean_translate=lean_result,
            error=f"Self-heal: {e}",
            total_cost_yuan=total_cost,
        )

    return PipelineResult(
        concept_id=concept_id,
        success=heal_result.success if heal_result else False,
        gap_fill=gap_result,
        lean_translate=lean_result,
        self_heal=heal_result,
        total_cost_yuan=total_cost,
    )


def process_concepts_batch(concepts: List[Dict[str, Any]],
                           skip_gap_fill: bool = False,
                           model: str = "deepseek-v4-pro") -> List[PipelineResult]:
    """Process multiple concepts sequentially."""
    results = []
    total = len(concepts)
    for i, c in enumerate(concepts):
        logger.info(f"Processing {i+1}/{total}: {c.get('id', '?')}")
        result = process_concept(c, skip_gap_fill=skip_gap_fill, model=model)
        results.append(result)

        # Print progress
        status = "✅" if result.success else "❌"
        print(f"  [{i+1:3d}/{total}] {status} {result.concept_id:<35} "
              f"¥{result.total_cost_yuan:.4f} "
              f"({'gap:' + str(result.gap_fill.steps_count) + ' steps' if result.gap_fill else 'no-gap'})")

    # Summary
    succeeded = sum(1 for r in results if r.success)
    total_cost = sum(r.total_cost_yuan for r in results)
    print(f"\n{'='*60}")
    print(f"  Pipeline complete: {succeeded}/{total} succeeded")
    print(f"  Total API cost: ¥{total_cost:.4f}")
    print(f"{'='*60}")

    return results
