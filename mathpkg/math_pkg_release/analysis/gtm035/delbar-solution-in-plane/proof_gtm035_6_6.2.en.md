---
role: proof
locale: en
of_concept: delbar-solution-in-plane
source_book: gtm035
source_chapter: "6"
source_section: "6.2"
---
# Proof of Solution to $\bar{\partial}$ in the Plane (Compact Support)

**Lemma 6.2.** Let $\phi \in C^1(\mathbb{R}^2)$ and assume that $\phi$ has compact support. Put

$$\Phi(\zeta) = -\frac{1}{\pi} \int_{\mathbb{R}^2} \phi(z) \frac{dx \, dy}{z - \zeta},$$

where $z = x + iy$. Then $\Phi \in C^1(\mathbb{R}^2)$ and

$$\frac{\partial \Phi}{\partial \bar{\zeta}}(\zeta) = \phi(\zeta), \qquad \text{for all } \zeta \in \mathbb{C}.$$

*Proof.* Choose $R > 0$ such that $\operatorname{supp} \phi \subset \{z \mid |z| \leq R\}$. Then

$$\pi \Phi(\zeta) = \int_{|z| \leq R} \phi(z) \frac{1}{\zeta - z} \, dx \, dy = \int_{|z' - \zeta| \leq R} \phi(\zeta - z') \frac{dx' \, dy'}{z'}$$

$$= \int_{\mathbb{R}^2} \phi(\zeta - z') \frac{dx' \, dy'}{z'}.$$

Since $1/z' \in L^1(dx' \, dy')$ on compact sets, it is legitimate to differentiate the last integral under the integral sign. We obtain

$$\pi \frac{\partial \Phi}{\partial \bar{\zeta}}(\zeta) = \int_{\mathbb{R}^2} \frac{\partial}{\partial \bar{\zeta}}\bigl[\phi(\zeta - z')\bigr] \frac{dx' \, dy'}{z'}$$

$$= \int_{\mathbb{R}^2} \frac{\partial \phi}{\partial \bar{\zeta}}(\zeta - z') \frac{dx' \, dy'}{z'}$$

$$= \int_{\mathbb{R}^2} \frac{\partial \phi}{\partial \bar{\zeta}}(z) \frac{dx \, dy}{\zeta - z}.$$

On the other hand, Lemma 2.5 (the Cauchy–Green formula) gives that

$$-\pi \phi(\zeta) = \int_{\mathbb{R}^2} \frac{\partial \phi}{\partial \bar{\zeta}}(z) \frac{dx \, dy}{z - \zeta}.$$

Comparing the two expressions, we conclude

$$\pi \frac{\partial \Phi}{\partial \bar{\zeta}}(\zeta) = -\bigl(-\pi \phi(\zeta)\bigr) = \pi \phi(\zeta),$$

and hence

$$\frac{\partial \Phi}{\partial \bar{\zeta}}(\zeta) = \phi(\zeta)$$

for all $\zeta \in \mathbb{C}$. $\square$

**Remark.** This lemma shows that the operator $\partial/\partial \bar{\zeta}$ admits a fundamental solution on $\mathbb{R}^2 \cong \mathbb{C}$ given by the Cauchy kernel $1/(\pi z)$. It is the one-variable version of the inhomogeneous Cauchy–Riemann equation $\bar{\partial}u = \phi$, which serves as the building block for solving the $\bar{\partial}$-equation in several complex variables.
