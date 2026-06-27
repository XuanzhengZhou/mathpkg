---
role: proof
locale: en
of_concept: berry-esseen-bernoulli-bound
source_book: gtm095
source_chapter: "1"
source_section: "6. De Moivre–Laplace Limit Theorem"
---

# Proof of the Berry–Esseen Bound for the Bernoulli Scheme

**Berry–Esseen Bound (Bernoulli case).** For the standardized sum $S_n = \xi_1 + \cdots + \xi_n$ of independent Bernoulli random variables with $P(\xi_i = 1) = p$, $P(\xi_i = 0) = q = 1-p$, let

$$F_n(x) = P\left\{ \frac{S_n - np}{\sqrt{npq}} \leq x \right\}$$

be the distribution function of the normalized sum. Then

$$\sup_{-\infty \leq x \leq \infty} |F_n(x) - \Phi(x)| \leq \frac{p^2 + q^2}{\sqrt{npq}},$$

where $\Phi(x) = \frac{1}{\sqrt{2\pi}} \int_{-\infty}^x e^{-t^2/2} dt$ is the standard normal distribution function.

**Proof.** This inequality is stated in Section 6 of Chapter 1 as a special case of the general Berry–Esseen theorem. The general proof, which applies to sums of independent random variables with finite third absolute moments, is given in **Section 11 of Chapter 3**.

The general Berry–Esseen theorem states that for independent, identically distributed random variables $X_1, \ldots, X_n$ with $E X_1 = 0$, $\text{Var} X_1 = \sigma^2 > 0$, and $E|X_1|^3 < \infty$,

$$\sup_x \left| P\left\{ \frac{S_n}{\sigma\sqrt{n}} \leq x \right\} - \Phi(x) \right| \leq \frac{C \cdot E|X_1|^3}{\sigma^3 \sqrt{n}},$$

where $C$ is an absolute constant. The bound presented here is the specialization to Bernoulli random variables with a concrete constant.

The bound is of order $O(1/\sqrt{npq})$. It is important to note that this order cannot be improved, which means that the normal approximation to $F_n(x)$ via $\Phi(x)$ can be poor for values of $p$ close to $0$ or $1$, even when $n$ is large. This observation motivates the use of the Poisson approximation (Section 4 of the same chapter) for the case of small $p$.
