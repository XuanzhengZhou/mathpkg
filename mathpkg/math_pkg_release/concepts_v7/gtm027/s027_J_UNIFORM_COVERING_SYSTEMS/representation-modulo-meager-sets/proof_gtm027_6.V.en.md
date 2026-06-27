---
role: proof
locale: en
of_concept: representation-modulo-meager-sets
source_book: gtm027
source_chapter: "6"
source_section: "V"
---

# Proof: Representation Modulo Meager Sets in Boolean $\sigma$-Rings

Let $\mathcal{B}$ be the family of all compact open subsets of a locally compact Boolean space $X$. Let $\mathcal{Q}$ be the smallest family of subsets of $X$ containing $\mathcal{B}$ and closed under countable unions and symmetric differences. Let $\mathcal{M}$ be the family of all meager subsets of $X$.

For each $A \in \mathcal{Q}$, we claim there exists a *unique* $B \in \mathcal{B}$ such that $A \Delta B \in \mathcal{M}$ (i.e., $A$ and $B$ differ by a meager set).

**Existence:** Since $\mathcal{Q}$ is generated from $\mathcal{B}$ by countable unions and symmetric differences, and both operations respect the equivalence relation "differs by a meager set" (countable unions of meager sets are meager; symmetric differences of meager sets are meager), every $A \in \mathcal{Q}$ is equivalent modulo $\mathcal{M}$ to some member of the $\sigma$-completion of $\mathcal{B}$. By 6.P(a), this completion maps back to $\mathcal{B}$ modulo meager sets.

More concretely: for $A \in \mathcal{Q}$, write $A$ in terms of generators from $\mathcal{B}$ using the operations. The meager "error" propagates through, and the final representative in $\mathcal{B}$ is obtained from part (a) (which gives closure of $\mathcal{B}$ under countable supremum).

**Uniqueness:** If $B_1, B_2 \in \mathcal{B}$ and $B_1 \Delta B_2 \in \mathcal{M}$, then the symmetric difference of two compact open sets is both compact open and meager. In a Baire space (the Stone space of a $\sigma$-ring is Baire), the only compact open meager set is empty. Hence $B_1 = B_2$.
