---
role: exercise
locale: en
chapter: "2"
section: "Supplement: Kepler Problem"
exercise_number: 6
---

Find all central fields in which bounded orbits exist and are all closed.

*Answer:* $U = ar^2$ (harmonic oscillator) or $U = -k/r$ (Newtonian/Coulomb potential).

*Solution outline.* If all bounded orbits are closed, then in particular the circular orbit angular period $\Phi_{\text{cir}}$ must be a rational multiple of $2\pi$: $\Phi_{\text{cir}} = 2\pi(m/n)$. According to Problem 3, the admissible power-law potentials are $U = ar^\alpha$ (with $\alpha \geq -2$) or $U = b \ln r$ (corresponding to $\alpha = 0$). In all these cases $\Phi_{\text{cir}} = \pi/\sqrt{\alpha + 2}$.

- If $\alpha > 0$, then $\lim_{E \to \infty} \Phi(E, M) = \pi/2$ (Problem 4), forcing $\Phi_{\text{cir}} = \pi/2$ and therefore $\alpha = 2$, i.e., $U = ar^2$.
- If $\alpha < 0$, then $\lim_{E \to -0} \Phi(E, M) = \pi/(2 + \alpha)$ (Problem 5). Equating $\pi/(2 + \alpha) = \pi/\sqrt{2 + \alpha}$ yields $\alpha = -1$, i.e., $U = -k/r$.
- If $\alpha = 0$ (logarithmic potential), $\Phi_{\text{cir}} = \pi/\sqrt{2}$, which is not commensurable with $2\pi$, so no closed bounded orbits exist in this case.

Thus, the only central fields in which all bounded orbits are closed are $U = ar^2$ ($a > 0$) and $U = -k/r$. In the field $U = ar^2$, all orbits are ellipses with center at the origin. In the field $U = -k/r$, all bounded orbits are ellipses with the origin at one focus (Kepler's first law).
