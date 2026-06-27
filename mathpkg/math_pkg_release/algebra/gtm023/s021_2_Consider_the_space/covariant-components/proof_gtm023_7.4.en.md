---
role: proof
locale: en
of_concept: covariant-components
source_book: gtm023
source_chapter: "7"
source_section: "4. Duality in an inner product space"
---

From the definition of \(\tau\), taking the inner product with \(e_{\mu}\),

$$\alpha_{\lambda\mu} = \langle \tau e_{\lambda}, e_{\mu} \rangle = (e_{\lambda}, e_{\mu}) = g_{\lambda\mu}.$$

Now write \(x = \sum_{\lambda} \xi^{\lambda} e_{\lambda}\) and define covariant components by \(\tau x = \sum_{\lambda} \xi_{\lambda} e^{*\lambda}\). Applying \(\langle \tau x, e_{\nu} \rangle\),

$$\xi_{\nu} = \langle \tau x, e_{\nu} \rangle = \left\langle \tau \sum_{\lambda} \xi^{\lambda} e_{\lambda}, e_{\nu} \right\rangle = \sum_{\lambda} \xi^{\lambda} \langle \tau e_{\lambda}, e_{\nu} \rangle = \sum_{\lambda} \xi^{\lambda} g_{\lambda\nu}.$$

Since \(g_{\lambda\nu} = g_{\nu\lambda}\) (symmetry of the inner product), we obtain

$$\xi_{\lambda} = \sum_{\nu} g_{\lambda\nu} \xi^{\nu}.$$

For the inner product interpretation, compute directly:

$$(x, e_{\nu}) = \left( \sum_{\lambda} \xi^{\lambda} e_{\lambda}, e_{\nu} \right) = \sum_{\lambda} \xi^{\lambda} (e_{\lambda}, e_{\nu}) = \sum_{\lambda} g_{\lambda\nu} \xi^{\lambda} = \sum_{\lambda} g_{\nu\lambda} \xi^{\lambda} = \xi_{\nu}.$$

If the basis is orthonormal, \(g_{\lambda\nu} = \delta_{\lambda\nu}\), so \(\tau e_{\lambda} = \sum_{\nu} \delta_{\lambda\nu} e^{*\nu} = e^{*\lambda}\) and \(\xi_{\lambda} = \sum_{\nu} \delta_{\lambda\nu} \xi^{\nu} = \xi^{\lambda}\).
