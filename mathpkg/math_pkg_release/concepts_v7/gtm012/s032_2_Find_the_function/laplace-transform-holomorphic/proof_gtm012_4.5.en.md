---
role: proof
locale: en
of_concept: laplace-transform-holomorphic
source_book: gtm012
source_chapter: "4"
source_section: "§5"
---

# Proof of Holomorphicity and estimate of the Laplace transform

**Holomorphicity.** Let $g = Lf$ be the Laplace transform of $f$. For $z, w$ with $\operatorname{Re} z, \operatorname{Re} w \geq b > a$, we consider the difference quotient:

$$\frac{g(w) - g(z)}{w - z} = \int_{M}^{\infty} \frac{e^{-wt} - e^{-zt}}{w - z} \, f(t) \, dt = \int_{M}^{\infty} G(w, z, t) \, f(t) \, dt,$$

where
$$G(w, z, t) = \frac{e^{-wt} - e^{-zt}}{w - z}.$$

Define the auxiliary function
$$h(s) = \exp\bigl(-[(1-s)z + sw]t\bigr), \qquad 0 \leq s \leq 1.$$

Then $h(0) = e^{-zt}$ and $h(1) = e^{-wt}$, so
$$G(w, z, t) = \frac{h(1) - h(0)}{w - z}.$$

Applying the Mean Value Theorem to the real and imaginary parts of $h$, there exists $\sigma \in (0,1)$ such that
$$\frac{h(1) - h(0)}{w - z} = h'(\sigma) = -t \, e^{-[(1-\sigma)z + \sigma w]t}.$$

Therefore
$$|G(w, z, t)| = \left| -t \, e^{-[(1-\sigma)z + \sigma w]t} \right| \leq t \, e^{-t \operatorname{Re}((1-\sigma)z + \sigma w)} \leq t \, e^{-tb},$$

since $\operatorname{Re} z, \operatorname{Re} w \geq b$.

Thus for $\operatorname{Re} z > a$, the integrand $e^{-zt} f(t)$ is dominated by $K e^{t(a - \operatorname{Re} z)}$, and the difference quotient is bounded uniformly in $w$ by $t e^{-tb} |f(t)|$. By the Dominated Convergence Theorem, we may pass to the limit $w \to z$ under the integral sign, obtaining
$$g'(z) = \lim_{w \to z} \frac{g(w) - g(z)}{w - z} = \int_{M}^{\infty} (-t) e^{-zt} f(t) \, dt = -\int_{-\infty}^{\infty} e^{-zt} \, t \, f(t) \, dt.$$

Since this holds for every $z$ with $\operatorname{Re} z > a$, $g$ is holomorphic in the half-plane $\{z \mid \operatorname{Re} z > a\}$, and the derivative formula is established.

**Estimate.** Using the growth condition $|f(t)| \leq K e^{at}$ and the support condition $\operatorname{supp}(f) \subset [M, \infty)$, we compute for $\operatorname{Re} z > a$:

$$|Lf(z)| = \left| \int_{M}^{\infty} e^{-zt} f(t) \, dt \right| \leq \int_{M}^{\infty} |e^{-zt}| \, |f(t)| \, dt \leq K \int_{M}^{\infty} e^{-t \operatorname{Re} z} \, e^{at} \, dt$$
$$= K \int_{M}^{\infty} \exp\bigl(t(a - \operatorname{Re} z)\bigr) \, dt = K \, (\operatorname{Re} z - a)^{-1} \, \exp\bigl(M(a - \operatorname{Re} z)\bigr).$$

This completes the proof. $\square$
