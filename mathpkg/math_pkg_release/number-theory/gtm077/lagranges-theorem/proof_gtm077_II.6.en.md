---
role: proof
locale: en
of_concept: lagranges-theorem
source_book: gtm077
source_chapter: "II"
source_section: "6"
---

# Proof of Lagrange's Theorem

**Lagrange's Theorem.** In a finite group $\mathfrak{G}$ of order $h$, the order $N$ of each subgroup $\mathfrak{U}$ is a divisor of $h$. The quotient $j = h/N$ is called the *index* of $\mathfrak{U}$ in $\mathfrak{G}$.

**Proof.** Let $\mathfrak{U} = \{U_1, U_2, \ldots, U_N\}$ be the subgroup. For each $A \in \mathfrak{G}$, define the left coset

$$A\mathfrak{U} = \{AU_1, AU_2, \ldots, AU_N\}.$$

**Claim 1 (Partition).** Two cosets are either disjoint or identical.

Suppose $x \in A\mathfrak{U} \cap B\mathfrak{U}$. Then $x = AU_i = BU_j$ for some $i, j$. Hence $B = A U_i U_j^{-1}$. For any $U_k \in \mathfrak{U}$, $BU_k = A(U_i U_j^{-1} U_k) \in A\mathfrak{U}$, so $B\mathfrak{U} \subseteq A\mathfrak{U}$. Symmetrically $A\mathfrak{U} \subseteq B\mathfrak{U}$. Thus $A\mathfrak{U} = B\mathfrak{U}$.

**Claim 2 (Equal size).** $|A\mathfrak{U}| = |\mathfrak{U}| = N$.

The map $f: \mathfrak{U} \to A\mathfrak{U}$ defined by $f(U) = AU$ is bijective: it is surjective by definition and injective because $AU_i = AU_j \implies A^{-1}AU_i = A^{-1}AU_j \implies U_i = U_j$.

**Conclusion.** Let $A_1\mathfrak{U}, A_2\mathfrak{U}, \ldots, A_j\mathfrak{U}$ be the distinct cosets of $\mathfrak{U}$ in $\mathfrak{G}$. By Claim 1, they partition $\mathfrak{G}$; by Claim 2, each has $N$ elements. Therefore

$$|\mathfrak{G}| = h = \sum_{i=1}^{j} |A_i\mathfrak{U}| = j \cdot N,$$

so $N \mid h$ and the index is $j = h/N$. ∎
