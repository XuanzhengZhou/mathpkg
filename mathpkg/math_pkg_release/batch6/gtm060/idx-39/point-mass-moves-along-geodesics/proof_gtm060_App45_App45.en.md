---
role: proof
locale: en
of_concept: point-mass-moves-along-geodesics
source_book: gtm060
source_chapter: "Appendix 45"
source_section: "Maupertuis' principle of least action"
---

This follows directly from the Maupertuis–Jacobi principle. For inertial motion, the Lagrangian is purely kinetic: $L = T = \frac{1}{2}(ds/d\tau)^2$, with $U = 0$. Then $H = T = h$, and the reduced action becomes

$$\int_{\gamma} \frac{\partial L}{\partial \dot{q}} \dot{q} \, d\tau = \int_{\gamma} 2T \, d\tau = \int_{\gamma} \left(\frac{ds}{d\tau}\right)^2 d\tau = \int_{\gamma} \sqrt{2h} \, ds.$$

By Maupertuis' principle, the trajectory extremizes this integral, hence it is a geodesic of the Riemannian metric $ds$.
