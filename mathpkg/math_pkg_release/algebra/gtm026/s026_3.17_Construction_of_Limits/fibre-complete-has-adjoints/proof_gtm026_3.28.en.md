---
role: proof
locale: en
of_concept: fibre-complete-has-adjoints
source_book: gtm026
source_chapter: "3"
source_section: "3.28"
---

The free object over $K$ is the least element $0$ of $(\mathcal{C}(K), \leqslant)$, that is, the co-optimal lift of the empty family out of $K$. The reasoning is that for any $f: K \longrightarrow L$,

$$\text{id}_K \longrightarrow (K, 0)U \longrightarrow (L, s)U \longrightarrow (L, t)U$$

the map $(K, 0) \longrightarrow (L, s)$ is admissible if and only if it is admissible preceded by every element of the empty family, and this condition is vacuously true for every $f: K \longrightarrow L$. Hence $0$ is indeed the free object on $K$, establishing the left adjoint to $U$.

Dually, the cofree object over $K$ is the greatest element $1$ of $\mathcal{C}(K)$, constructed as the optimal lift of the empty family into $K$, giving the right adjoint to $U$.
