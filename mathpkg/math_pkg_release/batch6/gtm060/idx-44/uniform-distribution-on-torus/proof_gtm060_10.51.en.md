---
role: proof
locale: en
of_concept: uniform-distribution-on-torus
source_book: gtm060
source_chapter: "10"
source_section: "51"
---

Apply the theorem on averages to the characteristic function $f = \chi_D$ of the measurable set $D$. Since $D$ is Jordan measurable, $f$ is Riemann integrable.

The time average gives

$$f^*(\varphi_0) = \lim_{T \to \infty} \frac{1}{T} \int_0^T \chi_D(\varphi_0 + \omega t) dt = \lim_{T \to \infty} \frac{\tau_D(T)}{T},$$

where $\tau_D(T) = \int_0^T \chi_D(\varphi(t)) dt$ is the total time the trajectory spends in $D$ up to time $T$.

The space average gives

$$\bar{f} = (2\pi)^{-n} \int_{T^n} \chi_D(\varphi) d\varphi = \frac{\operatorname{mes} D}{(2\pi)^n}.$$

By the theorem on averages, these are equal, establishing the uniform distribution property.
