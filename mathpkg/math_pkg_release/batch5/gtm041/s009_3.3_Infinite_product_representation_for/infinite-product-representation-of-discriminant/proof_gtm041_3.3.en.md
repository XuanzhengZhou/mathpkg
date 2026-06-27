---
role: proof
locale: en
of_concept: infinite-product-representation-of-discriminant
source_book: gtm041
source_chapter: "3"
source_section: "3.3"
---

Let $f(\tau) = \Delta(\tau)/\eta^{24}(\tau)$. Then $f(\tau + 1) = f(\tau)$ and $f(-1/\tau) = f(\tau)$, so $f$ is invariant under every transformation in $\Gamma$. Also, $f$ is analytic and nonzero in $H$ because $\Delta$ is analytic and nonzero and $\eta$ never vanishes in $H$.

Next we examine the behavior of $f$ at $i\infty$. We have

$$\eta^{24}(\tau) = e^{2\pi i\tau} \prod_{n=1}^{\infty}(1-e^{2\pi in\tau})^{24} = x \prod_{n=1}^{\infty}(1-x^n)^{24} = x\bigl(1+I(x)\bigr),$$

where $I(x)$ denotes a power series in $x$ with integer coefficients. Thus, $\eta^{24}(\tau)$ has a first order zero at $x = 0$. By Theorem 1.19 we also have the Fourier expansion

$$\Delta(\tau) = (2\pi)^{12} \sum_{n=1}^{\infty}\tau(n)x^n = (2\pi)^{12}x\bigl(1+I(x)\bigr).$$

Thus, near $i\infty$ the function $f$ has the Fourier expansion

$$f(\tau) = \frac{\Delta(\tau)}{\eta^{24}(\tau)} = \frac{(2\pi)^{12}x(1+I(x))}{x(1+I(x))} = (2\pi)^{12}.$$

Hence $f$ is a bounded modular function, analytic on $H$ and at $i\infty$, and therefore must be constant by Liouville's theorem for modular functions. The constant is evaluated as $(2\pi)^{12}$, giving $\Delta(\tau) = (2\pi)^{12}\eta^{24}(\tau)$.
