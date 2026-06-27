---
role: proof
locale: en
of_concept: trajectories-as-geodesics-of-jacobi-metric
source_book: gtm060
source_chapter: "Appendix 45"
source_section: "Maupertuis' principle of least action"
---

In this case $L = T - U$, $H = T + U$, and

$$\frac{\partial L}{\partial \dot{\mathbf{q}}} \dot{\mathbf{q}} = 2T = \left(\frac{ds}{d\tau}\right)^2 = 2(h - U).$$

Therefore, in order to guarantee a fixed value of $H = h$, the parameter $\tau$ must be chosen proportional to length:

$$d\tau = \frac{ds}{\sqrt{2(h - U)}}.$$

The reduced action integral will then be equal to

$$\int_{\gamma} \frac{\partial L}{\partial \dot{\mathbf{q}}} \dot{\mathbf{q}} \, d\tau = \int_{\gamma} \sqrt{2(h - U)} \, ds = \sqrt{2} \int_{\gamma} d\rho.$$

By Maupertuis' principle, the trajectories extremize this integral, hence they are geodesics in the metric $d\rho$.
