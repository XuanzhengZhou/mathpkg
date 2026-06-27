---
role: proof
locale: en
of_concept: integral-around-closed-curve-is-integer
source_book: gtm011
source_chapter: "4"
source_section: "4.1"
---

An easy argument using Lemma 1.19 shows that it suffices to prove this proposition under the additional assumption that $\gamma$ is smooth. In this case define $g : [0, 1] \to \mathbb{C}$ by

$$g(t) = \int_{0}^{t} \frac{\gamma'(s)}{\gamma(s) - a} \, ds.$$

Hence, $g(0) = 0$ and $g(1) = \int_{\gamma}(z - a)^{-1} dz$. We also have that

$$g'(t) = \frac{\gamma'(t)}{\gamma(t) - a} \quad \text{for} \quad 0 \leq t \leq 1.$$

But this gives

$$\frac{d}{dt} e^{-g}(\gamma - a) = e^{-g}\gamma' - g'e^{-g}(\gamma - a)$$

$$= e^{-g}\left[ \gamma' - \gamma'(\gamma - a)^{-1}(\gamma - a) \right]$$

$$= 0.$$

So $e^{-g}(\gamma - a)$ is the constant function $e^{-g(0)}(\gamma(0) - a) = \gamma(0) - a = e^{-g(1)}(\gamma(1) - a)$. Since $\gamma(0) = \gamma(1)$ we have that $e^{-g(1)} = 1$ or that $g(1) = 2\pi i k$ for some integer $k$.
