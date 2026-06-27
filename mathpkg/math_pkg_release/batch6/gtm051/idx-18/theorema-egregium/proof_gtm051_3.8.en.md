---
role: proof
locale: en
of_concept: theorema-egregium
source_book: gtm051
source_chapter: "3"
source_section: "3.8.7"
---

$R_{1212}$ is defined in terms of $(g_{ij})$ and its first and second partials by (3.8.4). The formula for $K$ is (3.5.5). Now use (3.8.5).

In more detail: From (3.8.5), the Gauss equation relates the Riemann curvature tensor components $R_{ijkl}$ to the second fundamental form coefficients $h_{ij}$ via
$$R_{1212} = h_{11}h_{22} - h_{12}^2 = \det(h_{ij}).$$

From (3.5.5), the Gauss curvature is
$$K = \frac{\det(h_{ij})}{\det(g_{ij})}.$$

Combining these gives
$$K = \frac{R_{1212}}{\det(g_{ij})}.$$

Since $R_{1212}$ is expressed via (3.8.4) entirely in terms of the Christoffel symbols $\Gamma_{ij}^k$, which in turn depend only on the coefficients $g_{ij}$ of the first fundamental form and their first partial derivatives, the Gauss curvature is an intrinsic quantity.
