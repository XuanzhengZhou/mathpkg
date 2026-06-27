---
role: proof
locale: en
of_concept: delbar-squared-zero
source_book: gtm035
source_chapter: "Chapter 5"
source_section: "5.3"
---
# Proof of $\bar{\partial}^2 = 0$, $\partial^2 = 0$, and $\partial\bar{\partial} + \bar{\partial}\partial = 0$

Recall that the exterior derivative splits as $d = \partial + \bar{\partial}$ on $\wedge^{p,q}(\Omega)$ (equation (2) of Section 5). Moreover, by Lemma 4.8, the exterior derivative satisfies $d^2 = 0$ on forms of all degrees. Hence

$$0 = d^2 = (\partial + \bar{\partial})^2 = \partial^2 + \partial\bar{\partial} + \bar{\partial}\partial + \bar{\partial}^2.$$

Now examine the bidegrees of each term. For $\omega \in \wedge^{p,q}(\Omega)$:

- $\partial\omega \in \wedge^{p+1,q}(\Omega)$, so $\partial^2\omega \in \wedge^{p+2,q}(\Omega)$ (bidegree $(2,0)$ component).
- $\bar{\partial}\omega \in \wedge^{p,q+1}(\Omega)$, so $\bar{\partial}^2\omega \in \wedge^{p,q+2}(\Omega)$ (bidegree $(0,2)$ component).
- $\partial\bar{\partial}\omega \in \wedge^{p+1,q+1}(\Omega)$ and $\bar{\partial}\partial\omega \in \wedge^{p+1,q+1}(\Omega)$, so $\partial\bar{\partial} + \bar{\partial}\partial$ maps into $\wedge^{p+1,q+1}(\Omega)$ (bidegree $(1,1)$ component).

Since the subspaces $\wedge^{p+2,q}$, $\wedge^{p,q+2}$, and $\wedge^{p+1,q+1}$ are linearly independent (they are distinct bihomogeneous components of the exterior algebra), the equation $\partial^2 + (\partial\bar{\partial} + \bar{\partial}\partial) + \bar{\partial}^2 = 0$ implies that each component must vanish identically. Therefore

$$\bar{\partial}^2 = 0, \qquad \partial^2 = 0, \qquad \partial\bar{\partial} + \bar{\partial}\partial = 0.$$

---

**Alternative direct computation for $\bar{\partial}^2f = 0$ on functions.** For $f \in C^\infty(\Omega)$,

$$\bar{\partial}f = \sum_{j=1}^{n} \frac{\partial f}{\partial \bar{z}_j} \, d\bar{z}_j.$$

Applying $\bar{\partial}$ again:

$$\bar{\partial}^2 f = \bar{\partial}\!\left( \sum_{j=1}^{n} \frac{\partial f}{\partial \bar{z}_j} \, d\bar{z}_j \right)
= \sum_{j,k=1}^{n} \frac{\partial^2 f}{\partial z_k \partial \bar{z}_j} \, dz_k \wedge d\bar{z}_j
+ \sum_{j,k=1}^{n} \frac{\partial^2 f}{\partial \bar{z}_k \partial \bar{z}_j} \, d\bar{z}_k \wedge d\bar{z}_j.$$

In the second sum, the mixed partials of a $C^\infty$ function satisfy $\frac{\partial^2 f}{\partial \bar{z}_k \partial \bar{z}_j} = \frac{\partial^2 f}{\partial \bar{z}_j \partial \bar{z}_k}$, while $d\bar{z}_k \wedge d\bar{z}_j = -d\bar{z}_j \wedge d\bar{z}_k$. Hence terms with $k \neq j$ cancel in pairs, and the $k = j$ terms vanish because $d\bar{z}_j \wedge d\bar{z}_j = 0$.

In the first sum, $\frac{\partial^2 f}{\partial z_k \partial \bar{z}_j} = \frac{\partial^2 f}{\partial \bar{z}_j \partial z_k}$ by equality of mixed partials. When we expand $\bar{\partial}\partial f$ we obtain the same terms with opposite signs, confirming $\bar{\partial}\partial + \partial\bar{\partial} = 0$. The computation for $\partial^2 = 0$ is analogous.

The result extends from functions to forms of arbitrary bidegree by linearity and the definitions of $\partial$ and $\bar{\partial}$ on $\wedge^{p,q}(\Omega)$.
