---
role: proof
locale: en
of_concept: properties-of-characteristic-functions
source_book: gtm095
source_chapter: "2"
source_section: "12"
---

# Proof of Basic Properties of Characteristic Functions

**Properties (1) and (3).** Property (1), $|\varphi(t)| \leq \varphi(0) = 1$, follows from $|e^{itx}| = 1$ and the normalization of probability measures. Property (3), $\varphi_{-\xi}(t) = \varphi_{\xi}(-t) = \overline{\varphi_{\xi}(t)}$, follows from $e^{it(-\xi)} = e^{i(-t)\xi} = \overline{e^{it\xi}}$ under integration against the distribution. Both are evident.

**Property (2) (Uniform continuity).** For any $t, h \in R$,

$$|\varphi(t+h) - \varphi(t)| = |\mathsf{E}\, e^{it\xi}(e^{ih\xi} - 1)| \leq \mathsf{E}\, |e^{ih\xi} - 1|.$$

Since $|e^{ih\xi} - 1| \leq 2$ and $\mathsf{E}\, 2 = 2 < \infty$, the dominated convergence theorem gives $\mathsf{E}\, |e^{ih\xi} - 1| \to 0$ as $h \to 0$. The bound does not depend on $t$, establishing uniform continuity.

**Property (4) (Symmetric distribution characterization).** See the proof for the symmetric-distribution-characterization concept.

**Property (5) (Differentiability).** Consider the difference quotient

$$\frac{\varphi(t + h) - \varphi(t)}{h} = \mathsf{E}\, e^{it\xi} \left( \frac{e^{ih\xi} - 1}{h} \right).$$

Since $|(e^{ihx} - 1)/h| \leq |x|$ and $\mathsf{E}\, |\xi| < \infty$, the dominated convergence theorem implies that the limit exists:

$$\lim_{h \to 0} \mathsf{E}\, e^{it\xi} \left( \frac{e^{ih\xi} - 1}{h} \right) = \mathsf{E}\, e^{it\xi} \lim_{h \to 0} \left( \frac{e^{ih\xi} - 1}{h} \right) = i\,\mathsf{E}(\xi e^{it\xi}) = i \int_{-\infty}^{\infty} x e^{itx} dF(x).$$

Hence $\varphi'(t)$ exists and

$$\varphi'(t) = i\,\mathsf{E}(\xi e^{it\xi}) = i \int_{-\infty}^{\infty} x e^{itx} dF(x).$$

The existence of the higher-order derivatives $\varphi^{(r)}(t)$, $1 < r \leq n$, and the validity of (12), follow by induction on $r$.

Formula (13), $\mathsf{E}\, \xi^r = \varphi^{(r)}(0) / i^r$, follows immediately from (12) by setting $t = 0$.

**Proof of (14) (Taylor expansion).** For real $y$, we have

$$e^{iy} = \cos y + i \sin y = \sum_{k=0}^{n-1} \frac{(iy)^k}{k!} + \frac{(iy)^n}{n!} \left[ \cos \theta_1 y + i \sin \theta_2 y \right]$$

with $|\theta_1| \leq 1$ and $|\theta_2| \leq 1$. Replacing $y$ by $t\xi$ and taking expectations yields

$$\varphi(t) = \sum_{k=0}^{n-1} \frac{(it)^k}{k!} \mathsf{E}\, \xi^k + \frac{(it)^n}{n!} \varepsilon_n(t),$$

where

$$\varepsilon_n(t) = \mathsf{E}\left[\xi^n(\cos \theta_1(\omega)t\xi + i\sin \theta_2(\omega)t\xi - 1)\right].$$

It is clear that $|\varepsilon_n(t)| \leq 3\,\mathsf{E}\, |\xi|^n$. The dominated convergence theorem shows that $\varepsilon_n(t) \to 0$ as $t \to 0$.

**Property (6) ($\varphi^{(2n)}(0) < \infty \Rightarrow \mathsf{E}\, \xi^{2n} < \infty$).** We give a proof for $n = 1$ by induction. Suppose $\varphi''(0)$ exists and is finite. By L'H\^opital's rule and Fatou's lemma,

$$\begin{aligned}
\varphi''(0) &= \lim_{h \to 0} \frac{1}{2} \left[ \frac{\varphi'(2h) - \varphi'(0)}{2h} + \frac{\varphi'(0) - \varphi'(-2h)}{2h} \right] \\
&= \lim_{h \to 0} \frac{2\varphi'(2h) - 2\varphi'(-2h)}{8h} = \lim_{h \to 0} \frac{1}{4h^2} [\varphi(2h) - 2\varphi(0) + \varphi(-2h)] \\
&= \lim_{h \to 0} \int_{-\infty}^{\infty} \left( \frac{e^{ihx} - e^{-ihx}}{2h} \right)^2 dF(x) \\
&= -\lim_{h \to 0} \int_{-\infty}^{\infty} \left( \frac{\sin hx}{hx} \right)^2 x^2 dF(x) \\
&\leq -\int_{-\infty}^{\infty} \lim_{h \to 0} \left( \frac{\sin hx}{hx} \right)^2 x^2 dF(x) = -\int_{-\infty}^{\infty} x^2 dF(x).
\end{aligned}$$

Therefore $\int_{-\infty}^{\infty} x^2 dF(x) \leq -\varphi''(0) < \infty$, so $\mathsf{E}\, \xi^2 < \infty$. The general case follows by induction.

**Property (7) (Convergence of power series).** Let $0 < t_0 < T$. By Stirling's formula, from

$$\limsup_n \frac{(\mathsf{E}\, |\xi|^n)^{1/n}}{n} < \frac{1}{t_0}$$

we obtain

$$\limsup_n \frac{(\mathsf{E}\, |\xi|^n t_0^n)^{1/n}}{n} < 1 \quad \Longrightarrow \quad \limsup_n \left( \frac{\mathsf{E}\, |\xi|^n t_0^n}{n!} \right)^{1/n} < 1.$$

Consequently the series $\sum (\mathsf{E}\, |\xi|^n t_0^n / n!)$ converges by Cauchy's test, and the series $\sum_{r=0}^{\infty} ((it)^r/r!) \mathsf{E}\, \xi^r$ converges for $|t| \leq t_0$. By (14), for $n \geq 1$,

$$\varphi(t) = \sum_{r=0}^{n} \frac{(it)^r}{r!} \mathsf{E}\, \xi^r + R_n(t),$$

where $|R_n(t)| \leq 3(|t|^n/n!) \mathsf{E}\, |\xi|^n$. Therefore $R_n(t) \to 0$ as $n \to \infty$ for $|t| < T$, and

$$\varphi(t) = \sum_{r=0}^{\infty} \frac{(it)^r}{r!} \mathsf{E}\, \xi^r$$

for all $|t| < T$. This completes the proof.
