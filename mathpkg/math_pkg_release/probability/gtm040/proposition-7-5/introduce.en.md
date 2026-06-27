---
role: introduce
locale: en
content_hash: ""
written_against: ""
---

In $R^n$ for $n = 1$ or 2, let $\mu = \mu^+ - \mu^-$ be the difference of two finite measures, and suppose that

$$\int_{R^1} |x - y| d\mu^+ (y) < \infty \quad \text{and} \quad \int_{R^1} |x - y| d\mu^- (y) < \infty \quad \text{a.e. if } n = 1$$

or

$$\int_{R^2} |\log |x - y|| d\mu^+ (y) < \infty \quad \text{and} \quad \int_{R^2} |\log |x - y|| d\mu^- (y) < \infty$$

a.e. if $n = 2$.

If $\mu(R^n) \neq 0$, then

$$\lim_{T \to \infty} \int_0^T \frac{1}{(2\pi t)^{n/2}} \int_{R^n} e^{-|x - y|^2/2t} d\mu(y) dt = +\infty \quad \text{or} \quad -\infty \quad \text{a.e

proof of Proposition 7-4 shows that for $n = 1$

$$\int_0^T \frac{1}{\sqrt{2\pi t}} \int_{-\infty}^{\infty} e^{-|x-y|^2/2t} d\mu(y) dt$$

$$= \int_{-\infty}^{\infty} |x-y| \left[ \int_{|x-y|/\sqrt{T}}^{\infty} \frac{2}{\sqrt{2\pi}} u^{-2} e^{-u^2/2} du \right] d\mu(y).$$

If we use integration by parts on the terms in the brackets, differentiating the exponential and integrating $u^{-2}$, we find that the right side is

$$= \int_{-\infty}^{\infty} |x-y| \frac{2}{\sqrt{2\pi}} \left[ -u^{-1} e^{-u^2/2} \left| \int_{|x-y|/\sqrt{T}}^{\infty} - \int_{|x-y|/\sqrt{T}}^{\infty} e^{-u^2/2} du \right| d\mu(y) \right]$$

$$= -\int_{-\infty}^{\infty} |x-y| \left[ \int_{|x-y|/\sqrt{T}}^{\infty} \frac{2}{\sqrt{2\pi}} e^{-u^2/2} du \right] d\mu(y)$$

$$+ \frac{2}{\sqrt{2\pi}} \int_{-\infty}^{\infty} \sqrt{T} e^{-|x-y|^2/2T} d\mu(y).$$

We let $T$ tend to $\infty$ and consider each term separately. In the first term the expression in brackets increases to 1. If we write the integral as the difference of one with respect to $\mu^+$ and one with respect to $\mu^-$ and use the fact that

$$\int_{-\infty}^{\infty} |x-y| d\mu^+ (y) < \infty \quad \text{and} \quad \int_{-\infty}^{\infty} |x-y| d\mu^- (y) < \infty \quad \text{a.e.},$$

we see by the Dominated Convergence Theorem that the first term tends a

To complete the proof we shall show that if $\mu(R^1) = 0$, then

$$\int_{-\infty}^{\infty} \sqrt{T} e^{-|x-y|^2/2T} d\mu(y)$$

tends to zero a.e. as $T \to \infty$. Since $\mu(R^1) = 0$, we have

$$\int_{-\infty}^{\infty} \sqrt{T} e^{-|x-y|^2/2T} d\mu(y) = \int_{-\infty}^{\infty} \sqrt{T} (e^{-|x-y|^2/2T} - 1) d\mu(y).$$

We shall prove that the right side even tends to zero when $\mu$ is replaced by $\mu^+$ or $\mu^-$. Let us do so for $\mu^+$. First we show that

$$|\sqrt{T}(e^{-|z|^2/2T} - 1)| \leq k|z|$$

for a fixed constant $k$ and for all $T$. By differential calculus methods, we find that

$$\frac{e^{-|z|^2/2T} - 1}{|z|}$$

assumes its maximum value as a function of $|z|$ when $|z|$ satisfies

$$\frac{|z|^2}{T} = e^{|z|^2/2T} - 1.$$

The unique positive solution occurs for $2 \leq |z|^2/T \leq 3$. Let $b = |z|^2/T$ with $2 \leq b \leq 3$ be the point at which the solution occurs. Then

$$\left| \sqrt{T} \frac{e^{-|z|^2/2T} - 1}{|z|} \right| \leq \left| \sqrt{T} \frac{e^{-b/2} - 1}{\sqrt{bT}} \right| = \frac{1 - e^{-b/2}}{\sqrt{b}} = k$$

and

$$|\sqrt{T}(e^{-|z|^2/2T} - 1)| \leq k|z|.$$

Put $|z| = |x-y|$. Since
