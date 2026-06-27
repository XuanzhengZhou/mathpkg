"""
Layer 1: Gap-filling — expand "obvious" proof steps into explicit steps.

Takes a textbook theorem statement + brief proof sketch (which may contain
gaps like "clearly", "it follows that", "one can show") and expands it
into a detailed, numbered proof where every step references a specific
axiom, definition, or known theorem.

This makes Layer 2 (Lean translation) much more reliable because the LLM
no longer needs to fill mathematical gaps — only translate explicit steps.
"""

import json
import logging
from dataclasses import dataclass, field
from typing import List, Optional

from .deepseek_client import get_client, LLMResponse

logger = logging.getLogger(__name__)

GAP_FILL_SYSTEM = """You are an expert mathematical proof writer. Your job is to expand
brief proof sketches into COMPLETE, NUMBERED proofs with NO gaps.

RULES:
1. NEVER use vague phrases: "clearly", "obviously", "it follows that",
   "one can show", "straightforward", "the result follows".
2. Every step must explicitly reference a specific axiom, definition,
   theorem, lemma, or logical operation.
3. Write at the level of a rigorous undergraduate textbook — a student
   must be able to follow every single line without additional reasoning.
4. Each numbered step should be ONE logical inference.
5. If the original proof says "by Theorem X", expand to show exactly
   HOW Theorem X applies (what substitution, what conditions are satisfied).
6. End with "∎".

FORMAT:
Return your response as a JSON object:
{
  "expanded_proof": "1. ...\\n2. ...\\n3. ...\\n∎",
  "steps_count": 15,
  "gaps_filled": ["Step 3: expanded 'it follows that' by citing Lemma 2.1", ...],
  "confidence": 0.85
}"""


@dataclass
class GapFillResult:
    concept_id: str
    statement: str
    original_sketch: str
    expanded_proof: str
    steps_count: int
    gaps_filled: List[str]
    confidence: float
    tokens_in: int
    tokens_out: int
    cost_yuan: float


def fill_gaps(concept_id: str,
              statement_latex: str,
              proof_sketch: str,
              model: str = "deepseek-v4-pro") -> GapFillResult:
    """
    Expand a proof sketch into an explicit, numbered proof.

    Parameters
    ----------
    concept_id : str
        Unique concept identifier.
    statement_latex : str
        LaTeX statement of the theorem.
    proof_sketch : str
        Brief proof sketch from the textbook (may contain gaps).
    model : str
        DeepSeek model to use. Pro recommended for quality.

    Returns
    -------
    GapFillResult with expanded proof.
    """
    client = get_client()

    user_prompt = f"""Theorem: {statement_latex}

Proof sketch from textbook:
{proof_sketch}

Expand this into a complete, numbered proof."""

    messages = [
        {"role": "system", "content": GAP_FILL_SYSTEM},
        {"role": "user", "content": user_prompt},
    ]

    schema = {
        "type": "object",
        "properties": {
            "expanded_proof": {"type": "string"},
            "steps_count": {"type": "integer"},
            "gaps_filled": {
                "type": "array",
                "items": {"type": "string"}
            },
            "confidence": {"type": "number"}
        },
        "required": ["expanded_proof", "steps_count", "gaps_filled", "confidence"]
    }

    response = client.chat_with_schema(messages, schema, model=model)

    # Parse JSON response
    content = response.content.strip()
    if content.startswith("```"):
        content = content.split("\n", 1)[1].rsplit("```", 1)[0]
    data = json.loads(content)

    return GapFillResult(
        concept_id=concept_id,
        statement=statement_latex,
        original_sketch=proof_sketch,
        expanded_proof=data.get("expanded_proof", ""),
        steps_count=data.get("steps_count", 0),
        gaps_filled=data.get("gaps_filled", []),
        confidence=data.get("confidence", 0.5),
        tokens_in=response.tokens_in,
        tokens_out=response.tokens_out,
        cost_yuan=response.cost_yuan,
    )
