---
role: proof
locale: en
of_concept: jacobi-equation-newton-form
source_book: gtm060
source_chapter: "Appendix 1"
source_section: "I"
---
Decompose the variation vector $\xi$ into components parallel and perpendicular to the velocity vector $v$. Since $\Omega(v,v) = 0$ and $\Omega(v,\xi)$ is skew-symmetric, the parallel component satisfies $\frac{D^2\xi}{Dt^2} = 0$. For the normal component, the Jacobi equation $\frac{D^2\xi}{Dt^2} = -\Omega(v,\xi)v$ holds. Define $U(\xi) = \frac{1}{2}\langle \Omega(v,\xi)v, \xi \rangle$. Then $\operatorname{grad} U$ (with respect to $\xi$) equals $\Omega(v,\xi)v$, since for any variation $\delta\xi$, we have $\langle \operatorname{grad} U, \delta\xi \rangle = \frac{d}{d\varepsilon}U(\xi+\varepsilon\delta\xi)|_{\varepsilon=0} = \langle \Omega(v,\xi)v, \delta\xi \rangle$. Using the sectional curvature formula $K = \langle \Omega(\xi,v)\xi, v \rangle / (|\xi|^2|v|^2)$ for orthonormal directions, we obtain $U = \frac{1}{2}K|\xi|^2|v|^2$.
