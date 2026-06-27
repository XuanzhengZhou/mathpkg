---
role: proof
locale: en
of_concept: generalized-cauchy-green-formula
source_book: gtm014
source_chapter: "2"
source_section: "2. The Malgrange Preparation Theorem"
---

Let $w \in D$ and choose $\varepsilon$ less than the distance from $w$ to $\gamma$. Let $D_{\varepsilon} = D \setminus (\text{disk of radius } \varepsilon \text{ about } w)$ and let $\gamma_{\varepsilon}$ be the boundary of $D_{\varepsilon}$.

Recall Green's Theorem for $\mathbb{R}^2$: if $M, N : D_{\varepsilon} \to \mathbb{R}$ are smooth and continuous on $\gamma_{\varepsilon}$, then

$$\int_{\gamma_{\varepsilon}} M \, dx + N \, dy = \iint_{D_{\varepsilon}} \left( \frac{\partial N}{\partial x} - \frac{\partial M}{\partial y} \right) dx \wedge dy.$$

The formula holds for complex-valued $M$ and $N$ by integrating the real and imaginary parts separately.

Write $F = f + ig$ and $dz = dx + i \, dy$. Applying Green's Theorem with the identity $\frac{\partial F}{\partial \bar{z}} = \frac{1}{2}\left(\frac{\partial F}{\partial x} + i\frac{\partial F}{\partial y}\right)$:

$$\int_{\gamma_{\varepsilon}} F \, dz = \int_{\gamma_{\varepsilon}} (f + ig)(dx + i \, dy) = 2i \iint_{D_{\varepsilon}} \frac{\partial F}{\partial \bar{z}} \, dx \wedge dy = -\iint_{D_{\varepsilon}} \frac{\partial F}{\partial \bar{z}} \, dz \wedge d\bar{z}.$$

Now apply this identity to the function $F(z)/(z - w)$. Since $1/(z - w)$ is holomorphic on $D_{\varepsilon}$,

$$\frac{\partial}{\partial \bar{z}} \left( \frac{F(z)}{z - w} \right) = \frac{(\partial F/\partial \bar{z})(z)}{z - w}.$$

Thus

$$\int_{\gamma_{\varepsilon}} \frac{F(z)}{z - w} \, dz = -\iint_{D_{\varepsilon}} \frac{(\partial F/\partial \bar{z})(z)}{z - w} \, dz \wedge d\bar{z}.$$

The boundary $\gamma_{\varepsilon}$ consists of $\gamma$ (traversed positively) and the circle of radius $\varepsilon$ about $w$ (traversed negatively). As $\varepsilon \to 0$, the integral over the small circle approaches $2\pi i \, F(w)$ (by the same computation as in the standard Cauchy formula), while the area integral over the disk of radius $\varepsilon$ tends to $0$. Taking the limit $\varepsilon \to 0$ yields

$$2\pi i \, F(w) = \int_{\gamma} \frac{F(z)}{z - w} \, dz + \iint_D \frac{(\partial F/\partial \bar{z})(z)}{z - w} \, dz \wedge d\bar{z},$$

which is equivalent to the stated formula. $\square$
