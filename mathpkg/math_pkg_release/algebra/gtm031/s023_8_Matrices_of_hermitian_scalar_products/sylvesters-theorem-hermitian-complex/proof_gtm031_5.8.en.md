---
role: proof
locale: en
of_concept: sylvesters-theorem-hermitian-complex
source_book: gtm031
source_chapter: "5"
source_section: "8"
---

Let $\Phi$ be the field of complex numbers with $\alpha \mapsto \bar{\alpha}$ the usual complex conjugation. For a hermitian scalar product $g(x, y)$, we have $g(u, u) = \overline{g(u, u)}$, so $g(u, u) \in \mathbb{R}$ for every $u$. By Theorem 3, there exists a basis $(u_1, \cdots, u_n)$ such that $g(u_i, u_i) = \beta_i \in \mathbb{R}$ and $g(u_i, u_j) = 0$ for $i \neq j$. Replacing $u_i$ by $v_i = \gamma_i u_i$ ($\gamma_i \neq 0$) transforms $\beta_i$ into $\gamma_i \bar{\gamma}_i \beta_i = |\gamma_i|^2 \beta_i$, which has the same sign as $\beta_i$.

Arrange the basis so that $\beta_i > 0$ for $i = 1, \cdots, p$, $\beta_j < 0$ for $j = p+1, \cdots, r$, and $\beta_k = 0$ for $k = r+1, \cdots, n$. For $i \leq p$, set $\gamma_i = \beta_i^{-1/2}$; for $p < j \leq r$, set $\gamma_j = (-\beta_j)^{-1/2}$. This yields the canonical form

$$\operatorname{diag}\{1, \cdots, 1, -1, \cdots, -1, 0, \cdots, 0\}.$$

The proof that $p$ is an invariant follows exactly the same dimension-counting argument as in Theorem 5. Define $\mathfrak{R}_+ = [u_1, \cdots, u_p]$, $\mathfrak{S}_- = [v_{p'+1}, \cdots, v_r]$, and let $\mathfrak{R}^\perp$ be the radical. For $y \in \mathfrak{R}_+ + \mathfrak{R}^\perp$,

$$g(y, y) = \sum_{i=1}^{p} |\eta_i|^2 \beta_i \geq 0,$$

with equality only if all $\eta_i = 0$. For $y \in \mathfrak{S}_- + \mathfrak{R}^\perp$, $g(y, y) \leq 0$ with equality only if $y \in \mathfrak{R}^\perp$. The intersection argument yields $p \leq p'$ and symmetrically $p' \leq p$, so $p = p'$. Hence the number of positive diagonal entries is an invariant of the hermitian cogredience class.
