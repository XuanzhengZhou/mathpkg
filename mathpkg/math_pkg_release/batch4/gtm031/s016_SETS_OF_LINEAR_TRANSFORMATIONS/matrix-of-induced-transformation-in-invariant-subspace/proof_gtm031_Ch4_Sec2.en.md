---
role: proof
locale: en
of_concept: matrix-of-induced-transformation-in-invariant-subspace
source_book: gtm031
source_chapter: "IV"
source_section: "2"
---

Since $(f_1, \ldots, f_r)$ is a basis for $\mathfrak{S}$ and $\mathfrak{S}$ is invariant under $A$, for each $i = 1, \ldots, r$ we have

$$f_i A = \sum_{j=1}^{r} \beta_{ij} f_j,$$

with the coefficients for $f_{r+1}, \ldots, f_n$ being zero (which is precisely what the reduced form guarantees). Thus the $r \times r$ matrix

$$\begin{bmatrix}
\beta_{11} & \beta_{12} & \cdots & \beta_{1r} \\
\beta_{21} & \beta_{22} & \cdots & \beta_{2r} \\
\vdots & \vdots & \ddots & \vdots \\
\beta_{r1} & \beta_{r2} & \cdots & \beta_{rr}
\end{bmatrix}$$

is exactly the matrix of the restriction $A|_{\mathfrak{S}}$ relative to the basis $(f_1, \ldots, f_r)$ of $\mathfrak{S}$. This is the upper-left block $A_{11}$ appearing in the reduced form.
