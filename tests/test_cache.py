#!/usr/bin/env python3
"""
Unit tests for the KnowledgeCache (SQLite graph cache).

Tests find_concept, get_dependencies, get_all_concepts, get_dependents.
Uses an in-memory database and inserts test data directly via Concept objects.
"""

from __future__ import annotations

import os
import sys
import tempfile
import unittest

# Ensure mathpkg package is importable from the project root.
_PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if _PROJECT_ROOT not in sys.path:
    sys.path.insert(0, _PROJECT_ROOT)

from mathpkg.graph.cache import KnowledgeCache
from mathpkg.graph.concept import Concept, ConceptVersion, Statement, Exercise


# ── helpers ────────────────────────────────────────────────────────────────

def _make_concept(
    cid: str,
    name_en: str,
    name_zh: str = "",
    ctype: str = "definition",
    required: list | None = None,
    recommended: list | None = None,
    suggested: list | None = None,
    lean_status: str = "none",
    confidence: float = 0.8,
    versions: list | None = None,
    statements: list | None = None,
    exercises: list | None = None,
    lean_path: str | None = None,
    lean_theorem: str | None = None,
) -> Concept:
    """Quickly construct a minimal Concept for testing."""
    return Concept(
        id=cid,
        name_en=name_en,
        name_zh=name_zh,
        type=ctype,
        depends_required=required or [],
        depends_recommended=recommended or [],
        depends_suggested=suggested or [],
        versions=versions or [],
        statements=statements or [],
        exercises=exercises or [],
        lean_mathlib4_path=lean_path,
        lean_mathlib4_theorem=lean_theorem,
        lean_status=lean_status,
        confidence=confidence,
    )


# ── test case ──────────────────────────────────────────────────────────────

class TestKnowledgeCache(unittest.TestCase):
    """Tests for KnowledgeCache with in-memory SQLite."""

    def setUp(self):
        self.cache = KnowledgeCache(db_path=":memory:")
        self._populate_test_data()

    def tearDown(self):
        self.cache.close()

    def _insert(self, concept: Concept):
        """Insert a concept directly into the cache's SQLite tables."""
        self.cache._insert_concept(concept)

    def _populate_test_data(self):
        """Build a small dependency graph for testing.

        Graph:
            set_theory (no deps)
            function   (depends: set_theory)
            group      (depends: function [required], monoid [recommended])
            subgroup   (depends: group)
            lagrange   (depends: subgroup)
        """
        c1 = _make_concept("set_theory", "Set Theory", "集合论", "theory")
        c2 = _make_concept("function", "Function", "函数", "definition",
                            required=["set_theory"])
        c3 = _make_concept("group", "Group", "群", "definition",
                            required=["function"],
                            recommended=["monoid"])
        c4 = _make_concept("subgroup", "Subgroup", "子群", "definition",
                            required=["group"])
        c5 = _make_concept("lagrange", "Lagrange's Theorem", "拉格朗日定理", "theorem",
                            required=["subgroup"],
                            lean_status="complete",
                            confidence=1.0,
                            versions=[
                                ConceptVersion(source="GTM073", author="Hungerford",
                                               chapter="I", section="I.4",
                                               pages="38-40", theorem_number="4.6")
                            ],
                            statements=[
                                Statement(type="theorem",
                                          name="Lagrange's Theorem",
                                          latex="|H| divides |G|",
                                          proof_sketch="Use cosets.")
                            ])
        for c in [c1, c2, c3, c4, c5]:
            self._insert(c)

    # ── tests ──────────────────────────────────────────────────────────

    def test_get_all_concepts(self):
        ids = self.cache.get_all_concepts()
        self.assertEqual(len(ids), 5)
        self.assertIn("set_theory", ids)
        self.assertIn("lagrange", ids)

    def test_find_concept_exists(self):
        info = self.cache.find_concept("group")
        self.assertIsNotNone(info)
        self.assertEqual(info["id"], "group")
        self.assertEqual(info["name_en"], "Group")
        self.assertEqual(info["type"], "definition")

    def test_find_concept_missing(self):
        info = self.cache.find_concept("nonexistent")
        self.assertIsNone(info)

    def test_get_dependencies_required(self):
        deps = self.cache.get_dependencies("lagrange", "required")
        self.assertEqual(deps, ["subgroup"])

        deps = self.cache.get_dependencies("group", "required")
        self.assertEqual(deps, ["function"])

    def test_get_dependencies_recommended(self):
        deps = self.cache.get_dependencies("group", "recommended")
        self.assertEqual(deps, ["monoid"])

    def test_get_dependencies_empty(self):
        deps = self.cache.get_dependencies("set_theory", "required")
        self.assertEqual(deps, [])

    def test_get_dependents(self):
        deps = self.cache.get_dependents("group")
        self.assertIn("subgroup", deps)
        self.assertEqual(len(deps), 1)

        deps = self.cache.get_dependents("function")
        self.assertIn("group", deps)
        self.assertEqual(len(deps), 1)

    def test_get_dependents_root(self):
        # lagrange depends on nothing, but subgroup depends on it
        deps = self.cache.get_dependents("lagrange")
        self.assertEqual(deps, [])

    def test_get_versions(self):
        versions = self.cache.get_versions("lagrange")
        self.assertEqual(len(versions), 1)
        self.assertEqual(versions[0]["source"], "GTM073")
        self.assertEqual(versions[0]["author"], "Hungerford")

    def test_get_versions_empty(self):
        versions = self.cache.get_versions("set_theory")
        self.assertEqual(versions, [])

    # ── YAML round-trip (if real YAML files exist) ────────────────────

    def test_yaml_loading(self):
        """If real concept YAML files exist, load them to verify format."""
        concepts_dir = os.path.join(_PROJECT_ROOT, "concepts")
        yaml_files: list[str] = []
        for root, _dirs, files in os.walk(concepts_dir):
            for fn in files:
                if fn.endswith(".yaml") and fn != "index.yaml":
                    yaml_files.append(os.path.join(root, fn))

        if yaml_files:
            for yp in yaml_files:
                try:
                    c = Concept.from_yaml(yp)
                    self.assertTrue(c.id, f"Concept from {yp} must have an id")
                except Exception as exc:
                    self.fail(f"Failed to load {yp}: {exc}")


class TestRebuildFromDir(unittest.TestCase):
    """Test rebuild_from_dir with a temporary concept tree."""

    def test_rebuild_from_temp_dir(self):
        """Create a minimal concept directory with index.yaml and a .yaml,
        then rebuild the cache from it."""
        with tempfile.TemporaryDirectory() as tmpdir:
            topic_dir = os.path.join(tmpdir, "algebra", "group_theory")
            nodes_dir = os.path.join(topic_dir, "nodes")
            os.makedirs(nodes_dir, exist_ok=True)

            # Write index.yaml
            index_path = os.path.join(topic_dir, "index.yaml")
            with open(index_path, "w") as f:
                f.write("""\
source_name: test-groups
topics:
  - name: Group Theory Basics
    concepts:
      - group
      - subgroup
""")

            # Write concept .yaml files
            with open(os.path.join(nodes_dir, "group.yaml"), "w") as f:
                f.write("""\
id: group
name:
  en: Group
  zh: "群"
type: definition
depends:
  required:
    - monoid
  recommended: []
  suggested: []
versions:
  - source: "GTM073"
    author: "Hungerford"
    chapter: "I"
    section: "I.2"
lean:
  status: partial
confidence: 0.9
""")

            with open(os.path.join(nodes_dir, "subgroup.yaml"), "w") as f:
                f.write("""\
id: subgroup
name:
  en: Subgroup
  zh: "子群"
type: definition
depends:
  required:
    - group
  recommended: []
  suggested: []
versions: []
lean:
  status: none
confidence: 0.8
""")

            # Rebuild
            cache = KnowledgeCache(db_path=":memory:")
            try:
                cache.rebuild_from_dir(tmpdir)

                all_ids = cache.get_all_concepts()
                self.assertIn("group", all_ids)
                self.assertIn("subgroup", all_ids)

                group_info = cache.find_concept("group")
                self.assertIsNotNone(group_info)
                self.assertEqual(group_info["name_en"], "Group")

                deps = cache.get_dependencies("subgroup", "required")
                self.assertEqual(deps, ["group"])

            finally:
                cache.close()


# ── main ───────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    # Run tests and print a clear result.
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromModule(sys.modules[__name__])
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    if result.wasSuccessful():
        print("\n✓ ALL TESTS PASSED")
    else:
        print(f"\n✗ {len(result.failures)} failures, {len(result.errors)} errors")
        sys.exit(1)
