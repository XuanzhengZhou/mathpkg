---
role: proof
locale: en
of_concept: closed-balanced-convex-hull-compact
source_book: gtm015
source_chapter: "35"
source_section: "Compact convex sets in a TVS"
---

# Proof of Closed balanced convex hull of a set with compact closure is compact

Let $E$ be a complete, locally convex, separated topological vector space over $\mathbb{K}$, and let $S \subset E$ be a subset whose closure $\overline{S}$ is compact.

**Step 1.** Let $B = \operatorname{bal}(\operatorname{conv} S)$ be the balanced convex hull of $S$. The closed balanced convex hull of $S$ is $\overline{B}$, since the closure of a balanced set is balanced (17.5) and the closure of a convex set is convex (25.17). Thus it suffices to prove that $\overline{B}$ is compact.

**Step 2.** Since $\overline{S}$ is compact, $S$ is precompact (totally bounded). In a locally convex space, the balanced convex hull of a precompact set is precompact. {Indeed, given a convex, symmetric neighborhood $V$ of $\theta$, there exist $s_1, \ldots, s_n \in S$ with $S \subset \bigcup_k (s_k + V)$. Then $B \subset \operatorname{bal}(\operatorname{conv}\{s_1, \ldots, s_n\}) + V$; the first term is compact by Lemma (35.2) and properties of the balanced hull, hence precompact, so $B$ is covered by finitely many translates of $V + V + V$, establishing precompactness.} Therefore $B$ is precompact.

**Step 3.** In a complete uniform space, a set is compact if and only if it is complete and precompact (or, equivalently, the closure of a precompact set is compact — see 24.16). Since $E$ is complete and $B$ is precompact, its closure $\overline{B}$ is compact.

**Step 4 (Closed convex hull).** It follows at once that the closed convex hull $(\operatorname{conv} S)^-$ is also compact, because $(\operatorname{conv} S)^- \subset \overline{B}$ and every closed subset of a compact set is compact.

Thus the closed, balanced convex hull of $S$ is compact, and in particular the closed convex hull of $S$ is compact.
