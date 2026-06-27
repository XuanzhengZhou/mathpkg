---
role: proof
locale: en
of_concept: lagrange-theorem
source_book: gtm077
source_chapter: "II"
source_section: "6"
---

# Proof of Lagrange's Theorem (Theorem 19)

Let $\mathfrak{G}$ be a finite group of order $h$, and let $\mathfrak{U}$ be a subgroup of $\mathfrak{G}$ of order $N$. Denote the elements of $\mathfrak{U}$ by $U_1, U_2, \ldots, U_N$.

For any element $A \in \mathfrak{G}$, define the left coset

$$A\mathfrak{U} = (AU_1, AU_2, \ldots, AU_N).$$

**Step 1: Cosets partition the group.** We first prove the Lemma: If two cosets $A\mathfrak{U}$ and $B\mathfrak{U}$ have one element in common, then they are identical.

Suppose $AU_a = BU_b$ for some indices $a, b$. Then $B = AU_a U_b^{-1}$. Consequently,

$$B\mathfrak{U} = (AU_a U_b^{-1} U_1, AU_a U_b^{-1} U_2, \ldots, AU_a U_b^{-1} U_N).$$

Since $\mathfrak{U}$ is a group, the products $U_a U_b^{-1} U_i$ run through all elements of $\mathfrak{U}$ as $i = 1, 2, \ldots, N$. Hence $B\mathfrak{U}$ consists of exactly the same elements as $A\mathfrak{U}$, only possibly in a different order. Thus two cosets are either disjoint or identical, and the collection of all distinct cosets forms a partition of $\mathfrak{G}$.

**Step 2: Each coset has $N$ elements.** The number of distinct elements in a coset $A\mathfrak{U}$ equals the order of $\mathfrak{U}$, i.e., $N$. This follows because the mapping $U_i \mapsto AU_i$ is a bijection from $\mathfrak{U}$ to $A\mathfrak{U}$: it is injective since $AU_i = AU_j$ implies $U_i = U_j$ by left cancellation (multiply by $A^{-1}$), and it is surjective by definition of the coset.

**Step 3: Count the elements of $\mathfrak{G}$.** Let $j$ denote the number of distinct cosets of $\mathfrak{U}$ in $\mathfrak{G}$. Since $\mathfrak{G}$ is the disjoint union of these $j$ cosets, and each coset contains exactly $N$ elements, we obtain

$$h = j \cdot N.$$

Therefore $N$ divides $h$, i.e., the order of every subgroup $\mathfrak{U}$ is a divisor of the order of the group $\mathfrak{G}$.

The quotient $j = h/N$ is called the *index* of the subgroup $\mathfrak{U}$ in $\mathfrak{G}$.
