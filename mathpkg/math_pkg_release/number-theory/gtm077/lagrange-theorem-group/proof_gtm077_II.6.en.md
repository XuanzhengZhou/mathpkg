---
role: proof
locale: en
of_concept: lagrange-theorem-group
source_book: gtm077
source_chapter: "II"
source_section: "6"
---

# Proof of Theorem 19 (Lagrange's Theorem)

**Theorem 19.** In a finite group $\mathfrak{G}$ of order $h$, the order $N$ of each subgroup $\mathfrak{U}$ is a divisor of $h$. The quotient $j = h/N$ is called the *index* of $\mathfrak{U}$ in $\mathfrak{G}$.

**Proof.** Let $\mathfrak{U} = (U_1, U_2, \ldots, U_N)$ be a subgroup of $\mathfrak{G}$ of order $N$.

**Step 1: Cosets partition the group.** For any $A \in \mathfrak{G}$, define the left coset $A\mathfrak{U} = (AU_1, AU_2, \ldots, AU_N)$. We prove the Lemma: If two cosets $A\mathfrak{U}$ and $B\mathfrak{U}$ have one element in common, then they are identical.

Suppose $AU_a = BU_b$. Then $B = AU_a U_b^{-1}$, and for any $i$,

$$BU_i = AU_a U_b^{-1} U_i.$$

Since $\mathfrak{U}$ is a group, $U_a U_b^{-1} U_i$ runs through all elements of $\mathfrak{U}$ as $i = 1, \ldots, N$. Thus $B\mathfrak{U}$ consists of exactly the same elements as $A\mathfrak{U}$, possibly in a different order. Two cosets are therefore either disjoint or identical, and the distinct cosets form a partition of $\mathfrak{G}$.

**Step 2: Each coset has $N$ elements.** The map $U_i \mapsto AU_i$ is a bijection from $\mathfrak{U}$ to $A\mathfrak{U}$: it is injective because $AU_i = AU_j$ implies $U_i = U_j$ (multiply on the left by $A^{-1}$), and surjective by definition. Hence $|A\mathfrak{U}| = |\mathfrak{U}| = N$.

**Step 3: Counting.** Let $j$ be the number of distinct cosets. Since $\mathfrak{G}$ is the disjoint union of these $j$ cosets and each contains exactly $N$ elements,

$$h = j \cdot N.$$

Thus $N \mid h$, and $j = h/N$ is the index of $\mathfrak{U}$ in $\mathfrak{G}$.

**Note on infinite groups.** If $\mathfrak{G}$ is infinite, the index is defined as the number of distinct cosets (which may be finite or infinite), and at least one of $N$ or $j$ must be infinite. ∎
