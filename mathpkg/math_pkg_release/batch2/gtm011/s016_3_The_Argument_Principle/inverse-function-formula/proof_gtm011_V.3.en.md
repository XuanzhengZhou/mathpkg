---
role: proof
locale: en
of_concept: inverse-function-formula
source_book: gtm011
source_chapter: "V"
source_section: "3"
---

**Proof.** Fix $\xi = f(z) \in \Omega$ with $|z - a| < R$. Since $f$ is one-one on $B(a; R)$, the equation $f(w) - \xi = 0$ has exactly one solution in $B(a; R)$, namely $w = z$. This zero is simple (because $f$ is one-one, $f'$ cannot vanish—otherwise $f$ would not be locally injective). Actually, the zero has multiplicity 1 since $f(w) - \xi$ vanishes only at $w = z$ with $f'(z) \neq 0$ (if $f'(z) = 0$, then $f$ would not be one-one in a neighborhood of $z$).

Let $\gamma$ be the circle $|w - a| = R$. Apply Theorem 3.6 (the Generalized Argument Principle) with the meromorphic function $f(w) - \xi$ and the analytic function $g(w) = w$ on a neighborhood of $\overline{B}(a; R)$. The function $f(w) - \xi$ has a single zero of multiplicity 1 at $w = z$ inside $\gamma$ and no poles. Theorem 3.6 gives

$$
\frac{1}{2\pi i} \int_{\gamma} \frac{w \, (f(w) - \xi)'}{f(w) - \xi} \, dw = g(z) \cdot 1 = z.
$$

Since $(f(w) - \xi)' = f'(w)$, we obtain

$$
z = \frac{1}{2\pi i} \int_{\gamma} \frac{w f'(w)}{f(w) - \xi} \, dw.
$$

But $z = f^{-1}(\xi)$, so substituting $\omega = \xi$ yields the desired formula

$$
f^{-1}(\omega) = \frac{1}{2\pi i} \int_{\gamma} \frac{z f'(z)}{f(z) - \omega} \, dz.
$$

This holds for every $\omega \in \Omega$. $\square$
