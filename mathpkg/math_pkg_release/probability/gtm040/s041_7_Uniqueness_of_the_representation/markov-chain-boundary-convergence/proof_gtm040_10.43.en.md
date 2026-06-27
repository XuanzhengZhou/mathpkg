---
role: proof
locale: en
of_concept: markov-chain-boundary-convergence
source_book: gtm040
source_chapter: "10"
source_section: "7. Uniqueness of the representation"
---
Define $k = \frac{1}{2} + \frac{1}{2}h$. Then $k$ is regular and normalized, with $S^{k*} = S^*$ and $B_e^k = B_e$ by Lemma 10-32. The function $h/k$ is a bounded regular function for the $k$-process with

$$\sum_i \pi_i^k \left(\frac{h_i}{k_i}\right) = \sum_i \pi_i h_i = 1,$$

and hence Lemma 10-42 applied to the $k$-process yields a function $g$ with

$$\left(\frac{h}{k}\right)_i = \int_{S} K^k(i, x) g(x) \, d\mu^k(x)$$

and

$$\Pr^k\left[\lim_{n \to \infty} \frac{h(x_n)}{k(x_n)} = g(x_v^k)\right] = 1.$$

As pointed out in the proof of Lemma 10-34, $x_v^k$ is identical with $x_v$, and also

$$\Pr^k[p] = \frac{1}{2} \Pr^1[p] + \frac{1}{2} \Pr^h[p]$$

for all cylinder sets $p$. Thus $\Pr^k[p]$ cannot be one unless both $\Pr^1[p]$ and $\Pr^h[p]$ equal one. Consequently,

$$\Pr\left[\lim_{n \to \infty} \frac{h(x_n)}{k(x_n)} = g(x_v)\right] = 1,$$

or equivalently,

$$\Pr\left[\lim_{n \to \infty} \frac{h(x_n)}{\frac{1}{2} + \frac{1}{2}h(x_n)} = g(x_v)\right] = 1.$$

Since $\{h(x_n)\}$ is a nonnegative martingale, $\lim_n h(x_n)$ exists almost everywhere $[\Pr]$ and is finite. Therefore the identity above implies that

$$\Pr\left[\lim_{n \to \infty} h(x_n) = \frac{g(x_v)}{2 - g(x_v)}\right] = 1.$$

It remains to identify $g$ as the Radon--Nikodym derivative of $\mu^h$ with respect to $\mu^k$. From Lemma 10-42 applied to the $k$-process, we have $g = d\mu^h/d\mu^k$, and thus the uniqueness part of Theorem 10-41 gives $\mu^h = g \mu^k$.

By Lemma 10-34, $\mu^k = \frac{1}{2}\mu + \frac{1}{2}\mu^h$. Hence

$$f\mu + \mu_s = \mu^h = g\mu^k = \frac{1}{2}g\mu + \frac{1}{2}g\mu^h = \frac{1}{2}g\mu + \frac{1}{2}gf\mu + \frac{1}{2}g\mu_s,$$

or

$$(2f - g - fg)\mu = (g - 2)\mu_s.$$

Since $\mu$ and $\mu_s$ are mutually singular, each side is the zero measure. For the left side, this means

$$2f - g - fg = 0 \quad \text{a.e. } [\mu],$$

or

$$f = \frac{g}{2 - g} \quad \text{a.e. } [\mu].$$

Therefore $\Pr[\lim_{n \to \infty} h(x_n) = f(x_v)] = 1$.
