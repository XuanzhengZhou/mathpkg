"""
Data model for a mathematical concept.

Uses only Python dataclasses (stdlib) — no pydantic.
"""

from __future__ import annotations

import yaml
from dataclasses import dataclass, field, fields
from typing import Optional, List, Dict, Any


# ── sub-dataclasses ────────────────────────────────────────────────────────

@dataclass
class ConceptVersion:
    """One version/reference of a concept in a specific source/textbook."""
    source: str = ""
    author: str = ""
    chapter: str = ""
    section: str = ""
    pages: str = ""
    theorem_number: str = ""
    statement_latex: str = ""


@dataclass
class Statement:
    """A formal statement (theorem/proof sketch) attached to a concept."""
    type: str = "theorem"       # theorem | lemma | corollary | proposition | definition
    name: str = ""
    latex: str = ""
    proof_sketch: str = ""


@dataclass
class Exercise:
    """An exercise that bridges concepts together."""
    type: str = "bridge"        # bridge | introduction
    source: str = ""
    number: str = ""
    description: str = ""
    connects: List[str] = field(default_factory=list)


# ── valid enum values ──────────────────────────────────────────────────────

VALID_CONCEPT_TYPES = frozenset({
    "theory", "definition", "theorem", "lemma", "corollary",
    "exercise_bridge", "exercise_introduction",
})

VALID_LEAN_STATUS = frozenset({"none", "partial", "complete"})


# ── main dataclass ─────────────────────────────────────────────────────────

@dataclass
class Concept:
    """A mathematical concept with dependencies, versions, and Lean status."""
    id: str = ""
    name_en: str = ""
    name_zh: str = ""
    type: str = "theory"
    depends_required: List[str] = field(default_factory=list)
    depends_recommended: List[str] = field(default_factory=list)
    depends_suggested: List[str] = field(default_factory=list)
    versions: List[ConceptVersion] = field(default_factory=list)
    statements: List[Statement] = field(default_factory=list)
    lean_mathlib4_path: Optional[str] = None
    lean_mathlib4_theorem: Optional[str] = None
    lean_status: str = "none"
    exercises: List[Exercise] = field(default_factory=list)
    confidence: float = 0.5

    # ── validation helper ──────────────────────────────────────────────

    def _normalize(self):
        """Called after construction to clamp / set defaults."""
        if self.type not in VALID_CONCEPT_TYPES:
            self.type = "theory"
        if self.lean_status not in VALID_LEAN_STATUS:
            self.lean_status = "none"
        self.confidence = max(0.0, min(1.0, float(self.confidence)))

    # ── YAML loading ───────────────────────────────────────────────────

    @classmethod
    def from_yaml(cls, filepath: str) -> "Concept":
        """
        Load a Concept from a YAML file.

        Handles all fields, providing sensible defaults for missing optional
        fields so that every .yaml is parseable regardless of completeness.
        """
        with open(filepath, "r", encoding="utf-8") as fh:
            raw: Dict[str, Any] = yaml.safe_load(fh) or {}

        # --- id / name ---
        cid = raw.get("id", "")
        name = raw.get("name") or {}
        name_en = name.get("en", "") if isinstance(name, dict) else str(name)
        name_zh = name.get("zh", "") if isinstance(name, dict) else ""

        # --- type (with default) ---
        ctype = raw.get("type", "theory")
        if ctype not in VALID_CONCEPT_TYPES:
            ctype = "theory"

        # --- depends ---
        dep = raw.get("depends") or {}
        dep_required = _as_str_list(dep.get("required", []))
        dep_recommended = _as_str_list(dep.get("recommended", []))
        dep_suggested = _as_str_list(dep.get("suggested", []))

        # --- versions ---
        versions: List[ConceptVersion] = []
        for v in raw.get("versions") or []:
            versions.append(ConceptVersion(
                source=v.get("source", ""),
                author=v.get("author", ""),
                chapter=str(v.get("chapter", "")),
                section=str(v.get("section", "")),
                pages=str(v.get("pages", "")),
                theorem_number=str(v.get("theorem_number", "")),
                statement_latex=v.get("statement_latex", ""),
            ))

        # --- statements ---
        statements: List[Statement] = []
        for s in raw.get("statements") or []:
            statements.append(Statement(
                type=s.get("type", "theorem"),
                name=s.get("name", ""),
                latex=s.get("latex", ""),
                proof_sketch=s.get("proof_sketch", ""),
            ))

        # --- lean ---
        lean = raw.get("lean") or {}
        lean_path: Optional[str] = lean.get("mathlib4_path", None)
        lean_theorem: Optional[str] = lean.get("mathlib4_theorem", None)
        lean_status = lean.get("status", "none")
        if lean_status not in VALID_LEAN_STATUS:
            lean_status = "none"

        # --- exercises ---
        exercises: List[Exercise] = []
        for e in raw.get("exercises") or []:
            exercises.append(Exercise(
                type=e.get("type", "bridge"),
                source=e.get("source", ""),
                number=str(e.get("number", "")),
                description=e.get("description", ""),
                connects=_as_str_list(e.get("connects", [])),
            ))

        # --- confidence ---
        confidence = float(raw.get("confidence", 0.5))

        obj = cls(
            id=cid,
            name_en=name_en,
            name_zh=name_zh,
            type=ctype,
            depends_required=dep_required,
            depends_recommended=dep_recommended,
            depends_suggested=dep_suggested,
            versions=versions,
            statements=statements,
            lean_mathlib4_path=lean_path,
            lean_mathlib4_theorem=lean_theorem,
            lean_status=lean_status,
            exercises=exercises,
            confidence=confidence,
        )
        obj._normalize()
        return obj

    # ── convenience ────────────────────────────────────────────────────

    def to_dict(self) -> Dict[str, Any]:
        """Serialize the concept back to a dictionary (for SQLite / debugging)."""
        return {
            "id": self.id,
            "name_en": self.name_en,
            "name_zh": self.name_zh,
            "type": self.type,
            "depends_required": self.depends_required,
            "depends_recommended": self.depends_recommended,
            "depends_suggested": self.depends_suggested,
            "versions": [
                {
                    "source": v.source,
                    "author": v.author,
                    "chapter": v.chapter,
                    "section": v.section,
                    "pages": v.pages,
                    "theorem_number": v.theorem_number,
                }
                for v in self.versions
            ],
            "statements": [
                {"type": s.type, "name": s.name, "latex": s.latex, "proof_sketch": s.proof_sketch}
                for s in self.statements
            ],
            "lean_mathlib4_path": self.lean_mathlib4_path,
            "lean_mathlib4_theorem": self.lean_mathlib4_theorem,
            "lean_status": self.lean_status,
            "exercises": [
                {
                    "type": e.type,
                    "source": e.source,
                    "number": e.number,
                    "description": e.description,
                    "connects": e.connects,
                }
                for e in self.exercises
            ],
            "confidence": self.confidence,
        }


# ── helper ─────────────────────────────────────────────────────────────────

def _as_str_list(value: Any) -> List[str]:
    """Coerce a YAML value into a list of strings (handles scalar, None, list)."""
    if value is None:
        return []
    if isinstance(value, list):
        return [str(v) for v in value]
    if isinstance(value, str):
        return [value]
    return [str(value)]
