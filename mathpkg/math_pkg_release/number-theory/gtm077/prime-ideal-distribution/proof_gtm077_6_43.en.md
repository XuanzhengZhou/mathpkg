---
role: proof
locale: en
of_concept: prime-ideal-distribution
source_book: gtm077
source_chapter: "VI"
source_section: "43"
---
# Proof of Theorem 126: Distribution Formula for Prime Ideals of Degree 1

From Theorem 123, we obtain immediately: The Dedekind zeta-function $\zeta_k(s)$ becomes infinitely large to the first order, as $s$ approaches $1$, so that

$$\log \zeta_k(s) = \log \frac{1}{s-1} + g(s),$$

where $g(s)$ is a function which remains bounded as $s$ tends to $1$.

Let $\mathfrak{p}_f$ run through the distinct prime ideals of degree $f$ for $f = 1, 2, \ldots, n$. (Of course $\mathfrak{p}_f$ need not exist for each $f$.) From the product representation of $\zeta_k(s)$ we have, for $s > 1$,

$$\log \zeta_k(s) = \sum_{f=1}^{n} \sum_{\mathfrak{p}_f} \left(-\log\left(1 - \frac{1}{N(\mathfrak{p}_f)^s}\right)\right).$$

For prime ideals $\mathfrak{p}_f$ of degree $f \geq 2$, the norm satisfies $N(\mathfrak{p}_f) = p^f$, and the contribution of these terms to $\log \zeta_k(s)$ remains bounded as $s \to 1$, because at most $n$ such prime ideals lie above each rational prime $p$.

For the prime ideals $\mathfrak{p}_1$ of degree one, we analyze the logarithm expansion. Since $N(\mathfrak{p}_1) \geq 2$, we have for $s \geq 1$:

$$-\log\left(1 - \frac{1}{N(\mathfrak{p}_1)^s}\right) = \frac{1}{N(\mathfrak{p}_1)^s} + \varphi(\mathfrak{p}_1, s),$$

where

$$\varphi(\mathfrak{p}_1, s) = \frac{1}{2} \frac{1}{N(\mathfrak{p}_1)^{2s}} + \frac{1}{3} \frac{1}{N(\mathfrak{p}_1)^{3s}} + \cdots.$$

This remainder is bounded by a geometric series:

$$0 \leq \varphi(\mathfrak{p}_1, s) < \frac{1}{N(\mathfrak{p}_1)^{2s}} \left(1 + \frac{1}{2^s} + \frac{1}{4^s} + \cdots\right) < \frac{2}{N(\mathfrak{p}_1)^{2s}}.$$

Summing over all $\mathfrak{p}_1$ and using that at most $n$ prime ideals lie above each rational prime $p$:

$$0 \leq \sum_{\mathfrak{p}_1} \varphi(\mathfrak{p}_1, s) \leq 2 \sum_{\mathfrak{p}_1} \frac{1}{N(\mathfrak{p}_1)^{2s}} \leq 2n \sum_{p} \frac{1}{p^{2s}} \leq 2n \sum_{p} \frac{1}{p^2},$$

which is bounded for $s \geq 1$ (since $\sum_p p^{-2}$ converges).

Therefore,

$$\log \zeta_k(s) - \sum_{\mathfrak{p}_1} \frac{1}{N(\mathfrak{p}_1)^s}$$

remains bounded as $s$ tends to $1$. Combined with $\log \zeta_k(s) = \log \frac{1}{s-1} + g(s)$, we obtain

$$\sum_{\mathfrak{p}_1} \frac{1}{N(\mathfrak{p}_1)^s} = \log \frac{1}{s-1} + g_1(s),$$

where $g_1(s)$ remains bounded as $s \to 1$. This is the desired distribution formula.

As an immediate consequence, the sum over $\mathfrak{p}_1$ diverges as $s \to 1^+$, which implies that there are infinitely many prime ideals of degree one in $k$.
