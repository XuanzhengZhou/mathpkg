---
role: proof
locale: en
of_concept: coset-equality-lemma
source_book: gtm077
source_chapter: "II"
source_section: "6"
---

# Proof of the Coset Equality Lemma

Let $\mathfrak{G}$ be a group and $\mathfrak{U}$ a subgroup with elements $U_1, U_2, \ldots, U_N$ (where $N$ may be infinite). For any $A \in \mathfrak{G}$, the left coset $A\mathfrak{U}$ is defined as $\{AU_i : U_i \in \mathfrak{U}\}$.

**Lemma.** If two cosets $A\mathfrak{U}$ and $B\mathfrak{U}$ have one element in common, then they are identical as sets.

**Proof.** Suppose there exist $U_a, U_b \in \mathfrak{U}$ such that $AU_a = BU_b$. Then

$$B = A U_a U_b^{-1}.$$

For any element $BU_i \in B\mathfrak{U}$, we have

$$BU_i = A U_a U_b^{-1} U_i.$$

Since $\mathfrak{U}$ is a subgroup, $U_a U_b^{-1} U_i \in \mathfrak{U}$, so $BU_i \in A\mathfrak{U}$. Thus $B\mathfrak{U} \subseteq A\mathfrak{U}$. By symmetry, $A\mathfrak{U} \subseteq B\mathfrak{U}$. Hence $A\mathfrak{U} = B\mathfrak{U}$.

Equivalently, the cosets of $\mathfrak{U}$ form a partition of $\mathfrak{G}$: two cosets are either disjoint or identical. This partition property is fundamental to the proof of Lagrange's Theorem. ∎
