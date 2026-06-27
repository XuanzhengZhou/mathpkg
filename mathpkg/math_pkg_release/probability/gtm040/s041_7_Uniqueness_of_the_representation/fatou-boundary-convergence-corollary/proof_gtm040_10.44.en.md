---
role: proof
locale: en
of_concept: fatou-boundary-convergence-corollary
source_book: gtm040
source_chapter: "10"
source_section: "7. Uniqueness of the representation"
---
By Theorem 10-43,

$$\Pr\left[\lim_{n \to \infty} h(x_n) = f(x_v)\right] = 1.$$

For $x \in \bar{S}$ with $K(\cdot, x)$ normalized, Proposition 10-35 gives

$$\Pr^{K(\cdot, x)}[x_v(\omega) = x] = 1.$$

Now, the measure $\mu$ is the harmonic measure of the original chain. For any Borel set $A \subseteq \Omega$, we have

$$\Pr[A] = \int_{S^*} \Pr^{K(\cdot, x)}[A] \, d\mu(x)$$

by the integral representation of the constant function $1$ (which is regular) and Lemma 10-39. Since $\Pr[\lim_n h(x_n) = f(x_v)] = 1$, it follows that for $\mu$-almost every $x$,

$$\Pr^{K(\cdot, x)}\left[\lim_{n \to \infty} h(x_n) = f(x_v)\right] = 1.$$

But for $\mu$-almost every $x$ for which $K(\cdot, x)$ is normalized, $x_v = x$ holds $\Pr^{K(\cdot, x)}$-almost surely by Proposition 10-35. Therefore, for $\mu$-almost every such $x$,

$$\Pr^{K(\cdot, x)}\left[\lim_{n \to \infty} h(x_n) = f(x)\right] = 1.$$
