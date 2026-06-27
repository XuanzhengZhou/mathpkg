---
role: proof
locale: en
of_concept: generalized-cauchy-integral-formula
source_book: gtm014
source_chapter: "IV"
source_section: "2"
---

Let $w \in D$ and choose $\varepsilon$ less than the distance from $w$ to $\gamma$. Let $D_{\varepsilon} = D \setminus (\text{disk of radius }\varepsilon \text{ about } w)$ and let $\gamma_{\varepsilon}$ be the boundary of $D_{\varepsilon}$.

Recall Green's Theorem for $\mathbf{R}^2$: for smooth $M, N: \overline{D_{\varepsilon}} \to \mathbf{R}$,
$$\int_{\gamma_{\varepsilon}} M \, dx + N \, dy = \iint_{D_{\varepsilon}} \left( \frac{\partial N}{\partial x} - \frac{\partial M}{\partial y} \right) dx \wedge dy.$$
The formula also holds for complex-valued $M, N$.

Write $F = f + ig$. Apply Green's Theorem with $M = f + ig$ and $N = i(f + ig)$:
$$\int_{\gamma_{\varepsilon}} F \, dz = \int_{\gamma_{\varepsilon}} (f + ig)(dx + i \, dy) = 2i \iint_{D_{\varepsilon}} \frac{\partial F}{\partial \bar{z}} \, dx \wedge dy = -\iint_{D_{\varepsilon}} \frac{\partial F}{\partial \bar{z}} \, dz \wedge d\bar{z}.$$

Now apply this to $F(z)/(z - w)$ on $D_{\varepsilon}$. Since $1/(z - w)$ is holomorphic on $D_{\varepsilon}$,
$$\frac{\partial}{\partial \bar{z}} \left( \frac{F(z)}{z - w} \right) = \frac{\partial F / \partial \bar{z}}{z - w}.$$

Thus
$$\int_{\gamma_{\varepsilon}} \frac{F(z)}{z - w} \, dz = -\iint_{D_{\varepsilon}} \frac{\partial F / \partial \bar{z}}{z - w} \, dz \wedge d\bar{z}.$$

The boundary $\gamma_{\varepsilon}$ consists of $\gamma$ (positively oriented) and the circle of radius $\varepsilon$ about $w$ (negatively oriented). Letting $\varepsilon \to 0$, the integral over the small circle approaches $2\pi i \, F(w)$ (by continuity of $F$), while the area integral converges to the integral over $D$. This yields the stated formula.
