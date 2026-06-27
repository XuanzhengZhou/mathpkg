---
role: proof
locale: en
of_concept: uniform-convergence-implies-limit-of-integrals
source_book: gtm012
source_chapter: "4"
source_section: "4. Sequences and series of functions"
---

# Proof of Theorem 4.2: Uniform convergence implies convergence of integrals

**Theorem 4.2.** Suppose $(f_n)_{n=1}^{\infty}$ is a sequence of continuous complex-valued functions on the interval $[a, b]$, and suppose it converges uniformly to $f$. Then

$$\int_a^b f = \lim_{n \to \infty} \int_a^b f_n.$$

*Proof.* Since each $f_n$ is continuous and the convergence is uniform, the limit function $f$ is also continuous (by Theorem 4.1), hence Riemann integrable. Using the basic estimate for Riemann integrals (property (2.2) in the text),

$$
\left| \int_a^b f_n - \int_a^b f \right|
= \left| \int_a^b (f_n - f) \right|
\leq \|f_n - f\|_{\infty} \cdot |b - a|.
$$

Since $f_n \to f$ uniformly, $\|f_n - f\|_{\infty} \to 0$ as $n \to \infty$. Therefore

$$\lim_{n \to \infty} \left| \int_a^b f_n - \int_a^b f \right| = 0,$$

which is equivalent to $\int_a^b f = \lim_{n \to \infty} \int_a^b f_n$. $\square$
