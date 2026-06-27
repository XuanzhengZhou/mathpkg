---
role: proof
locale: en
of_concept: harmonic-conjugate-existence
source_book: gtm055
source_chapter: "3"
source_section: "Problems"
---

Since $u$ is harmonic, $\Delta u = u_{xx} + u_{yy} = 0$. Consider the complex-valued function $g = u_x - i u_y$ on $\Delta$ (writing complex coordinates $\lambda = x + iy$). The Cauchy-Riemann equations for $g$ are $u_{xx} = (-u_y)_y = -u_{yy}$ (which holds by harmonicity) and $u_{xy} = -(-u_y)_x = u_{yx}$ (which holds by equality of mixed partials). Thus $g$ is analytic on $\Delta$.

Since $\Delta$ is simply connected, $g$ has a primitive $f$ on $\Delta$ (Problem P(ii)) such that $f' = g = u_x - i u_y$. Writing $f = U + iV$, the Cauchy-Riemann equations give $U_x = u_x$ and $U_y = u_y$, so $U$ and $u$ differ by a constant. After adjusting by this constant, $u = \operatorname{Re}(f)$, and $v = \operatorname{Im}(f)$ is the harmonic conjugate.
