---
role: proof
locale: en
of_concept: inverse-function-theorem-holomorphic
source_book: gtm012
source_chapter: "4"
source_section: "4. The local behavior of a holomorphic function"
---

# Proof of Inverse Function Theorem for Holomorphic Functions

**Theorem 4.2.** Suppose $f$ is holomorphic in an open set $\Omega$, and suppose $z_0 \in \Omega$ and $f'(z_0) \neq 0$. Let $w_0 = f(z_0)$. Then there exist $\delta > 0$ and $\varepsilon > 0$ such that for each $w_1$ with $|w_1 - w_0| < \varepsilon$ there is a unique $z_1$ with $|z_1 - z_0| < \delta$ such that $f(z_1) = w_1$. Moreover, the function $g$ defined by $g(w_1) = z_1$ is holomorphic on $|w - w_0| < \varepsilon$.

*Proof.* By Lemma 4.1, near $z_0$ we may write

$$f(z) = w_0 + (z - z_0)h(z)$$

where $h$ is holomorphic in $\Omega$ and $h(z_0) = f'(z_0) \neq 0$ (here $m = 1$ since $f'(z_0) \neq 0$). Choose $\delta > 0$ so small that the closed disc $|z - z_0| \leq \delta$ is contained in $\Omega$ and $|h(z)| \geq \frac{1}{2}|h(z_0)|$ for all $z$ in this disc. Let $C$ be the circle of radius $\delta$ around $z_0$. Then $f(z) \neq w_0$ if $z \in C$.

Since $C$ is compact and $f$ is continuous, we may choose $\varepsilon > 0$ so that

$$f(z) \neq w_1 \quad \text{if } |w_1 - w_0| < \varepsilon \text{ and } z \in C.$$

Now define, for $|w_1 - w_0| < \varepsilon$,

$$g(w_1) = \frac{1}{2\pi i} \int_C z f'(z) [f(z) - w_1]^{-1} \, dz.$$

This function is holomorphic on the disc $|w_1 - w_0| < \varepsilon$; indeed it may be differentiated under the integral sign.

We claim that $g$ is the inverse of $f$ near $z_0$. Suppose $|z_1 - z_0| < \delta$, $f(z_1) = w_1$, and $|w_1 - w_0| < \varepsilon$. We may assume $\delta$ is chosen so small that $f'(z) \neq 0$ for $|z - z_0| < \delta$. Then by the Cauchy integral formula applied to the identity function $\mathrm{id}(z) = z$ and the function $f(z) - w_1$ (which has a single simple zero at $z_1$ inside $C$), we find

$$g(w_1) = z_1.$$

Thus $g$ is a holomorphic inverse to $f$ on a neighborhood of $z_0$. In particular, $f$ is one-to-one near $z_0$ and $g(f(z)) = z$ for $z$ near $z_0$.

To verify that $f(g(w)) = w$ for $w$ near $w_0$, note that by choosing $\varepsilon$ sufficiently small, we may ensure that $|f(g(w)) - w_0| < \varepsilon$ whenever $|w - w_0| < \varepsilon$. Then for such $w$,

$$g(f(g(w))) = g(w)$$

since $g$ is a left inverse. Because $g$ is one-to-one on a sufficiently small neighborhood of $w_0$, this implies $f(g(w)) = w$. $\square$
