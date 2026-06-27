---
role: proof
locale: en
of_concept: lemma-d3467214a4
source_book: gtm077
source_chapter: "II"
source_section: "6"
---

# Proof: Coset Equality Lemma

Let $\mathfrak{U} = (U_1, U_2, \ldots, U_N)$ be a subgroup of $\mathfrak{G}$. For any $A \in \mathfrak{G}$, the left coset is defined as

$$A\mathfrak{U} = (AU_1, AU_2, \ldots, AU_N).$$

**Lemma.** If two cosets $A\mathfrak{U}$ and $B\mathfrak{U}$ have one element in common, then they have all elements in common, thus they agree except for order.

**Proof.** Suppose $AU_a = BU_b$ is a common element for some indices $a, b$. Then multiplying on the right by $U_b^{-1}$ yields

$$B = AU_a U_b^{-1}.$$

Consequently,

$$B\mathfrak{U} = (AU_a U_b^{-1} U_1, AU_a U_b^{-1} U_2, \ldots, AU_a U_b^{-1} U_N).$$

Now observe that as $i$ runs through $1, 2, \ldots, N$, the products $U_a U_b^{-1} U_i$ run through all elements of $\mathfrak{U}$. This follows from the group property (closure and existence of inverses): the map $U_i \mapsto U_a U_b^{-1} U_i$ is a bijection of $\mathfrak{U}$ onto itself, because multiplying on the left by $(U_a U_b^{-1})^{-1} = U_b U_a^{-1}$ recovers $U_i$.

Therefore $B\mathfrak{U}$ consists of exactly the same $N$ elements as $A\mathfrak{U}$, possibly in a different order. Thus the two cosets are identical as sets.

**Corollary (Coset Partition).** Two cosets are either disjoint or identical. Consequently, the distinct cosets of $\mathfrak{U}$ partition the group $\mathfrak{G}$.

**Corollary (Constant Coset Size).** Each coset contains exactly $N$ elements, since the map $U_i \mapsto AU_i$ is a bijection from $\mathfrak{U}$ to $A\mathfrak{U}$ (injective because $AU_i = AU_j$ implies $U_i = U_j$ by left cancellation, surjective by definition). ∎
