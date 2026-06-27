"""
Learning path resolver (modeled after apt's DepCache + solver).

Core algorithm: expand dependencies via BFS, prune mastered concepts,
topological sort via Kahn's algorithm, enrich with recommended deps,
and package into a LearningPath.
"""

from __future__ import annotations

import logging
from collections import deque
from dataclasses import dataclass, field
from typing import List, Dict, Set, Tuple, Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from mathpkg.graph.cache import KnowledgeCache
    from mathpkg.status.user_state import UserState
    from mathpkg.resolver.policy import Policy

logger = logging.getLogger(__name__)


# ── data types ───────────────────────────────────────────────────────────────

@dataclass
class LearningStep:
    """A single step in a learning path."""
    concept_id: str
    name_en: str
    name_zh: str
    type: str               # theory | definition | theorem | lemma | corollary
    depth: int              # distance from target (target = 0)
    depends_on: List[str]   # concepts that must be learned before this step
    lean_verified: bool     # Mathlib4 has this theorem?
    estimated_minutes: int
    sources: List[str]      # recommended textbook sources (e.g. "GTM073 §I.4")


@dataclass
class LearningPath:
    """A complete learning plan from current knowledge to target concept."""
    target: str
    steps: List[LearningStep]       # ordered — first to last
    total_concepts: int             # all concepts in the graph for this topic
    already_mastered: int           # concepts user already knows
    new_to_learn: int               # len(steps)
    lean_verified_count: int        # how many steps have Mathlib4 backing
    estimated_total_minutes: int
    suggested_followups: List[str]  # natural next concepts after target


# ── resolver ──────────────────────────────────────────────────────────────────

class LearningPathResolver:
    """
    Dependency resolver for mathematical concepts.

    Equivalent to apt's DepCache — tracks what needs to be "installed"
    (learned) and in what order, respecting the dependency graph.

    Parameters
    ----------
    cache : KnowledgeCache
        The merged knowledge graph from all sources.
    user_state : UserState
        What the user already knows.
    policy : Policy
        Controls whether recommended/suggested deps are included.
    """

    def __init__(self, cache: KnowledgeCache, user_state: UserState, policy: Policy):
        self.cache = cache
        self.user_state = user_state
        self.policy = policy

    # ── main entry point ─────────────────────────────────────────────────

    def resolve(self, target: str) -> LearningPath:
        """
        Build a complete learning path for *target*.

        Returns a LearningPath, or raises ValueError if the target
        does not exist in the cache.
        """
        target_info = self.cache.find_concept(target)
        if target_info is None:
            raise ValueError(f"Concept '{target}' not found in cache")

        all_ids = set(self.cache.get_all_concepts())

        # Step 1: expand — collect all required dependencies via BFS
        needed: Dict[str, int] = {}  # concept_id -> depth
        self._expand(target, 0, needed, set())

        # Step 2: prune — remove concepts the user already mastered
        mastered = set(self.user_state.get_mastered())
        remaining = {cid for cid in needed if cid not in mastered}
        already = len(needed) - len(remaining)

        # Step 3: order — topological sort (Kahn's algorithm)
        ordered = self._topological_sort(remaining, all_ids)

        # Step 4: enrich — insert recommended dependencies per policy
        if self.policy.install_recommends:
            ordered = self._enrich_with_recommended(ordered, remaining, mastered)

        # Step 5: build LearningStep list
        steps: List[LearningStep] = []
        lean_count = 0
        for cid in ordered:
            info = self.cache.find_concept(cid)
            if info is None:
                continue
            verified = (info.get("lean_status") == "complete")
            if verified:
                lean_count += 1
            reqs = self.cache.get_dependencies(cid, "required")
            versions = self.cache.get_versions(cid)
            source_strs = [f"{v['source']} §{v.get('section','?')}" for v in versions[:2]]

            step = LearningStep(
                concept_id=cid,
                name_en=info.get("name_en", cid),
                name_zh=info.get("name_zh", cid),
                type=info.get("type", "definition"),
                depth=needed.get(cid, 0),
                depends_on=[d for d in reqs if d in remaining or d in needed],
                lean_verified=verified,
                estimated_minutes=self._estimate_time(info.get("type", "definition")),
                sources=source_strs,
            )
            steps.append(step)

        # Suggested follow-ups: concepts that depend on target
        followups = self.get_suggested_followups(target)

        path = LearningPath(
            target=target,
            steps=steps,
            total_concepts=len(all_ids),
            already_mastered=already,
            new_to_learn=len(steps),
            lean_verified_count=lean_count,
            estimated_total_minutes=sum(s.estimated_minutes for s in steps),
            suggested_followups=followups,
        )
        return path

    # ── dependency expansion (BFS) ────────────────────────────────────────

    def _expand(self, current: str, depth: int, needed: Dict[str, int],
                visited: Set[str]) -> None:
        """BFS along required edges. Populates *needed* with {id: depth}."""
        if depth > self.policy.max_depth:
            logger.warning("Max depth %d exceeded at %s", self.policy.max_depth, current)
            return
        if current in visited:
            return
        visited.add(current)

        # Record this concept (root gets depth 0, deps get increasing depth)
        if current not in needed or needed[current] < depth:
            needed[current] = depth

        for dep in self.cache.get_dependencies(current, "required"):
            self._expand(dep, depth + 1, needed, visited)

    # ── topological sort ──────────────────────────────────────────────────

    def _topological_sort(self, concept_ids: Set[str],
                          all_ids: Set[str]) -> List[str]:
        """
        Kahn's algorithm. Returns a topologically sorted list of *concept_ids*.

        Raises ValueError if a cycle is detected.
        """
        # Build subgraph
        in_degree: Dict[str, int] = {cid: 0 for cid in concept_ids}
        adjacency: Dict[str, List[str]] = {cid: [] for cid in concept_ids}

        for cid in concept_ids:
            for dep in self.cache.get_dependencies(cid, "required"):
                if dep in concept_ids:
                    in_degree[cid] += 1
                    adjacency.setdefault(dep, []).append(cid)

        # Kahn's algorithm
        queue: deque[str] = deque(cid for cid, deg in in_degree.items() if deg == 0)
        result: List[str] = []

        while queue:
            node = queue.popleft()
            result.append(node)
            for neighbor in adjacency.get(node, []):
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        if len(result) != len(concept_ids):
            remaining = [c for c, d in in_degree.items() if d > 0]
            raise ValueError(
                f"Cycle detected in dependency graph. "
                f"Remaining nodes: {remaining}. "
                f"Sorted so far: {len(result)}/{len(concept_ids)}"
            )
        return result

    # ── enrich with recommended ───────────────────────────────────────────

    def _enrich_with_recommended(self, ordered: List[str],
                                  remaining: Set[str],
                                  mastered: Set[str]) -> List[str]:
        """
        Insert recommended dependencies before each concept, if not already
        present in the ordered list and not mastered.
        """
        result: List[str] = []
        present: Set[str] = set(ordered) | mastered

        for cid in ordered:
            recs = self.cache.get_dependencies(cid, "recommended")
            for rec in recs:
                if rec not in present and rec in self.cache.get_all_concepts():
                    result.append(rec)
                    present.add(rec)
            result.append(cid)

        return result

    # ── follow-up suggestions ─────────────────────────────────────────────

    def get_suggested_followups(self, target: str) -> List[str]:
        """Return concepts that depend on *target* (natural next steps)."""
        return self.cache.get_dependents(target)

    # ── cycle detection ───────────────────────────────────────────────────

    def detect_cycles(self) -> List[Tuple[str, str]]:
        """
        Detect cycles anywhere in the full dependency graph.

        Returns a list of (from, to) edges that participate in cycles.
        Empty list means the graph is a DAG.
        """
        all_ids = self.cache.get_all_concepts()

        # Build adjacency
        adj: Dict[str, List[str]] = {cid: [] for cid in all_ids}
        for cid in all_ids:
            for dep in self.cache.get_dependencies(cid, "required"):
                if dep in adj:
                    adj[cid].append(dep)

        # DFS with recursion stack for cycle detection
        WHITE, GRAY, BLACK = 0, 1, 2
        color: Dict[str, int] = {cid: WHITE for cid in all_ids}
        cycle_edges: List[Tuple[str, str]] = []

        def dfs(u: str, parent: Optional[str] = None):
            color[u] = GRAY
            for v in adj.get(u, []):
                if color.get(v) == GRAY:
                    cycle_edges.append((u, v))
                elif color.get(v) == WHITE:
                    dfs(v, u)
            color[u] = BLACK

        for cid in all_ids:
            if color.get(cid) == WHITE:
                dfs(cid)

        return cycle_edges

    # ── helpers ───────────────────────────────────────────────────────────

    @staticmethod
    def _estimate_time(concept_type: str) -> int:
        """Estimate study time in minutes based on concept type."""
        estimates = {
            "theory": 60,
            "definition": 30,
            "theorem": 45,
            "lemma": 20,
            "corollary": 15,
        }
        return estimates.get(concept_type, 30)
