---
role: proof
locale: en
of_concept: orbit-closure-condition
source_book: gtm060
source_chapter: "2"
source_section: "8"
---

The total energy in the derived one-dimensional problem is conserved. Consequently, the dependence of $r$ on $t$ is defined by the quadrature

$$\dot{r} = \sqrt{2(E - V(r))}, \quad \int dt = \int \frac{dr}{\sqrt{2(E - V(r))}}.$$

Since $\dot{\phi} = M/r^2$, we have $d\phi/dr = (M/r^2)/\sqrt{2(E - V(r))}$, and the equation of the orbit in polar coordinates is found by quadrature,

$$\varphi = \int \frac{M/r^2 \, dr}{\sqrt{2(E - V(r))}}.$$

The angle between the pericenter ($r = r_{\min}$) and the apocenter ($r = r_{\max}$) is

$$\Phi = \int_{r_{\min}}^{r_{\max}} \frac{M/r^2 \, dr}{\sqrt{2(E - V(r))}}.$$

The angle between two successive pericenters is $2\Phi$. If $\Phi$ is commensurable with $2\pi$, i.e., $\Phi = 2\pi(m/n)$ for integers $m,n$, then after $n$ radial oscillations the orbit returns to its starting point and is closed. If $\Phi$ is not commensurable with $2\pi$, the successive pericenters never repeat exactly, and the orbit is everywhere dense in the annulus $r_{\min} \leq r \leq r_{\max}$.
