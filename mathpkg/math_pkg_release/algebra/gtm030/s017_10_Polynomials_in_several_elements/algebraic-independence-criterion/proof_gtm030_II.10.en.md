---
role: proof
locale: en
of_concept: algebraic-independence-criterion
source_book: gtm030
source_chapter: "II"
source_section: "10"
---

($\Rightarrow$) Assume each $u_k$ is transcendental over $\mathfrak{A}[u_1, \cdots, u_{k-1}]$ and suppose there is a polynomial relation $\sum a_{i_1 \cdots i_r} u_1^{i_1} \cdots u_r^{i_r} = 0$. Regroup as a polynomial in $u_r$:
$$D_0 + D_1 u_r + \cdots + D_m u_r^m = 0,$$
where each $D_i$ is a polynomial in $u_1, \cdots, u_{r-1}$ with coefficients in $\mathfrak{A}$. Since $u_r$ is transcendental over $\mathfrak{A}[u_1, \cdots, u_{r-1}]$, each $D_i = 0$. By induction on $r$, this implies all coefficients are zero. Thus the $u_i$ are algebraically independent.

($\Leftarrow$) Assume $u_1, \cdots, u_r$ are algebraically independent. If there is a relation $\sum D_i u_k^i = 0$ with $D_i \in \mathfrak{A}[u_1, \cdots, u_{k-1}]$, expanding each $D_i$ as a polynomial in $u_1, \cdots, u_{k-1}$ gives a polynomial relation in $u_1, \cdots, u_k$ which, by algebraic independence, must have all coefficients zero. Hence each $D_i = 0$, showing $u_k$ is transcendental over $\mathfrak{A}[u_1, \cdots, u_{k-1}]$.
