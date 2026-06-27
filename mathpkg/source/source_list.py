"""
Source list management (modeled after apt's pkgSourceList).

Reads a sources.yaml file that declares where to find math concepts.
"""

from __future__ import annotations

import os
import logging
from dataclasses import dataclass, field
from typing import List, Optional

logger = logging.getLogger(__name__)

DEFAULT_SOURCES_PATH = "/home/a123/文档/mathpkg/sources.yaml"


@dataclass
class Source:
    """A single knowledge source entry."""
    name: str = ""
    uri: str = ""
    type: str = "local"      # local | git | http | arxiv
    enabled: bool = True


class SourceList:
    """
    Manages the list of registered knowledge sources.

    Equivalent to apt's pkgSourceList — reads the main sources file
    and provides the list of enabled Source objects.
    """

    def __init__(self, filepath: Optional[str] = None):
        self.filepath = filepath or DEFAULT_SOURCES_PATH
        self._sources: List[Source] = []
        self._reload()

    def _reload(self):
        """Re-read sources.yaml from disk."""
        self._sources = []

        if not os.path.isfile(self.filepath):
            logger.warning("sources file not found: %s", self.filepath)
            return

        import yaml

        try:
            with open(self.filepath, "r", encoding="utf-8") as fh:
                doc = yaml.safe_load(fh) or {}
        except Exception:
            logger.exception("Failed to parse %s", self.filepath)
            return

        entries = doc.get("sources", [])
        if not isinstance(entries, list):
            logger.warning("'sources' key in %s is not a list", self.filepath)
            return

        for entry in entries:
            if not isinstance(entry, dict):
                continue
            src = Source(
                name=entry.get("name", ""),
                uri=entry.get("uri", ""),
                type=entry.get("type", "local"),
                enabled=bool(entry.get("enabled", True)),
            )
            self._sources.append(src)

        logger.info("Loaded %d sources from %s", len(self._sources), self.filepath)

    @property
    def enabled(self) -> List[Source]:
        """Return only enabled sources."""
        return [s for s in self._sources if s.enabled]

    @property
    def all(self) -> List[Source]:
        """Return all sources (including disabled)."""
        return list(self._sources)

    def add_source(self, name: str, uri: str, stype: str = "local") -> None:
        """Add a new source entry (in-memory only for now)."""
        src = Source(name=name, uri=uri, type=stype, enabled=True)
        self._sources.append(src)

    def remove_source(self, name: str) -> bool:
        """Remove a source by name (in-memory only for now). Returns True if removed."""
        before = len(self._sources)
        self._sources = [s for s in self._sources if s.name != name]
        return len(self._sources) < before
