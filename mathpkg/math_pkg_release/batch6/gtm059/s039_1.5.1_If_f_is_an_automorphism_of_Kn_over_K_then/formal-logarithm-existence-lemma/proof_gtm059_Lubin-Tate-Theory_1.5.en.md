---
role: proof
locale: en
of_concept: formal-logarithm-existence-lemma
source_book: gtm059
source_chapter: "Lubin-Tate Theory"
source_section: "1.5"
---

*Proof.* We look at the difference

$$\frac{1}{\pi^{n+1}} [\pi^{n+1}](X) - \frac{1}{\pi^n} [\pi^n](X) = \frac{1}{\pi^{n+1}} \left( [\pi]([\pi^n](X)) - \pi [\pi^n](X) \right).$$

Let

$$s_i^{(n)}(X) = \sigma^{(n)}(X) + g_i^{(n)}(X),$$

where

$$g_i^{(n)}(X) = \sum c_i^{(n)} X^i$$

and the terms in $g_i^{(n)}$ have degree at least $n+1$ with each term of degree at least $2$.

The power series $[\pi](X) - \pi X$ has coefficients in $\pi \mathfrak{o}$. Therefore the right-hand side of the difference is divisible by higher powers of $\pi$ as $n$ grows.

We are interested in the coefficients of monomials of degree $\leq k$ for a fixed $k$. Reducing all expressions modulo $X^{k+1}$, we see that we may assume

$$g_1 X = g_2 X + g_3 X$$

and successive differences are divisible by $\pi^n$. Since each nontrivial term in the difference has degree at least $2$, it follows that for any fixed degree $k$, the coefficient sequence is Cauchy in the $p$-adic topology, hence convergent.

The additivity property $\lambda(X +_A Y) = \lambda(X) + \lambda(Y)$ follows by taking the limit of the additivity relation for $[\pi^n]$, which satisfies

$$[\pi^n](X +_A Y) = [\pi^n](X) +_A [\pi^n](Y)$$

because $[\pi^n]$ is an endomorphism of $A$. Dividing by $\pi^n$ and taking the limit, the formal group addition $+_A$ becomes ordinary addition $+$, since the nonlinear terms in $+_A$ are washed out by the limit process.

**Remark.** The convergence is not uniform in $k$, but for each fixed $k$ the limit exists as $n \to \infty$. The resulting logarithm $\lambda(X)$ has $\lambda'(0) = 1$ and coefficients in the completion of the maximal unramified extension of $K$.

**Example.** If $A = G_m$ is the formal multiplicative group, then the logarithm is given by

$$\lambda(X) = \log(1 + X) = X - \frac{X^2}{2} + \frac{X^3}{3} - \cdots,$$

the usual power series for the logarithm from calculus.
