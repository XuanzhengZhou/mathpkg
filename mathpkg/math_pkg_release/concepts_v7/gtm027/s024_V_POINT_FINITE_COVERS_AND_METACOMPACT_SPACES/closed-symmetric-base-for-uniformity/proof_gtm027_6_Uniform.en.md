---
role: proof
locale: en
of_concept: closed-symmetric-base-for-uniformity
source_book: gtm027
source_chapter: "6"
source_section: "Uniform Spaces"
---

# Proof that Closed Symmetric Members Form a Base for a Uniformity (Theorem 6.8)

**Theorem 6.8.** The family of closed symmetric members of a uniformity $\mathcal{U}$ is a base for $\mathcal{U}$.

**Proof.** Let $U \in \mathcal{U}$ and choose $V \in \mathcal{U}$ such that $V \circ V \circ V \subset U$. By a result concerning the closure in uniform spaces (Theorem 6.7), the closure $\overline{V}$ of $V$ in $X \times X$ satisfies $\overline{V} \subset V \circ V \circ V$. Therefore $\overline{V} \subset U$, so $U$ contains the closed member $\overline{V}$ of $\mathcal{U}$.

Now $W = \overline{V} \cap \overline{V}^{-1}$ is a closed symmetric member of $\mathcal{U}$ (since $\mathcal{U}$ is closed under inverses and finite intersections). Since $W \subset \overline{V} \subset U$, we have found a closed symmetric member of $\mathcal{U}$ contained in $U$.

Thus every member of $\mathcal{U}$ contains a closed symmetric member, so the family of closed symmetric members is a base for $\mathcal{U}$.
