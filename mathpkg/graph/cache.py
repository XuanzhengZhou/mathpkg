"""
SQLite-based knowledge graph cache (modeled after apt's pkgCache).

Tables
------
concepts(id TEXT PRIMARY KEY, name_en TEXT, name_zh TEXT, type TEXT,
         lean_status TEXT, confidence REAL)
dependencies(from_concept TEXT, to_concept TEXT, dep_type TEXT,
             PRIMARY KEY(from_concept, to_concept, dep_type))
concept_versions(concept_id TEXT, source TEXT, author TEXT, chapter TEXT,
                 section TEXT, pages TEXT, theorem_number TEXT,
                 PRIMARY KEY(concept_id, source))
"""

from __future__ import annotations

import os
import sqlite3
import logging
from typing import Optional, Dict, List

from .concept import Concept

logger = logging.getLogger(__name__)

DDL_STATEMENTS = [
    """
    CREATE TABLE IF NOT EXISTS concepts (
        id                    TEXT PRIMARY KEY,
        name_en               TEXT,
        name_zh               TEXT,
        type                  TEXT,
        lean_status           TEXT,
        lean_mathlib4_path    TEXT,
        lean_mathlib4_theorem TEXT,
        confidence            REAL
    )
    """,
    """
    CREATE TABLE IF NOT EXISTS dependencies (
        from_concept  TEXT,
        to_concept    TEXT,
        dep_type      TEXT,
        PRIMARY KEY   (from_concept, to_concept, dep_type)
    )
    """,
    """
    CREATE TABLE IF NOT EXISTS concept_versions (
        concept_id     TEXT,
        source         TEXT,
        author         TEXT,
        chapter        TEXT,
        section        TEXT,
        pages          TEXT,
        theorem_number TEXT,
        PRIMARY KEY    (concept_id, source)
    )
    """,
]


class KnowledgeCache:
    """
    SQLite-backed knowledge graph cache.

    Equivalent to apt's pkgCache — stores merged metadata from all sources.
    """

    def __init__(self, db_path: str = ":memory:"):
        self.db_path = db_path
        self.conn = sqlite3.connect(db_path)
        self.conn.execute("PRAGMA journal_mode=WAL")
        self.conn.execute("PRAGMA foreign_keys=ON")
        self._ensure_tables()

    def _ensure_tables(self):
        for ddl in DDL_STATEMENTS:
            self.conn.execute(ddl)
        self.conn.commit()
        self._migrate_add_lean_columns()

    def _migrate_add_lean_columns(self):
        """Add lean_mathlib4_path and lean_mathlib4_theorem columns if missing."""
        existing = {row[1] for row in self.conn.execute("PRAGMA table_info(concepts)")}
        for col_name in ("lean_mathlib4_path", "lean_mathlib4_theorem"):
            if col_name not in existing:
                try:
                    self.conn.execute(f"ALTER TABLE concepts ADD COLUMN {col_name} TEXT")
                    logger.info("Added column %s to concepts table", col_name)
                except sqlite3.OperationalError:
                    pass
        self.conn.commit()

    # ── rebuild from a concepts directory ──────────────────────────────

    def rebuild_from_dir(self, concepts_dir: str):
        """
        Walk *concepts_dir*, find every index.yaml under */**/,
        parse each one, load every concept .yaml listed therein,
        and insert everything into SQLite.

        This is the equivalent of ``apt update``.
        """
        self._clear_all()

        index_files: List[str] = []
        for root, dirs, files in os.walk(concepts_dir):
            for fn in files:
                if fn == "index.yaml":
                    index_files.append(os.path.join(root, fn))

        if not index_files:
            logger.warning("No index.yaml files found under %s", concepts_dir)
            return

        for ipath in sorted(index_files):
            self._process_index(ipath)

        self.conn.commit()
        logger.info("Rebuilt cache from %d index files under %s",
                    len(index_files), concepts_dir)

    def _process_index(self, index_path: str):
        """Parse one index.yaml and ingest all listed concepts."""
        import yaml

        with open(index_path, "r", encoding="utf-8") as fh:
            doc = yaml.safe_load(fh) or {}

        source_name = doc.get("source_name", os.path.basename(os.path.dirname(index_path)))
        topics = doc.get("topics", [])
        concept_ids: List[str] = []
        for topic in topics:
            for cid in topic.get("concepts", []):
                cid = str(cid).strip()
                if cid and cid not in concept_ids:
                    concept_ids.append(cid)

        # The directory containing index.yaml is the "root" of those concepts
        root_dir = os.path.dirname(index_path)
        loaded = 0
        for cid in concept_ids:
            yaml_path = self._find_concept_yaml(root_dir, cid)
            if yaml_path is None:
                logger.warning("Concept yaml not found for %s (source %s)", cid, source_name)
                continue
            try:
                concept = Concept.from_yaml(yaml_path)
                self._insert_concept(concept)
                loaded += 1
            except Exception:
                logger.exception("Failed to load concept from %s", yaml_path)

        logger.info("Index %s: loaded %d/%d concepts",
                     source_name, loaded, len(concept_ids))

    @staticmethod
    def _find_concept_yaml(root_dir: str, concept_id: str) -> Optional[str]:
        """
        Search for a concept's .yaml file in the directory tree.

        Tries several common patterns:
          1. root_dir/concept_id.yaml
          2. root_dir/nodes/concept_id.yaml
          3. root_dir <walk> concept_id.yaml
        """
        candidates = [
            os.path.join(root_dir, f"{concept_id}.yaml"),
            os.path.join(root_dir, "nodes", f"{concept_id}.yaml"),
        ]
        for cand in candidates:
            if os.path.isfile(cand):
                return cand

        # fallback: walk the tree (breadth-first limited depth)
        for r, _dirs, files in os.walk(root_dir):
            for fn in files:
                if fn == f"{concept_id}.yaml":
                    return os.path.join(r, fn)
        return None

    def _insert_concept(self, concept: Concept):
        self.conn.execute(
            """INSERT OR REPLACE INTO concepts
               (id, name_en, name_zh, type, lean_status, confidence)
               VALUES (?, ?, ?, ?, ?, ?)""",
            (concept.id, concept.name_en, concept.name_zh,
             concept.type, concept.lean_status, concept.confidence),
        )

        # dependencies
        for dep_type, dep_list in [
            ("required", concept.depends_required),
            ("recommended", concept.depends_recommended),
            ("suggested", concept.depends_suggested),
        ]:
            for target in dep_list:
                self.conn.execute(
                    """INSERT OR IGNORE INTO dependencies
                       (from_concept, to_concept, dep_type)
                       VALUES (?, ?, ?)""",
                    (concept.id, target, dep_type),
                )

        # versions
        for v in concept.versions:
            self.conn.execute(
                """INSERT OR REPLACE INTO concept_versions
                   (concept_id, source, author, chapter, section, pages, theorem_number)
                   VALUES (?, ?, ?, ?, ?, ?, ?)""",
                (concept.id, v.source, v.author, v.chapter,
                 v.section, v.pages, v.theorem_number),
            )

    # ── query helpers ──────────────────────────────────────────────────

    def find_concept(self, concept_id: str) -> Optional[Dict]:
        """Look up a concept by its id. Returns None if not found."""
        cur = self.conn.execute(
            "SELECT id, name_en, name_zh, type, lean_status, confidence "
            "FROM concepts WHERE id = ?",
            (concept_id,),
        )
        row = cur.fetchone()
        if row is None:
            return None
        return {
            "id": row[0],
            "name_en": row[1],
            "name_zh": row[2],
            "type": row[3],
            "lean_status": row[4],
            "confidence": row[5],
        }

    def get_dependencies(self, concept_id: str, dep_type: str = "required") -> List[str]:
        """Return all concepts that *concept_id* depends on of the given type."""
        cur = self.conn.execute(
            "SELECT to_concept FROM dependencies "
            "WHERE from_concept = ? AND dep_type = ? "
            "ORDER BY to_concept",
            (concept_id, dep_type),
        )
        return [row[0] for row in cur.fetchall()]

    def get_all_concepts(self) -> List[str]:
        """Return all concept IDs in the cache (sorted)."""
        cur = self.conn.execute("SELECT id FROM concepts ORDER BY id")
        return [row[0] for row in cur.fetchall()]

    def get_dependents(self, concept_id: str) -> List[str]:
        """
        Reverse lookup — return all concept IDs that depend on *concept_id*.
        """
        cur = self.conn.execute(
            "SELECT DISTINCT from_concept FROM dependencies "
            "WHERE to_concept = ? ORDER BY from_concept",
            (concept_id,),
        )
        return [row[0] for row in cur.fetchall()]

    def get_versions(self, concept_id: str) -> List[Dict]:
        """Return all known versions/sources for a concept."""
        cur = self.conn.execute(
            "SELECT source, author, chapter, section, pages, theorem_number "
            "FROM concept_versions WHERE concept_id = ? ORDER BY source",
            (concept_id,),
        )
        return [
            {
                "source": r[0], "author": r[1], "chapter": r[2],
                "section": r[3], "pages": r[4], "theorem_number": r[5],
            }
            for r in cur.fetchall()
        ]

    # ── internal ───────────────────────────────────────────────────────

    def _clear_all(self):
        self.conn.execute("DELETE FROM concept_versions")
        self.conn.execute("DELETE FROM dependencies")
        self.conn.execute("DELETE FROM concepts")
        self.conn.commit()

    def close(self):
        self.conn.close()
