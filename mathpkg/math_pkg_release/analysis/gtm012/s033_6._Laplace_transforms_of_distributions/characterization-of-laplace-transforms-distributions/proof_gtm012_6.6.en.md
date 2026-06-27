---
role: proof
locale: en
of_concept: characterization-of-laplace-transforms-distributions
source_book: gtm012
source_chapter: "6"
source_section: "§6. Laplace transforms of distributions"
---

# Proof of Characterization of Laplace Transforms of Distributions

**Theorem 6.3.** Suppose $g$ is a holomorphic function in a half plane

$$\{z \mid \operatorname{Re} z > a\}.$$

Then $g$ is the Laplace transform of a distribution $F \in \mathcal{L}'$ if and only if there exist constants $K$, $k$, $M$ such that

$$|g(z)| \leq K(1 + |z|)^k e^{-M \operatorname{Re} z}, \quad \operatorname{Re} z > a.$$

*Proof.* **Necessity.** If $g = LF$ for some $F \in \mathcal{L}'$ satisfying the bound

$$|F(u)| \leq K|u|_{k,a,M}, \quad u \in \mathcal{L},$$

then by Theorem 6.2, $LF$ is holomorphic for $\operatorname{Re} z > a$. Moreover, from the definition of $LF$ and the seminorm estimate, for any $z$ with $\operatorname{Re} z > a$,

$$|g(z)| = |LF(z)| \leq K|e_z|_{k,a,M} = K|z|^k e^{aM - (\operatorname{Re} z)M} = K|z|^k e^{-M \operatorname{Re} z} \cdot e^{aM}.$$

Absorbing the constant $e^{aM}$ into $K$ and estimating $|z|^k \leq (1+|z|)^k$ gives the required bound.

**Sufficiency.** Suppose $g$ is holomorphic for $\operatorname{Re} z > a$ and satisfies

$$|g(z)| \leq K(1 + |z|)^k e^{-M \operatorname{Re} z}, \quad \operatorname{Re} z > a.$$

First consider the case $a \geq 0$. Choose $b > \max\{a, 0\}$ and define

$$h(z) = z^{-k-2} g(z), \quad \operatorname{Re} z > b.$$

Then $h$ is holomorphic for $\operatorname{Re} z > b$ and satisfies

$$|h(z)| \leq K|z|^{-k-2} (1+|z|)^k e^{-M \operatorname{Re} z} \leq K' |z|^{-2} e^{-M \operatorname{Re} z}.$$

By Theorem 5.2, there exists a continuous function $f$ such that

$$\operatorname{supp} f \subset [M, \infty), \quad |f(t)| \leq c e^{bt},$$

and $h = Lf$ (the classical Laplace transform). Let $F = D^{k+2} F_f$, where $F_f$ is the regular distribution defined by $f$. Then by Proposition 6.1 (property relating differentiation to multiplication by $z$),

$$LF(z) = z^{k+2} Lf(z) = z^{k+2} h(z) = g(z), \quad \operatorname{Re} z > b.$$

Since this holds for every $b > \max\{a, 0\}$, it holds for all $\operatorname{Re} z > a$. This completes the proof in the case $a \geq 0$.

When $a < 0$, define

$$g_1(z) = g(z + a).$$

Then $g_1$ is holomorphic for $\operatorname{Re} z > 0$ and satisfies

$$|g_1(z)| = |g(z+a)| \leq K(1 + |z+a|)^k e^{-M \operatorname{Re}(z+a)} \leq K_1 (1 + |z|)^k e^{-M \operatorname{Re} z}.$$

Applying the case $a \geq 0$ to $g_1$, there exists $F_1 \in \mathcal{L}'$ such that $g_1 = LF_1$ for $\operatorname{Re} z > 0$. Setting $F = e_{-a} F_1$, we obtain

$$LF(z) = L(e_{-a}F_1)(z) = LF_1(z+a) = g_1(z+a) = g(z), \quad \operatorname{Re} z > a.$$

This completes the proof. $\square$
