---
role: proof
locale: en
of_concept: duality-mu-pt-and-qt-f
source_book: gtm040
source_chapter: "7"
source_section: "3. Equivalence of Brownian motion and potential theory"
---

For Brownian motion in $\mathbb{R}^3$, the transition density is

$$p(t, x, y) = \frac{1}{(2\pi t)^{3/2}} e^{-|x-y|^2/2t}.$$

The transition operator $P^t$ acts on measures by

$$(\mu P^t)(dy) = \left( \int_{\mathbb{R}^3} p(t, x, y)\, d\mu(x) \right) dy,$$

so that for $f \in C_0$,

$$\int_{\mathbb{R}^3} f(y)\, d(\mu P^t)(y) = \int_{\mathbb{R}^3} \int_{\mathbb{R}^3} f(y) p(t, x, y)\, dy\, d\mu(x).$$

Define $Q^t$ on $C_0$ by

$$(Q^t f)(x) = \int_{\mathbb{R}^3} p(t, x, y) f(y)\, dy.$$

Then by the symmetry $p(t, x, y) = p(t, y, x)$ of the transition density, the right-hand side above is $\int_{\mathbb{R}^3} (Q^t f)(x)\, d\mu(x)$, establishing the duality.
