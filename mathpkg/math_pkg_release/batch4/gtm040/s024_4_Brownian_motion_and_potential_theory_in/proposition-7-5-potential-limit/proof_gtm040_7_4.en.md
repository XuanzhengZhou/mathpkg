---
role: proof
locale: en
of_concept: proposition-7-5-potential-limit
source_book: gtm040
source_chapter: "7"
source_section: "4. Brownian motion and potential theory in n dimensions"
---

**Proof.** We give the proof for $n = 1$; the case $n = 2$ is similar. Starting from the integral representation, for $n = 1$ we have

$$\int_0^T \frac{1}{\sqrt{2\pi t}} \int_{-\infty}^{\infty} e^{-|x-y|^2/2t} \, d\mu(y) \, dt = \int_{-\infty}^{\infty} |x-y| \left[ \int_{|x-y|/\sqrt{T}}^{\infty} \frac{2}{\sqrt{2\pi}} \, u^{-2} e^{-u^2/2} \, du \right] d\mu(y).$$

Apply integration by parts to the inner integral, differentiating $e^{-u^2/2}$ and integrating $u^{-2}$:

$$\int_{|x-y|/\sqrt{T}}^{\infty} u^{-2} e^{-u^2/2} \, du = \left[ -u^{-1} e^{-u^2/2} \right]_{|x-y|/\sqrt{T}}^{\infty} - \int_{|x-y|/\sqrt{T}}^{\infty} e^{-u^2/2} \, du.$$

Substituting back, the right side becomes

$$= -\int_{-\infty}^{\infty} |x-y| \left[ \int_{|x-y|/\sqrt{T}}^{\infty} \frac{2}{\sqrt{2\pi}} \, e^{-u^2/2} \, du \right] d\mu(y) + \frac{2}{\sqrt{2\pi}} \int_{-\infty}^{\infty} \sqrt{T} \, e^{-|x-y|^2/2T} \, d\mu(y).$$

We let $T \to \infty$ and consider each term separately.

**First term.** As $T \to \infty$, the lower limit $|x-y|/\sqrt{T} \to 0$, so the inner integral increases to $\int_0^{\infty} \frac{2}{\sqrt{2\pi}} e^{-u^2/2} du = 1$. Write the outer integral as the difference of one with respect to $\mu^+$ and one with respect to $\mu^-$. Since

$$\int_{-\infty}^{\infty} |x-y| \, d\mu^+(y) < \infty \quad \text{and} \quad \int_{-\infty}^{\infty} |x-y| \, d\mu^-(y) < \infty \quad \text{a.e.},$$

the Dominated Convergence Theorem implies that the first term tends a.e. to

$$-\int_{-\infty}^{\infty} |x-y| \, d\mu(y) = g(x),$$

where $g(x)$ is the potential in dimension $1$.

**Second term.** We show that if $\mu(\mathbb{R}^1) = 0$, then

$$\int_{-\infty}^{\infty} \sqrt{T} \, e^{-|x-y|^2/2T} \, d\mu(y) \to 0 \quad \text{a.e. as } T \to \infty.$$

Since $\mu(\mathbb{R}^1) = 0$, we have

$$\int_{-\infty}^{\infty} \sqrt{T} \, e^{-|x-y|^2/2T} \, d\mu(y) = \int_{-\infty}^{\infty} \sqrt{T} \bigl(e^{-|x-y|^2/2T} - 1\bigr) \, d\mu(y).$$

We prove that the right side tends to zero when $\mu$ is replaced by $\mu^+$ or $\mu^-$. Consider $\mu^+$. First we establish the pointwise bound

$$\bigl|\sqrt{T}(e^{-|z|^2/2T} - 1)\bigr| \leq k|z|$$

for a fixed constant $k$ and for all $T$. By differential calculus, the function

$$\frac{e^{-|z|^2/2T} - 1}{|z|}$$

attains its maximum as a function of $|z|$ when $|z|$ satisfies

$$\frac{|z|^2}{T} = e^{|z|^2/2T} - 1.$$

The unique positive solution occurs for $2 \leq |z|^2/T \leq 3$. Let $b = |z|^2/T$ with $2 \leq b \leq 3$ be the point at which the maximum occurs. Then

$$\left| \sqrt{T} \, \frac{e^{-|z|^2/2T} - 1}{|z|} \right| \leq \left| \sqrt{T} \, \frac{e^{-b/2} - 1}{\sqrt{bT}} \right| = \frac{1 - e^{-b/2}}{\sqrt{b}} = k,$$

so indeed $|\sqrt{T}(e^{-|z|^2/2T} - 1)| \leq k|z|$. Setting $|z| = |x-y|$, the integrand is bounded by $k|x-y|$, which is integrable with respect to $\mu^+$ by hypothesis. Moreover, for each fixed $y$, $e^{-|x-y|^2/2T} - 1 \to 0$ as $T \to \infty$, so the Dominated Convergence Theorem yields

$$\int_{-\infty}^{\infty} \sqrt{T} \bigl(e^{-|x-y|^2/2T} - 1\bigr) \, d\mu^+(y) \to 0.$$

The same argument applies to $\mu^-$.

**Conclusion.** If $\mu(\mathbb{R}^1) = 0$, then both terms of the decomposition converge, and the whole expression tends to $g(x)$ a.e. If $\mu(\mathbb{R}^1) \neq 0$, the first term still converges, but the second term behaves like $\sqrt{T} \, \mu(\mathbb{R}^1)$ (since $e^{-|x-y|^2/2T} \to 1$ pointwise), and therefore diverges to $+\infty$ or $-\infty$ a.e. according as $\mu(\mathbb{R}^1) > 0$ or $\mu(\mathbb{R}^1) < 0$. This completes the proof for $n = 1$. The proof for $n = 2$ follows by a similar argument with the logarithmic kernel.
