---
role: proof
locale: en
of_concept: elementary-divisors-field-extension
source_book: gtm049
source_chapter: "7"
source_section: "7.5"
---

By Proposition 8 (Smith normal form over a Euclidean domain), the matrix $XI - A$ over the polynomial ring $F[X]$ can be reduced by elementary row and column operations to a diagonal form $\operatorname{diag}(d_1, \ldots, d_t)$ where each $d_i \in F[X]$ is monic and $d_1 \mid d_2 \mid \cdots \mid d_t$. The non-unit diagonal entries $d_{s+1}, \ldots, d_t$ are the invariant factors of $A$, and their ideals satisfy $[d_{s+1}] \supset \cdots \supset [d_t]$.

These invariant factors are computed using only the Euclidean algorithm in $F[X]$, which involves division of polynomials with coefficients in $F$. Since $F \subset K$ for any field extension $K$, the same computation is valid over $K[X]$. Thus the invariant factors are independent of the field containing $F$, and the minimum polynomial $d_t$ (up to a non-zero constant factor) is likewise field-independent.

For the matrix $A = \begin{pmatrix}0&1\\2&0\end{pmatrix}$:
$$XI - A = \begin{pmatrix} X & -1 \\ -2 & X \end{pmatrix}.$$
Computing the Smith normal form over $\mathbb{Q}[X]$:
$$\begin{pmatrix} X & -1 \\ -2 & X \end{pmatrix} \sim \begin{pmatrix} 1 & 0 \\ 0 & X^2-2 \end{pmatrix},$$
so the single invariant factor is $X^2 - 2$, which is the minimum polynomial and the elementary divisor over $\mathbb{Q}$.

Over $\mathbb{R}[X]$, the polynomial $X^2 - 2$ factors as $(X - \sqrt{2})(X + \sqrt{2})$, giving two elementary divisors $X - \sqrt{2}$ and $X + \sqrt{2}$ over $\mathbb{R}$.
