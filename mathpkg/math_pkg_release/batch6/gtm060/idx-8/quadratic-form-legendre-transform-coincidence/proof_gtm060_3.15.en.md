---
role: proof
locale: en
of_concept: quadratic-form-legendre-transform-coincidence
source_book: gtm060
source_chapter: "3"
source_section: "15"
---

By Euler's theorem on homogeneous functions, for a homogeneous function $f$ of degree 2, we have $(\partial f / \partial \mathbf{x})\mathbf{x} = 2f$.

By definition of the Legendre transform, $\mathbf{p} = \partial f / \partial \mathbf{x}$, and

$$g(\mathbf{p}(\mathbf{x})) = \mathbf{p}\mathbf{x} - f(\mathbf{x}) = \left(\frac{\partial f}{\partial \mathbf{x}}\right)\mathbf{x} - f(\mathbf{x}) = 2f(\mathbf{x}) - f(\mathbf{x}) = f(\mathbf{x}).$$

Thus $f(\mathbf{x}) = g(\mathbf{p})$ at corresponding points.

**Example.** For $f(x) = \frac{1}{2} m x^2$, we have $p = m x$ and

$$g(p) = \frac{p^2}{2m} = \frac{m^2 x^2}{2m} = \frac{1}{2} m x^2 = f(x).$$
