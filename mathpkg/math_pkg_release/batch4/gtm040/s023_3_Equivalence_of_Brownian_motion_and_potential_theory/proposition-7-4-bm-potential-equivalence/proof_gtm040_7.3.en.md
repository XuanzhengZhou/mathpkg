---
role: proof
locale: en
of_concept: proposition-7-4-bm-potential-equivalence
source_book: gtm040
source_chapter: "7"
source_section: "3. Equivalence of Brownian motion and potential theory"
---

We may assume that $\mu \geq 0$ without loss of generality. Then

$$\int_0^T f(x,t) dt = \int_0^T \left[ \int_{R^3} \frac{1}{(2\pi t)^{3/2}} e^{-|x-y|^2/2t} d\mu(y) \right] dt.$$

By Fubini's Theorem we may interchange the order of integration. The above expression becomes

$$= \int_{R^3} \left[ \int_{0}^{T} \frac{1}{(2\pi t)^{3/2}} e^{-|x-y|^2/2t} dt \right] d\mu(y).$$

We make the change of variable on $t$ which sends $|x-y|^2/t$ into $u^2$. Specifically, let $u = |x-y|/\sqrt{t}$, so that $t = |x-y|^2/u^2$ and $dt = -2|x-y|^2/u^3\, du$. The expression becomes

$$= \int_{R^3} \left[ \int_{|x-y|/\sqrt{T}}^{\infty} \frac{2}{(2\pi)^{3/2}} |x-y|^{-1} e^{-u^2/2} du \right] d\mu(y).$$

By the Monotone Convergence Theorem,

$$\lim_{T \to \infty} \int_{0}^{T} f(x,t) dt = \int_{R^3} \left[ \int_{0}^{\infty} \frac{2}{(2\pi)^{3/2}} |x-y|^{-1} e^{-u^2/2} du \right] d\mu(y)$$

$$= \int_{R^3} \frac{1}{|x-y|} d\mu(y) \left[ \frac{1}{2\pi} \int_{-\infty}^{\infty} \frac{1}{\sqrt{2\pi}} e^{-u^2/2} du \right]$$

$$= \frac{1}{2\pi} \int_{R^3} \frac{1}{|x-y|} d\mu(y)$$

$$= g(x).$$
