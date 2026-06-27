---
role: proof
locale: en
of_concept: triangular-property-of-orthonormal-basis
source_book: gtm031
source_chapter: "VI"
source_section: "1"
---

In the Gram-Schmidt construction, the induction hypothesis includes $[u_1, \ldots, u_i] = [e_1, \ldots, e_i]$ for all $i \leq k$. At step $k+1$, the vector $f_{k+1}$ is defined as

$$f_{k+1} = e_{k+1} - \sum_{i=1}^{k} (e_{k+1}, u_i) u_i,$$

and $u_{k+1}$ is a scalar multiple of $f_{k+1}$. Since each $u_i$ for $i \leq k$ lies in $[e_1, \ldots, e_i] \subseteq [e_1, \ldots, e_k]$, the correction term $\sum_{i=1}^{k} (e_{k+1}, u_i) u_i$ lies in $[e_1, \ldots, e_k]$. Therefore $f_{k+1}$ and hence $u_{k+1}$ are linear combinations of $e_1, \ldots, e_{k+1}$.

By induction, for each $i$, $u_i$ is a linear combination of $e_1, \ldots, e_i$. Thus the expansion coefficients $\tau_{ij}$ satisfy $\tau_{ij} = 0$ whenever $j > i$, meaning the matrix $(\tau)$ is lower triangular.
