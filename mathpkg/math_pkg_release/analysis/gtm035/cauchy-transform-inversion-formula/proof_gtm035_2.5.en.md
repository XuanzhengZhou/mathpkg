---
role: proof
locale: en
of_concept: cauchy-transform-inversion-formula
source_book: gtm035
source_chapter: "2"
source_section: "2.5"
---

# Proof of Cauchy Transform Inversion Formula

**Lemma 2.5.** Let $F \in C_0^1(\mathbb{C})$. Then

$$F(\zeta) = -\frac{1}{\pi} \int_{\mathbb{C}} \frac{\partial F}{\partial \overline{z}}(z) \frac{dx\,dy}{z - \zeta}, \qquad \text{for all } \zeta \in \mathbb{C}.$$

## Proof

Fix $\zeta \in \mathbb{C}$. Choose $R$ large enough so that $\operatorname{supp} F \subset \{z : |z| < R\}$ and $|\zeta| < R$.

For $\varepsilon > 0$ small, let $\Omega_\varepsilon = \{z : |z| < R,\; |z - \zeta| > \varepsilon\}$. By Stokes' theorem,

$$\int_{\Omega_\varepsilon} d\left( \frac{F(z)\,dz}{z - \zeta} \right) = \int_{\partial \Omega_\varepsilon} \frac{F(z)\,dz}{z - \zeta}.$$

Computing the exterior derivative:

$$d\left( \frac{F(z)\,dz}{z - \zeta} \right) = \frac{\partial F}{\partial \overline{z}} \frac{d\overline{z} \wedge dz}{z - \zeta}.$$

The boundary $\partial \Omega_\varepsilon$ consists of two components: $\{|z| = R\}$ and $\{|z - \zeta| = \varepsilon\}$ (with opposite orientation). Since $F = 0$ on $\{|z| = R\}$, the boundary integral reduces to

$$\int_{|z - \zeta| = \varepsilon} \frac{F(z)\,dz}{z - \zeta} = -\int_0^{2\pi} F(\zeta + \varepsilon e^{i\theta})\, i\,d\theta.$$

Thus

$$\int_{\Omega_\varepsilon} \frac{\partial F}{\partial \overline{z}} \frac{d\overline{z} \wedge dz}{z - \zeta} = -\int_0^{2\pi} F(\zeta + \varepsilon e^{i\theta})\, i\,d\theta.$$

Letting $\varepsilon \to 0$, the right-hand side converges to $-2\pi i\,F(\zeta)$. Using $d\overline{z} \wedge dz = 2i\,dx \wedge dy$, we obtain

$$\int_{|z| < R} \frac{\partial F}{\partial \overline{z}} \frac{2i\,dx\,dy}{z - \zeta} = -2\pi i\,F(\zeta),$$

which simplifies to

$$F(\zeta) = -\frac{1}{\pi} \int_{\mathbb{C}} \frac{\partial F}{\partial \overline{z}}(z) \frac{dx\,dy}{z - \zeta}.$$

$\square$
