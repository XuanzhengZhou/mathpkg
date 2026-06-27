---
role: proof
locale: en
of_concept: charged-particle-uniform-magnetic-field
source_book: gtm048
source_chapter: "3"
source_section: "3.8"
---

Abbreviate $d(u^i \circ \gamma)/du$ by $\dot{\gamma}^i$ and $d^2(u^i \circ \gamma)/du^2$ by $\ddot{\gamma}^i$. Substituting
$$g = \sum_{\mu=1}^{3} du^\mu \otimes du^\mu - du^4 \otimes du^4, \quad F = 2B_0\, du^1 \wedge du^2, \quad D_{\partial_i}\partial_j = 0$$
into the Lorentz world-force law $D_{\gamma_*}\gamma_* = e\tilde{F}\gamma_*$, we obtain by algebra:
$$\ddot{\gamma}^3 = \ddot{\gamma}^4 = 0, \qquad \ddot{\gamma}^1 = \frac{eB_0}{m}\dot{\gamma}^2, \qquad \ddot{\gamma}^2 = -\frac{eB_0}{m}\dot{\gamma}^1.$$

Define $\omega = eB_0/m$. The equations for $\gamma^1$ and $\gamma^2$ form a coupled linear system:
$$\ddot{\gamma}^1 = \omega\dot{\gamma}^2, \qquad \ddot{\gamma}^2 = -\omega\dot{\gamma}^1.$$

Integrating once gives $\dot{\gamma}^1 = \omega\gamma^2 + A$, $\dot{\gamma}^2 = -\omega\gamma^1 + B$ for constants $A, B$. Eliminating yields
$$\ddot{\gamma}^1 + \omega^2 m^2 \gamma^1 = \text{constant},$$
so the general solution in the $(1,2)$-plane is circular motion with angular frequency $\omega m$ in the affine parameter $u$.

By elementary integration, using the fact that $m \neq 0$, there exist $y \in \mathbb{R}^4$ and $a, b, c, \phi \in \mathbb{R}$ such that
$$\gamma u = y + \bigl(a\sin(\omega m u + \phi),\, a\cos(\omega m u + \phi),\, b m u,\, c m u\bigr)$$
for all $u \in \mathcal{E}$. The condition $g(\gamma_*, \gamma_*) = -m^2$ translates to
$$(\dot{\gamma}^4)^2 = m^2 + \sum_{\mu=1}^{3} \dot{\gamma}^\mu \dot{\gamma}^\mu,$$
from which we conclude $c^2 = 1 + a^2\omega^2 + b^2$.

To obtain an intuitive picture, consider $\mathcal{E} = \mathbb{R}$ and examine the world-line $\gamma\mathbb{R}$, its projection $\alpha$ into $\{(u^1, u^2, u^3, 0)\}$, and its projection $\beta$ into $\{(u^1, u^2, 0, 0)\}$. When $a = 0 = b$, the particle is at rest in the Newtonian sense; in the general case $a \neq 0 \neq b$, the particle spirals around the $u^3$-direction (the direction of the magnetic field lines, cf. Example 3.7.2). Charged particles in Earth's magnetic field spiral from pole to pole; similar motions are observed in laboratory plasmas and inferred for electrons in metals subjected to external magnetic fields.

The proper time $\Delta s$ required to go once around the circle is $\Delta s = m\Delta u = 2\pi/\omega$. The quantity $\omega = 2\pi/\Delta s$ is called the (angular) synchrotron frequency. This term also applies to high-energy particle accelerators that use magnetic fields, and to astrophysical contexts: when radio telescopes receive radio waves from a quasar, it is essentially the synchrotron frequency of charged particles moving in a magnetic field near the quasar that determines the (angular) frequency of the received radio waves. (Complicated corrections for the frequency ratio, defined in Chapter 5, are required to obtain the actual values.)
