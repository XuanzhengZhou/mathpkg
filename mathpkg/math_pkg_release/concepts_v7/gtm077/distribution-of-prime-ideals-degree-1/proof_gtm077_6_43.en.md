---
role: proof
locale: en
of_concept: distribution-of-prime-ideals-degree-1
source_book: gtm077
source_chapter: "VI"
source_section: "43"
---
# Proof: Distribution of Prime Ideals of Degree 1

We analyze the logarithmic density of prime ideals of degree one in a number field $k$ of degree $n$. Let $\mathfrak{p}_f$ run through the distinct prime ideals of degree $f$ for $f = 1, 2, \ldots, n$.

From the product representation of the Dedekind zeta-function:

$$\zeta_k(s) = \prod_{\mathfrak{p}} \frac{1}{1 - N(\mathfrak{p})^{-s}} \qquad (s > 1),$$

we obtain the logarithmic form:

$$\log \zeta_k(s) = \sum_{f=1}^{n} \sum_{\mathfrak{p}_f} \left(-\log\left(1 - \frac{1}{N(\mathfrak{p}_f)^s}\right)\right).$$

**Step 1: Bounding higher-degree contributions.** For $f \geq 2$, the norm $N(\mathfrak{p}_f) = p^f \geq 4$, and since at most $n$ prime ideals of $k$ divide a given rational prime $p$, the total contribution from all $\mathfrak{p}_f$ with $f \geq 2$ is bounded by

$$n \sum_{p} \sum_{f=2}^{n} \left(-\log\left(1 - \frac{1}{p^{fs}}\right)\right) \leq n \sum_{p} \sum_{f=2}^{n} \frac{2}{p^{fs}} \leq 2n \sum_{p} \frac{1}{p^2(p^s - 1)},$$

which converges uniformly for $s \geq 1$. Hence these contributions remain bounded as $s \to 1^+$.

**Step 2: Isolating degree-one primes.** For $\mathfrak{p}_1$ (degree one prime ideals), expand the logarithm:

$$-\log\left(1 - \frac{1}{N(\mathfrak{p}_1)^s}\right) = \frac{1}{N(\mathfrak{p}_1)^s} + \varphi(\mathfrak{p}_1, s),$$

with remainder

$$0 \leq \varphi(\mathfrak{p}_1, s) = \sum_{\nu=2}^{\infty} \frac{1}{\nu N(\mathfrak{p}_1)^{\nu s}} < \frac{2}{N(\mathfrak{p}_1)^{2s}}.$$

Summing the remainder over all $\mathfrak{p}_1$:

$$0 \leq \sum_{\mathfrak{p}_1} \varphi(\mathfrak{p}_1, s) \leq 2 \sum_{\mathfrak{p}_1} \frac{1}{N(\mathfrak{p}_1)^{2s}} \leq 2n \sum_{p} \frac{1}{p^{2}} < \infty,$$

which is bounded for all $s \geq 1$.

**Step 3: Using $\zeta_k(s) \sim \frac{1}{s-1}$.** From Theorem 123, the Dedekind zeta-function has a simple pole at $s = 1$:

$$\log \zeta_k(s) = \log \frac{1}{s-1} + g(s),$$

with $g(s)$ bounded as $s \to 1^+$. Combining with Steps 1 and 2 yields

$$\sum_{\mathfrak{p}_1} \frac{1}{N(\mathfrak{p}_1)^s} = \log \frac{1}{s-1} + g_1(s),$$

where $g_1(s)$ remains bounded as $s \to 1^+$.

**Step 4: Density interpretation.** The identity above implies that the sum over degree-one prime ideals weighted by $N(\mathfrak{p}_1)^{-s}$ has the same logarithmic singularity at $s = 1$ as the sum over all prime ideals. In terms of Dirichlet density, the set of prime ideals of degree one has natural density $1$ among all prime ideals of $k$. In particular, there are infinitely many prime ideals of degree one in every number field $k$.

This result can be applied to any algebraic number field, and by choosing $k = \mathbb{Q}(\zeta_m)$, the field of $m$-th roots of unity, one obtains consequences about the distribution of rational primes in arithmetic progressions (Theorem 131).
