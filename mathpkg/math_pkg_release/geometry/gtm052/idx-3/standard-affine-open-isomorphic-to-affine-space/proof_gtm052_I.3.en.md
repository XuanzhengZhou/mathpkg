---
role: proof
locale: en
of_concept: standard-affine-open-isomorphic-to-affine-space
source_book: gtm052
source_chapter: "I"
source_section: "3"
---

We have already shown that the map $\varphi_i: U_i \to \mathbf{A}^n$ is a homeomorphism (see Proposition 2.2), so we need only check that the regular functions are the same on any open set.

On $U_i$, the regular functions are locally quotients of homogeneous polynomials in $x_0, \ldots, x_n$ of the same degree. On $\mathbf{A}^n$, the regular functions are locally quotients of polynomials in $y_1, \ldots, y_n$. One can check easily that these two concepts are identified by the maps $\alpha$ and $\beta$ of the proof of (2.2). Concretely, a homogeneous polynomial $F(x_0, \ldots, x_n)$ of degree $d$ corresponds to the inhomogeneous polynomial $F(y_1, \ldots, y_{i-1}, 1, y_i, \ldots, y_n)$ on $\mathbf{A}^n$, and conversely any polynomial $g(y_1, \ldots, y_n)$ of degree $d$ homogenizes to $x_i^d \cdot g(x_0/x_i, \ldots, \widehat{x_i/x_i}, \ldots, x_n/x_i)$. These transformations preserve the property of being a regular function, hence the regular functions correspond under $\varphi_i$.
