---
role: proof
locale: en
of_concept: gauss-divergence-theorem-surface
source_book: gtm051
source_chapter: "5"
source_section: "5.6"
---

**Proof.** 

1. Without loss of generality, we may assume that $P$ lies entirely within one coordinate system. If not, subdivide $F$ into $\{F_\rho\}$, $1 \leq \rho \leq k$, so that each $P_\rho := P|_{F_\rho}$ lies inside a coordinate system. If the theorem holds for each $P_\rho$, summing yields
$$\iint_P (\operatorname{div} X) dM = \sum_\rho \iint_{P_\rho} (\operatorname{div} X) dM = \sum_\rho \int_{\partial P_\rho} i_X dM.$$
The interior edges appear twice with opposite orientations and their line integrals cancel, leaving only the boundary integral $\int_{\partial P} i_X dM$.

2. Now assume $P$ lies in a single coordinate chart $(U, (u^1, u^2))$. In local coordinates:
$$\operatorname{div} X = \frac{1}{\sqrt{g}} \sum_i \frac{\partial}{\partial u^i}(\sqrt{g} \, \xi^i), \quad dM = \sqrt{g} \, du^1 \wedge du^2,$$
and $i_X dM = -\xi^2 \sqrt{g} \, du^1 + \xi^1 \sqrt{g} \, du^2$.

Thus
$$\iint_P (\operatorname{div} X) dM = \iint_F \frac{1}{\sqrt{g}} \left(\frac{\partial}{\partial u^1}(\sqrt{g} \xi^1) + \frac{\partial}{\partial u^2}(\sqrt{g} \xi^2)\right) \sqrt{g} \, du^1 du^2$$
$$= \iint_F \left(\frac{\partial}{\partial u^1}(\sqrt{g} \xi^1) + \frac{\partial}{\partial u^2}(\sqrt{g} \xi^2)\right) du^1 du^2.$$

Now set $f_1 = -\xi^2 \sqrt{g}$, $f_2 = +\xi^1 \sqrt{g}$. Then
$$\frac{\partial f_2}{\partial u^1} - \frac{\partial f_1}{\partial u^2} = \frac{\partial}{\partial u^1}(\xi^1 \sqrt{g}) + \frac{\partial}{\partial u^2}(\xi^2 \sqrt{g}).$$

By the classical Stokes theorem for two dimensions:
$$\iint_F \left(\frac{\partial f_2}{\partial u^1} - \frac{\partial f_1}{\partial u^2}\right) du^1 du^2 = \int_{\partial F} (f_1 du^1 + f_2 du^2) = \int_{\partial F} i_X dM = \int_{\partial P} i_X dM.$$
This completes the proof. $\square$
