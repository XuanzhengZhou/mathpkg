---
role: proof
locale: en
of_concept: prop-for-every-one-dimensional-aperiodic-recurrent
source_book: gtm034
source_chapter: "7"
source_section: "015"
---

Proof: As usual (see D6.2), letting

$$\phi(\theta) = E_0[e^{i\theta x_1}] = \sum_{z \in R} P(0,x)e^{iz\theta},$$

one finds

(1) $a_n(x) + a_n(-x) = \sum_{k=0}^{n} \frac{1}{\pi} \int_{-\pi}^{\pi} [1 - \cos x\theta] \phi^k(\theta) d\theta$

$$= \frac{1}{\pi} \int_{-\pi}^{\pi} \frac{1 - \cos x\theta}{1 - \phi(\theta)} [1 - \phi^{n+1}(\theta)] d\theta.$$

Before letting $n \to \infty$ we must show that for each $x$ in $R$

$$[1 - \cos x\theta][1 - \phi(\theta)]^{-1}$$

is integrable on the interval $[-\pi,\pi]$. We have, for some $A < \infty$

$$\left| \frac{1 - \cos x\theta}{1 - \phi(\theta)} \right| \leq \frac{|1 - \cos x\theta|}{\text{Re}[1 - \phi(\theta)]} \leq A \left| \frac{1 - \cos x\theta}{\theta^

Equation (2) proved part (a) of P4. To prove part (b) decompose

(3) $$\frac{1}{x\pi} \int_{-\pi}^{\pi} \frac{1 - \cos x\theta}{1 - \phi(\theta)} d\theta = f_{\delta}(x,\theta) + g_{\delta}(x,\theta),$$

with $\delta > 0, x \neq 0$,

$$f_{\delta}(x,\theta) = \frac{1}{x\pi} \int_{-\delta}^{\delta} \frac{1 - \cos x\theta}{1 - \phi(\theta)} d\theta,$$

$$g_{\delta}(x,\theta) = \frac{1}{\pi x} \int_{\delta < |\theta| \leq \pi} \frac{1 - \cos x\theta}{1 - \phi(\theta)} d\theta.$$

Clearly

(4) $$\lim_{x \to \infty} g_{\delta}(x,\theta) = 0 \text{ for every } \delta > 0.$$

Specializing to the case when $\sigma^2 = \infty$, we choose $\delta > 0$ so small that

$$\left| \frac{\theta^2}{1 - \phi(\theta)} \right| < \epsilon \text{ for } |\theta| < \delta.$$

This can be done for arbitrary $\epsilon > 0$, since

$$|1 - \phi(\theta)| \geq \text{Re} [1 - \phi(\theta)] = 2 \sum_{x \in R} P(0,x) \sin^2 \left(\frac{x\theta}{2}\right)$$

$$\geq \frac{2\theta^2}{\pi^2} \sum_{[x] |x\theta| \leq \pi} x^2 P(0,x).$$

It follows that

(5) $$\lim_{x \to +\infty} |f_{\delta}(x,\theta)| \leq \frac{\epsilon}{\pi} \lim_{x \to +\infty} \frac{1}{x} \int_{-\delta}^{\delta} \frac{1 - \cos x\theta}{\theta^2} d\theta$$

$$= \frac
