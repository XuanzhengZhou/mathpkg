---
role: proof
locale: en
of_concept: existence-of-distribution-solution-to-pde
source_book: gtm012
source_chapter: "7"
source_section: "Differential equations"
---

# Proof of Existence and Uniqueness of Distribution Solutions to Polynomial Differential Equations

**Theorem 7.1.** Suppose $p$ is a polynomial of degree $n > 0$, and suppose $H \in \mathcal{L}'$. Then there is a unique distribution $F \in \mathcal{L}'$ such that

$$p(D)F = H.$$

**Proof.** Distributions in $\mathcal{L}'$ are uniquely determined by their Laplace transforms (Theorem 6.3). Therefore $p(D)F = H$ is equivalent to

$$L(p(D)F)(z) = LH(z), \qquad \operatorname{Re} z > a$$

for some $a \in \mathbb{R}$. But

$$L(p(D)F)(z) = p(z) LF(z).$$

We may choose $a$ so large that $p(z) \neq 0$ if $\operatorname{Re} z \geq a$, and so that $LH$ is holomorphic for $\operatorname{Re} z > a$ and satisfies the estimate given in Theorem 6.3. Then we may define

$$g(z) = p(z)^{-1} LH(z), \qquad \operatorname{Re} z > a.$$

Then $g$ is holomorphic. Since $|p(z)^{-1}|$ is bounded for $\operatorname{Re} z \geq a$, the function $g$ satisfies the same type of estimate as $LH$, i.e., there exist constants $K$, $k$, $M$ such that

$$|g(z)| \leq K(1 + |z|)^k \exp(-M \operatorname{Re} z), \qquad \operatorname{Re} z > a.$$

By Theorem 6.3 there is a unique distribution $F \in \mathcal{L}'$ such that $LF = g$. Then

$$L(p(D)F)(z) = p(z) LF(z) = p(z) g(z) = LH(z), \qquad \operatorname{Re} z > a,$$

which implies $p(D)F = H$. The uniqueness of $F$ follows from the uniqueness of the Laplace transform: if $F_1, F_2 \in \mathcal{L}'$ both satisfy $p(D)F_j = H$, then $LF_1 = LF_2$ on some half-plane, hence $F_1 = F_2$.

$\square$

The proof just given provides us, in principle, with a way to calculate $F$, given $H$. Carrying out the calculation formally, treating $F$ and $H$ as though they were functions:

$$F(t) = \frac{1}{2\pi i} \int_C e^{tz} LF(z) \, dz
= \frac{1}{2\pi i} \int_C e^{tz} p(z)^{-1} LH(z) \, dz
= \int_{\mathbb{R}} \left[ \frac{1}{2\pi i} \int_C e^{(t-s)z} p(z)^{-1} \, dz \right] H(s) \, ds
= \int_{\mathbb{R}} G(t-s) H(s) \, ds,$$

where

$$G(t) = \frac{1}{2\pi i} \int_C e^{tz} p(z)^{-1} \, dz$$

and $C$ is a line $\operatorname{Re} z = b > a$. This formal calculation motivates the definition of the Green's function $G$ for the operator $p(D)$.
