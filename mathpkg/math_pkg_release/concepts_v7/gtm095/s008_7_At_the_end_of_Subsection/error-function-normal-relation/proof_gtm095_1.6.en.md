---
role: proof
locale: en
of_concept: error-function-normal-relation
source_book: gtm095
source_chapter: "1"
source_section: "6"
---

# Proof of the Relation Between Error Function and Normal Distribution

Let $\Phi(x) = \frac{1}{\sqrt{2\pi}} \int_{-\infty}^{x} e^{-y^2/2} \, dy$ be the standard normal distribution function and let $\operatorname{erf}(x) = \frac{2}{\sqrt{\pi}} \int_{0}^{x} e^{-t^2} \, dt$ for $x > 0$ be the error function.

We establish the two identities:

**First identity:** $\Phi(x) = \frac{1}{2} \left[ 1 + \operatorname{erf}\!\left( \frac{x}{\sqrt{2}} \right) \right]$.

By symmetry of the normal density,
$$\Phi(x) = \frac{1}{\sqrt{2\pi}} \int_{-\infty}^{0} e^{-y^2/2} \, dy + \frac{1}{\sqrt{2\pi}} \int_{0}^{x} e^{-y^2/2} \, dy = \frac{1}{2} + \frac{1}{\sqrt{2\pi}} \int_{0}^{x} e^{-y^2/2} \, dy.$$

Make the substitution $t = y / \sqrt{2}$, so that $y = \sqrt{2}\, t$ and $dy = \sqrt{2}\, dt$. Then

$$\frac{1}{\sqrt{2\pi}} \int_{0}^{x} e^{-y^2/2} \, dy = \frac{1}{\sqrt{2\pi}} \int_{0}^{x/\sqrt{2}} e^{-t^2} \sqrt{2} \, dt = \frac{1}{\sqrt{\pi}} \int_{0}^{x/\sqrt{2}} e^{-t^2} \, dt = \frac{1}{2} \operatorname{erf}\!\left( \frac{x}{\sqrt{2}} \right).$$

Hence $\Phi(x) = \frac{1}{2} \left[ 1 + \operatorname{erf}\!\left( \frac{x}{\sqrt{2}} \right) \right]$.

**Second identity:** $\operatorname{erf}(x) = 2\,\Phi(\sqrt{2}\, x) - 1$.

This follows immediately from the first identity by substituting $x \mapsto \sqrt{2}\, x$:

$$\Phi(\sqrt{2}\, x) = \frac{1}{2} \left[ 1 + \operatorname{erf}(x) \right],$$

and solving for $\operatorname{erf}(x)$ yields the result.
