---
role: proof
locale: en
of_concept: homogeneity-of-eisenstein-invariants
source_book: gtm041
source_chapter: "1"
source_section: "1.11"
---

For any $\lambda \neq 0$, the scaled lattice $\lambda\Omega = \{\lambda\omega : \omega \in \Omega\}$ has periods $(\lambda\omega_1, \lambda\omega_2)$. By definition,
$$G_n(\lambda\omega_1, \lambda\omega_2) = \sum_{\omega \in \Omega, \omega \neq 0} \frac{1}{(\lambda\omega)^n} = \lambda^{-n} \sum_{\omega \neq 0} \frac{1}{\omega^n} = \lambda^{-n} G_n(\omega_1, \omega_2).$$

Since $g_2 = 60 G_4$, we have
$$g_2(\lambda\omega_1, \lambda\omega_2) = 60 G_4(\lambda\omega_1, \lambda\omega_2) = 60 \lambda^{-4} G_4(\omega_1, \omega_2) = \lambda^{-4} g_2(\omega_1, \omega_2).$$

Similarly, $g_3 = 140 G_6$ gives
$$g_3(\lambda\omega_1, \lambda\omega_2) = 140 G_6(\lambda\omega_1, \lambda\omega_2) = 140 \lambda^{-6} G_6(\omega_1, \omega_2) = \lambda^{-6} g_3(\omega_1, \omega_2).$$

For the discriminant $\Delta = g_2^3 - 27 g_3^2$, we obtain
$$\Delta(\lambda\omega_1, \lambda\omega_2) = (\lambda^{-4} g_2)^3 - 27(\lambda^{-6} g_3)^2 = \lambda^{-12}(g_2^3 - 27 g_3^2) = \lambda^{-12} \Delta(\omega_1, \omega_2).$$

Thus $g_2$, $g_3$, and $\Delta$ are homogeneous of degrees $-4$, $-6$, and $-12$, respectively.
