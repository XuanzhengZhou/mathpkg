---
role: proof
locale: en
of_concept: soliton-solution
source_book: gtm060
source_chapter: "Appendix 13"
source_section: "The Korteweg–de Vries equation"
---

Substituting the traveling wave ansatz $u(x,t) = \varphi(\xi)$ with $\xi = x - ct$ into the KdV equation $u_t = 6uu_x - u_{xxx}$:

1. $u_t = -c \varphi'(\xi)$
2. $6uu_x = 6\varphi(\xi) \varphi'(\xi) = 3(\varphi^2)'$
3. $-u_{xxx} = -\varphi'''(\xi)$

The KdV equation becomes:
$$-c\varphi' = 3(\varphi^2)' - \varphi'''.$$

Integrating once with respect to $\xi$:
$$-c\varphi = 3\varphi^2 - \varphi'' + d_0,$$
where $d_0$ is a constant of integration. Rearranging:
$$\varphi'' = 3\varphi^2 + c\varphi - d_0.$$

Let $d = -d_0$, giving:
$$\varphi'' = 3\varphi^2 + c\varphi + d.$$

This is Newton's second law for a particle of unit mass in the potential $V(\varphi) = -\varphi^3 - \frac{c}{2}\varphi^2 - d\varphi$. The force is $F(\varphi) = -V'(\varphi) = 3\varphi^2 + c\varphi + d$.

The potential $V(\varphi)$ is a cubic. For soliton solutions vanishing at infinity, we require $\varphi \to 0$ and $\varphi' \to 0$ as $\xi \to \pm\infty$. This forces $d = 0$ (since $\varphi'' \to 0$ and $\varphi \to 0$ implies $d = 0$).

With $d = 0$, the equation is $\varphi'' = 3\varphi^2 + c\varphi = \varphi(3\varphi + c)$. The fixed points are $\varphi = 0$ and $\varphi = -c/3$. For $c > 0$, the point $\varphi = 0$ is a saddle (one positive and one negative eigenvalue of the linearization) and $\varphi = -c/3$ is a center. The separatrix connecting the saddle to itself (homoclinic orbit) gives the soliton profile.

The explicit soliton solution is:
$$\varphi(\xi) = -\frac{c}{2} \operatorname{sech}^2\left(\frac{\sqrt{c}}{2}\xi\right).$$

This decays exponentially as $|\xi| \to \infty$ and represents a single localized pulse traveling to the right with speed $c > 0$.
