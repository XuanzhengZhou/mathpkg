---
role: proof
locale: en
of_concept: characteristic-function-nondegeneracy-condition
source_book: gtm095
source_chapter: "Chapter 3"
source_section: "§5. Inversion formula, moments and semi-invariants"
---

# Proof of Bochner-type nondegeneracy condition for characteristic functions

**Theorem 2.** A distribution function $F = F(x)$ is uniquely determined by its characteristic function $\varphi = \varphi(t)$.

Let $F = F(x)$ and $G = G(x)$ be two distribution functions with the same characteristic function $\varphi(t) = \int_{-\infty}^{\infty} e^{itx} dF(x) = \int_{-\infty}^{\infty} e^{itx} dG(x)$ for all $t \in \mathbb{R}$.

Consider the smoothed indicator function:

$$f^\varepsilon(x) = \frac{1}{\sqrt{2\pi\varepsilon}} \int_a^b e^{-(y-x)^2/2\varepsilon} dy.$$

As $\varepsilon \to 0$, we have $f^\varepsilon(x) \to I_{(a,b]}(x)$.

By the inversion/continuity properties of characteristic functions and the identity $\int e^{itx} dF(x) = \int e^{itx} dG(x)$, one can show that for all bounded continuous functions $f$,

$$\int_{-\infty}^{\infty} f(x) dF(x) = \int_{-\infty}^{\infty} f(x) dG(x).$$

Applying this to $f^\varepsilon$ and taking $\varepsilon \to 0$ yields, by the dominated convergence theorem:

$$\int_{-\infty}^{\infty} I_{(a,b]}(x) dF(x) = \int_{-\infty}^{\infty} I_{(a,b]}(x) dG(x),$$

i.e., $F(b) - F(a) = G(b) - G(a)$. Since $a$ and $b$ are arbitrary continuity points, it follows that $F(x) = G(x)$ for all $x \in \mathbb{R}$.

This completes the proof of the theorem.

---

**Bochner's Criterion (Nondegeneracy condition).** A function $\varphi(t)$ is a characteristic function if and only if $\varphi(0) = 1$, $\varphi$ is continuous at $0$, and $\varphi$ is nonnegative definite, i.e., for all $n \geq 1$, all real $t_1, \ldots, t_n$, and all complex $\lambda_1, \ldots, \lambda_n$,

$$\sum_{i,j=1}^{n} \varphi(t_i - t_j) \lambda_i \bar{\lambda}_j \geq 0.$$

*Necessity.* If $\varphi(t) = \int_{-\infty}^{\infty} e^{itx} dF(x)$, then

$$\sum_{i,j=1}^{n} \varphi(t_i - t_j) \lambda_i \bar{\lambda}_j = \int_{-\infty}^{\infty} \left| \sum_{k=1}^{n} \lambda_k e^{it_k x} \right|^2 dF(x) \geq 0.$$

The sufficiency is more difficult; see [31], XIX.2.
