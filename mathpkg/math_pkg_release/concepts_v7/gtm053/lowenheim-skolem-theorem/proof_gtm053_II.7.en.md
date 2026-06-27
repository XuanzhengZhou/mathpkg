---
role: proof
locale: en
of_concept: lowenheim-skolem-theorem
source_book: gtm053
source_chapter: "II"
source_section: "7"
---

# Proof of the Löwenheim-Skolem Theorem

**Theorem 7.4 (Löwenheim-Skolem).** If a set of formulas $\mathcal{E}$ in a first-order language $L$ has a model, then it has a model of cardinality at most $|L| + \aleph_0$.

*Proof.* This theorem follows immediately as a corollary of Gödel's Completeness Theorem (II.6.2).

Suppose $\mathcal{E}$ has a model. Then $\mathcal{E}$ is consistent (since a satisfiable set cannot be inconsistent). By the proof of the Completeness Theorem, we construct a canonical model whose domain consists of equivalence classes of variable-free terms in the extended language $L^{(\infty)}$.

The number of variable-free terms in $L^{(\infty)}$ is at most $|L^{(\infty)}| = |L| + \aleph_0$, since terms are finite strings over the alphabet of $L^{(\infty)}$ and there are only countably many finite strings over an alphabet of size $|L| + \aleph_0$.

The equivalence relation $t_1 \sim t_2 \iff (t_1 = t_2) \in \mathcal{E}^{(\infty)}$ partitions these terms into equivalence classes, so the number of equivalence classes is also at most $|L| + \aleph_0$.

Thus the canonical model constructed in the proof of the Completeness Theorem has cardinality $\leq |L| + \aleph_0$, and its reduct to $L$ is a model of $\mathcal{E}$ of the same cardinality.

**Note on the downward vs. upward direction.** The downward Löwenheim-Skolem theorem (every satisfiable theory has a small model) is a direct consequence of the Henkin construction. The upward direction (every theory with infinite models has arbitrarily large models) follows from the Compactness Theorem by adding new constant symbols and the diagram method. $\square$
