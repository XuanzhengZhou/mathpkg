---
role: proof
locale: en
of_concept: bertrand-classification-closed-orbits
source_book: gtm060
source_chapter: "2"
source_section: "8"
---

The result follows from a sequence of problems.

**Step 1.** The substitution $x = M/r$ transforms the orbit equation. Show that the angle $\Phi$ between pericenter and apocenter equals the semiperiod of an oscillation in the one-dimensional system with potential energy $W(x) = U(M/x) + x^2/2$:
$$\Phi = \int_{x_{\min}}^{x_{\max}} \frac{dx}{\sqrt{2(E - W)}}.$$

**Step 2.** For an orbit close to a circle of radius $r$, the angle is approximately
$$\Phi \approx \Phi_{\text{cir}} = \pi \frac{M}{r^2 \sqrt{V''(r)}} = \pi \sqrt{\frac{U'}{3U' + rU''}}.$$

**Step 3.** For $\Phi_{\text{cir}}$ to be independent of $r$, we need $U(r) = ar^\alpha$ ($\alpha \geq -2$, $\alpha \neq 0$) or $U(r) = b\log r$. Then $\Phi_{\text{cir}} = \pi/\sqrt{\alpha + 2}$. For all bounded orbits to be closed, $\Phi$ must be a rational multiple of $2\pi$ for all values of $E$ and $M$.

**Step 4.** Taking $U(r) \to \infty$ as $r \to \infty$ (so that $\alpha > 0$), one considers the limit $E \to \infty$. The substitution $x = y x_{\max}$ reduces $\Phi$ to
$$\Phi = \int_{y_{\min}}^{1} \frac{dy}{\sqrt{2(W^*(1) - W^*(y))}},$$
where $W^*(y) = y^2/2 + E^{-1}U(M/(y x_{\max}))$. As $E \to \infty$ we have $x_{\max} \to \infty$, $y_{\min} \to 0$, and $W^*(y) \to y^2/2$, giving $\Phi \to \int_0^1 dy/\sqrt{1-y^2} = \pi/2$.

Thus $\Phi_{\text{cir}} = \pi/2 = \pi/\sqrt{\alpha + 2}$, yielding $\alpha = 2$, i.e., $U = ar^2$. The case $\alpha = -1$ (i.e., $U = -k/r$) is handled separately by noting that the limit $E \to \infty$ is not applicable (the potential goes to $0$, not $\infty$), but the requirement of independence of $\Phi$ from $r$ still forces $\alpha = -1$.

Therefore the only central potentials for which all bounded orbits are closed are $U = ar^2$ (harmonic oscillator) and $U = -k/r$ (Newtonian/Coulomb).
