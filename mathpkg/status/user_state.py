"""
User knowledge state tracker with YAML persistence.

Tracks which concepts the user has mastered, is learning, stuck on, etc.
Persists to ~/.mathpkg/status.yaml.
"""

from __future__ import annotations

import os
import logging
from datetime import datetime
from typing import Dict, List, Optional, Set

logger = logging.getLogger(__name__)

DEFAULT_STATUS_PATH = os.path.expanduser("~/.mathpkg/status.yaml")

# Valid status values for a concept
STATUS_MASTERED = "mastered"
STATUS_STUCK = "stuck"
STATUS_SKIPPED = "skipped"
STATUS_UNKNOWN = "unknown"
STATUS_NOT_LEARNED = "not_learned"
STATUS_LEARNING = "learning"
STATUS_LEARNED = "learned"

VALID_STATUSES = frozenset({
    STATUS_MASTERED, STATUS_STUCK, STATUS_SKIPPED, STATUS_UNKNOWN,
    STATUS_NOT_LEARNED, STATUS_LEARNING, STATUS_LEARNED,
})


class UserState:
    """
    Tracks a user's knowledge state for individual concepts.

    Persists to ~/.mathpkg/status.yaml via YAML.
    """

    def __init__(self, filepath: Optional[str] = None):
        self.filepath = filepath or DEFAULT_STATUS_PATH
        self._states: Dict[str, str] = {}       # concept_id → status
        self._notes: Dict[str, str] = {}         # concept_id → user notes
        self._sources: Dict[str, str] = {}       # concept_id → textbook source
        self._timestamps: Dict[str, str] = {}    # concept_id → ISO timestamp
        self._load()  # auto-load from disk if file exists

    # ── query ──────────────────────────────────────────────────────────

    def status_of(self, concept_id: str) -> str:
        """Return the status for a concept (default: 'not_learned')."""
        return self._states.get(concept_id, STATUS_NOT_LEARNED)

    def get_state(self, concept_id: str) -> str:
        """Alias for status_of — used by resolver and CLI."""
        return self.status_of(concept_id)

    def is_mastered(self, concept_id: str) -> bool:
        return self.status_of(concept_id) in (STATUS_MASTERED, STATUS_LEARNED)

    def is_stuck(self, concept_id: str) -> bool:
        return self.status_of(concept_id) == STATUS_STUCK

    def is_learning(self, concept_id: str) -> bool:
        return self.status_of(concept_id) == STATUS_LEARNING

    def is_learned(self, concept_id: str) -> bool:
        return self.status_of(concept_id) == STATUS_LEARNED

    def is_known(self, concept_id: str) -> bool:
        """A concept is 'known' if the user has mastered or learned it."""
        return self.is_mastered(concept_id) or self.is_learned(concept_id)

    def get_note(self, concept_id: str) -> str:
        return self._notes.get(concept_id, "")

    def get_source(self, concept_id: str) -> str:
        return self._sources.get(concept_id, "")

    # ── mutation ───────────────────────────────────────────────────────

    def mark(self, concept_id: str, status: str, **kwargs) -> None:
        """Mark a concept with a given status. Accepts kwargs: note, source, learned_from, notes, confidence."""
        if status not in VALID_STATUSES:
            raise ValueError(f"Invalid status '{status}'. Must be one of {sorted(VALID_STATUSES)}")
        self._states[concept_id] = status

        note = kwargs.get("note") or kwargs.get("notes", "")
        source = kwargs.get("source") or kwargs.get("learned_from", "")
        if note:
            self._notes[concept_id] = note
        if source:
            self._sources[concept_id] = source
        if "confidence" in kwargs:
            self._timestamps[concept_id + "_confidence"] = str(kwargs["confidence"])
        self._timestamps[concept_id] = datetime.now().isoformat()

    @property
    def _data(self) -> dict:
        """Access internal state dict for CLI compatibility."""
        return {
            "concepts": {
                cid: {
                    "state": self._states.get(cid, STATUS_NOT_LEARNED),
                    "note": self._notes.get(cid, ""),
                    "source": self._sources.get(cid, ""),
                }
                for cid in sorted(set(self._states) | set(self._notes) | set(self._sources))
            }
        }

    def mark_mastered(self, concept_id: str, note: str = "", source: str = "") -> None:
        self.mark(concept_id, STATUS_MASTERED, note=note, source=source)

    def mark_stuck(self, concept_id: str, note: str = "") -> None:
        self.mark(concept_id, STATUS_STUCK, note)

    def mark_skipped(self, concept_id: str, note: str = "") -> None:
        self.mark(concept_id, STATUS_SKIPPED, note)

    def mark_learning(self, concept_id: str, note: str = "", source: str = "") -> None:
        self.mark(concept_id, STATUS_LEARNING, note, source)

    def mark_learned(self, concept_id: str, note: str = "", source: str = "") -> None:
        self.mark(concept_id, STATUS_LEARNED, note, source)

    def reset(self, concept_id: str) -> None:
        """Reset a concept's status to not_learned."""
        self._states.pop(concept_id, None)
        self._notes.pop(concept_id, None)
        self._sources.pop(concept_id, None)
        self._timestamps.pop(concept_id, None)

    # ── bulk query ─────────────────────────────────────────────────────

    def mastered_ids(self) -> Set[str]:
        return {cid for cid, s in self._states.items() if s == STATUS_MASTERED}

    def get_mastered(self) -> List[str]:
        """Return list of mastered (or learned) concept IDs. Used by resolver."""
        return sorted(
            cid for cid, s in self._states.items()
            if s in (STATUS_MASTERED, STATUS_LEARNED)
        )

    def get_in_progress(self) -> List[str]:
        """Return list of concepts currently being learned or stuck."""
        return sorted(
            cid for cid, s in self._states.items()
            if s in (STATUS_LEARNING, STATUS_STUCK)
        )

    def stuck_ids(self) -> Set[str]:
        return {cid for cid, s in self._states.items() if s == STATUS_STUCK}

    def learning_ids(self) -> Set[str]:
        return {cid for cid, s in self._states.items() if s == STATUS_LEARNING}

    def learned_ids(self) -> Set[str]:
        return {cid for cid, s in self._states.items() if s == STATUS_LEARNED}

    def all_known_ids(self) -> Set[str]:
        """All concept IDs that have been marked (any non-not_learned status)."""
        return set(self._states.keys())

    # ── stats ──────────────────────────────────────────────────────────

    def stats(self) -> Dict[str, int]:
        """Return counts of each status across all tracked concepts."""
        counts = {
            STATUS_MASTERED: 0,
            STATUS_LEARNING: 0,
            STATUS_LEARNED: 0,
            STATUS_STUCK: 0,
            STATUS_SKIPPED: 0,
            STATUS_NOT_LEARNED: 0,
        }
        for s in self._states.values():
            if s in counts:
                counts[s] += 1
        return counts

    def get_unlocked(self, cache) -> List[str]:
        """
        Return concepts whose required dependencies are all mastered,
        and which the user has not yet mastered themselves.
        """
        all_concepts = cache.get_all_concepts()
        unlocked = []
        for cid in all_concepts:
            if self.is_mastered(cid):
                continue
            deps = cache.get_dependencies(cid, "required")
            if all(self.is_mastered(d) for d in deps):
                unlocked.append(cid)
        return sorted(unlocked)

    def _load(self) -> None:
        """Auto-load state from disk if the YAML file exists. Called from __init__."""
        import yaml

        if not os.path.isfile(self.filepath):
            return

        with open(self.filepath, "r", encoding="utf-8") as fh:
            data = yaml.safe_load(fh) or {}

        concepts = data.get("concepts", {})
        for cid, entry in concepts.items():
            if not isinstance(entry, dict):
                continue
            status = entry.get("status", entry.get("state", STATUS_UNKNOWN))
            note = entry.get("note", "")
            source = entry.get("source", "")
            timestamp = entry.get("timestamp", "")
            self._states[cid] = status
            if note:
                self._notes[cid] = note
            if source:
                self._sources[cid] = source
            if timestamp:
                self._timestamps[cid] = timestamp

    def to_dict(self) -> dict:
        """Serialize to a dict (for YAML persistence)."""
        return {
            "last_updated": datetime.now().isoformat(),
            "concepts": {
                cid: {
                    "status": self._states[cid],
                    "note": self._notes.get(cid, ""),
                    "source": self._sources.get(cid, ""),
                    "timestamp": self._timestamps.get(cid, ""),
                }
                for cid in sorted(self._states)
            },
        }

    def save(self) -> None:
        """Save state to disk as YAML."""
        import yaml

        os.makedirs(os.path.dirname(self.filepath), exist_ok=True)
        with open(self.filepath, "w", encoding="utf-8") as fh:
            yaml.dump(self.to_dict(), fh, allow_unicode=True, default_flow_style=False)
        logger.debug("UserState saved to %s (%d concepts)",
                     self.filepath, len(self._states))

    @classmethod
    def load(cls, filepath: Optional[str] = None) -> "UserState":
        """Load state from disk. Returns a new empty state if no file exists."""
        import yaml

        state = cls(filepath)
        path = state.filepath
        if not os.path.isfile(path):
            logger.debug("No status file at %s, starting empty.", path)
            return state

        with open(path, "r", encoding="utf-8") as fh:
            data = yaml.safe_load(fh) or {}

        concepts = data.get("concepts", {})
        for cid, entry in concepts.items():
            if not isinstance(entry, dict):
                continue
            status = entry.get("status", STATUS_UNKNOWN)
            note = entry.get("note", "")
            source = entry.get("source", "")
            timestamp = entry.get("timestamp", "")
            state._states[cid] = status
            if note:
                state._notes[cid] = note
            if source:
                state._sources[cid] = source
            if timestamp:
                state._timestamps[cid] = timestamp

        logger.debug("UserState loaded from %s (%d concepts)", path, len(state._states))
        return state
