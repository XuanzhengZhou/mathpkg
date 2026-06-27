---
role: proof
locale: en
of_concept: determinant-expansion-first-order-trace
source_book: gtm060
source_chapter: "2"
source_section: "B"
---

The proof is obtained by a direct expansion of the determinant. Write $E + At = (\delta_{ij} + a_{ij}t)$. By the Leibniz formula for the determinant,

$$\det(E + At) = \sum_{\sigma \in S_n} \text{sgn}(\sigma) \prod_{i=1}^{n} (\delta_{i,\sigma(i)} + a_{i,\sigma(i)} t).$$

The product expands as a polynomial in $t$. The constant term comes from choosing $\delta_{i,\sigma(i)}$ for all $i$, which is nonzero only when $\sigma$ is the identity permutation, giving $1$. The linear term in $t$ comes from choosing $a_{i,\sigma(i)} t$ for exactly one index $i$ and $\delta_{j,\sigma(j)}$ for all $j \neq i$. For this to be nonzero, we must have $\sigma(j) = j$ for all $j \neq i$, forcing $\sigma(i) = i$ as well, so $\sigma$ is again the identity. Summing over the $n$ choices of $i$ gives $\sum_{i=1}^{n} a_{ii} t = t \, \text{tr } A$.

All remaining terms involve products of at least two factors of the form $a_{i,\sigma(i)} t$ and are therefore $O(t^2)$. Thus

$$\det(E + At) = 1 + t \, \text{tr } A + O(t^2).$$
