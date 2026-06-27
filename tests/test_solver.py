"""Tests for the learning path resolver (solver.py)."""

import os
import sys
import unittest

# Ensure the project root is on the path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from mathpkg.graph.cache import KnowledgeCache
from mathpkg.resolver.solver import LearningPathResolver, LearningStep, LearningPath
from mathpkg.resolver.policy import Policy
from mathpkg.status.user_state import UserState


class TestLearningPathResolver(unittest.TestCase):
    """Test the dependency resolver with real group theory concepts."""

    @classmethod
    def setUpClass(cls):
        cls.cache = KnowledgeCache(":memory:")
        concepts_dir = os.path.join(
            os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
            "concepts"
        )
        if os.path.isdir(concepts_dir):
            cls.cache.rebuild_from_dir(concepts_dir)

    def setUp(self):
        # Use temp file to avoid inheriting CLI test state
        import tempfile
        self._tmpfile = os.path.join(tempfile.gettempdir(), "mathpkg_test_status.yaml")
        self.user = UserState(filepath=self._tmpfile)
        self.policy = Policy(install_recommends=True)

    @property
    def resolver(self):
        return LearningPathResolver(self.cache, self.user, self.policy)

    def test_resolve_lagrange_returns_path(self):
        """resolve('lagrange_theorem') should return a LearningPath with steps."""
        path = self.resolver.resolve("lagrange_theorem")
        self.assertIsInstance(path, LearningPath)
        self.assertEqual(path.target, "lagrange_theorem")
        self.assertGreater(path.new_to_learn, 0)
        self.assertGreater(len(path.steps), 0)

    def test_resolve_lagrange_includes_coset(self):
        """Lagrange requires coset, so coset should appear before lagrange."""
        path = self.resolver.resolve("lagrange_theorem")
        step_ids = [s.concept_id for s in path.steps]
        self.assertIn("coset", step_ids)
        self.assertIn("lagrange_theorem", step_ids)
        self.assertLess(step_ids.index("coset"), step_ids.index("lagrange_theorem"))

    def test_mastered_prunes_steps(self):
        """After mastering subgroup, the path should be shorter."""
        path_before = self.resolver.resolve("lagrange_theorem")
        self.user.mark("subgroup", "mastered")
        path_after = self.resolver.resolve("lagrange_theorem")
        self.assertLess(path_after.new_to_learn, path_before.new_to_learn)

    def test_policy_no_recommends_reduces_steps(self):
        """Without recommends, the path should be shorter or equal."""
        with_recs = self.resolver.resolve("lagrange_theorem")
        policy_no = Policy(install_recommends=False)
        resolver_no = LearningPathResolver(self.cache, self.user, policy_no)
        without_recs = resolver_no.resolve("lagrange_theorem")
        self.assertLessEqual(without_recs.new_to_learn, with_recs.new_to_learn)

    def test_resolve_root_returns_only_target(self):
        """Resolving a root concept (set_and_function) should have minimal steps."""
        path = self.resolver.resolve("set_and_function")
        self.assertLessEqual(path.new_to_learn, 1)

    def test_resolve_invalid_raises(self):
        """Resolving a nonexistent concept should raise ValueError."""
        with self.assertRaises(ValueError):
            self.resolver.resolve("nonexistent_concept_xyz")

    def test_suggested_followups(self):
        """Lagrange should suggest orbit-stabilizer and Cayley as followups."""
        followups = self.resolver.get_suggested_followups("lagrange_theorem")
        self.assertIn("orbit_stabilizer_theorem", followups)

    def test_detect_cycles_empty(self):
        """The group theory graph should have no cycles."""
        cycles = self.resolver.detect_cycles()
        self.assertEqual(len(cycles), 0, f"Unexpected cycles: {cycles}")

    def test_topological_sort_no_duplicates(self):
        """Ordered steps should have no duplicate concept IDs."""
        path = self.resolver.resolve("first_isomorphism_theorem")
        ids = [s.concept_id for s in path.steps]
        self.assertEqual(len(ids), len(set(ids)), f"Duplicates: {ids}")

    def test_learning_step_fields(self):
        """Each LearningStep should have all required fields populated."""
        path = self.resolver.resolve("lagrange_theorem")
        for step in path.steps:
            self.assertIsNotNone(step.concept_id)
            self.assertIsNotNone(step.name_en)
            self.assertIsNotNone(step.type)
            self.assertGreaterEqual(step.depth, 0)
            self.assertGreater(step.estimated_minutes, 0)

    def test_first_isomorphism_deps_all_present(self):
        """All required deps of first_isomorphism_theorem should be in the path."""
        path = self.resolver.resolve("first_isomorphism_theorem")
        step_ids = {s.concept_id for s in path.steps}
        for dep in ["quotient_group", "kernel_of_homomorphism",
                     "image_of_homomorphism", "group_isomorphism"]:
            self.assertIn(dep, step_ids, f"Missing required dep: {dep}")

    @classmethod
    def tearDownClass(cls):
        cls.cache.close()


class TestUserState(unittest.TestCase):
    """Test the user state tracking."""

    def setUp(self):
        self.user = UserState()

    def test_default_not_learned(self):
        self.assertEqual(self.user.get_state("any_concept"), "not_learned")

    def test_mark_and_retrieve(self):
        self.user.mark("group", "mastered", learned_from="GTM073")
        self.assertEqual(self.user.get_state("group"), "mastered")
        self.assertTrue(self.user.is_mastered("group"))

    def test_get_mastered(self):
        self.user.mark("a", "mastered")
        self.user.mark("b", "learning")
        self.user.mark("c", "mastered")
        mastered = self.user.get_mastered()
        self.assertIn("a", mastered)
        self.assertIn("c", mastered)
        self.assertNotIn("b", mastered)

    def test_get_in_progress(self):
        self.user.mark("x", "learning")
        self.user.mark("y", "stuck")
        self.user.mark("z", "mastered")
        in_progress = self.user.get_in_progress()
        self.assertIn("x", in_progress)
        self.assertIn("y", in_progress)
        self.assertNotIn("z", in_progress)

    def test_mark_with_notes(self):
        self.user.mark("subgroup", "stuck", notes="正规子群不懂")
        data = self.user._data["concepts"]["subgroup"]
        self.assertEqual(data.get("note"), "正规子群不懂")


if __name__ == "__main__":
    unittest.main(verbosity=2)
