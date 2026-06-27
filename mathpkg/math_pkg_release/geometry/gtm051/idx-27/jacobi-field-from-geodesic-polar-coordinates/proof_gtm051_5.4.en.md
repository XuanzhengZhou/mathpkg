---
role: proof
locale: en
of_concept: jacobi-field-from-geodesic-polar-coordinates
source_book: gtm051
source_chapter: "5"
source_section: "5.4"
---

For sufficiently small $r>0$, this is a polar coordinate system centered at $p$. We need to show that there exists $\delta>0$ and $\epsilon>0$ so that $\phi$ is defined. Notice that $\phi(t,0)$ is defined for $t\in[0,a]$; in fact, $\phi(t,0)=c(t)$. Moreover, $\phi([0,a],0)$ is compact. If $U\subset T_pM$ is the domain of definition of $\exp_p$, then $\phi([0,a],0)$ lies in $\exp_p(U)$, an open set. The existence of the required $\epsilon>0$ and $\delta>0$ now follow from the compactness of $\phi([0,a],0)$.

Let $\{e_1(t),e_2(t)\}$ be the Frenet frame along $c(t)$ with $\{e_1(0),e_2(0)\}=\{e_1(p),e_2(p)\}$. We consider the $(t,\theta)$ coordinate having coordinate basis $\{e_1(t,\theta),e_2(t,\theta)\}$. Now $Y(t)=(\partial\phi/\partial\theta)(t,0)=d\phi(e_2(t,0))$, so if we write $Y(t)=y(t)e_2(t)$, then $y(t)^2=|Y(t)|^2$. Wherever $\phi$ is a coordinate system, its first fundamental form $(g_{ij})$ must have $g_{22}(t,0)=y(t)^2$. In fact, $\phi$ will be a coordinate system in a neighborhood of any point $(t,0)$ where $y(t)\neq0$, i.e., where $Y(t)\neq0$. On such a neighborhood, we have geodesic polar coordinates and hence, by (5.3.2), geodesic coordinates. This allows us to use the formula for Gauss curvature:

$$K = \frac{-(\sqrt{g_{22}})_{11}}{g_{22}}$$

of (4.3.8), where we consider $(t,\theta)=(u^1,u^2)$ as coordinates.
