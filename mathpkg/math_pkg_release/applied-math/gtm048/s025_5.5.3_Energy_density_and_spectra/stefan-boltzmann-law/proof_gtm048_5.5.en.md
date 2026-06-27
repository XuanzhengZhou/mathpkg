---
role: proof
locale: en
of_concept: stefan-boltzmann-law
source_book: gtm048
source_chapter: "5"
source_section: "5.5.4"
---

Let $F_Z$ be Planck with temperature $T$. The specific intensity is $I = e^3 P(e/kT) = e^3 \cdot 2h^{-3}[(\exp(e/kT)) - 1]^{-1}$. The total energy density is obtained by integrating the specific intensity over all energies and all spatial directions. Since the Planck distribution is isotropic (independent of $U$), the integral over the celestial sphere $\mathcal{S}_Z$ contributes a factor of $4\pi$:

$$u = \int_{P_z} eF_z \pi_z = \int_{\mathcal{S}_Z} \int_0^\infty e^3 F_Z \, de \, d\zeta = 4\pi \int_0^\infty I \, de.$$

Substituting the expression for $I$:

$$u = 4\pi \int_0^\infty e^3 \cdot 2h^{-3}[(\exp(e/kT)) - 1]^{-1} \, de = 8\pi h^{-3} \int_0^\infty \frac{e^3}{[\exp(e/kT)] - 1} \, de.$$

Make the change of variable $u = e/kT$, so $e = kT u$ and $de = kT \, du$:

$$u = 8\pi h^{-3} \int_0^\infty \frac{(kT u)^3}{(\exp u) - 1} \cdot kT \, du = 8\pi h^{-3} (kT)^4 \int_0^\infty \frac{u^3}{(\exp u) - 1} \, du.$$

The dimensionless integral evaluates to $\int_0^\infty \frac{u^3}{(\exp u) - 1} \, du = \frac{\pi^4}{15}$. Therefore,

$$u = 8\pi h^{-3} (kT)^4 \cdot \frac{\pi^4}{15} = \frac{8\pi^5 k^4}{15 h^3} T^4 = a_0 T^4,$$

where $a_0 = 8\pi^5 k^4/(15h^3)$ is the blackbody constant. In geometrized units, $a_0 \cong 1.4 \times 10^{-41}$ (seconds)$^{-2}$ (Kelvin)$^{-4}$.
