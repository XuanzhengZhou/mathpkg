---
role: proof
locale: en
of_concept: barycentric-subdivision-mesh-bound
source_book: gtm047
source_chapter: "5"
source_section: "5"
---

For any simplex $\sigma^n$ of $K$, the simplices of $b\sigma^n$ are formed by joins of barycenters of faces of $\sigma^n$. Each such simplex has vertices that are barycenters of a chain of faces $\sigma^{i_0} \subset \sigma^{i_1} \subset \cdots \subset \sigma^{i_k}$ of $\sigma^n$. The diameter of any such simplex is at most the maximum distance between any two such barycenters. By elementary geometry, the barycenter of a face lies within the convex hull of its vertices, and the distance between barycenters of nested faces is bounded by $\frac{1}{2}\|\sigma^n\|$, since each barycentric coordinate step halves the possible span. Therefore $\|b\sigma^n\| \leqslant \frac{1}{2}\|\sigma^n\|$.
