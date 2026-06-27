---
role: proof
locale: en
of_concept: prokhorov-poisson-bound
source_book: gtm095
source_chapter: "1"
source_section: "6. De Moivre–Laplace Limit Theorem"
---

# Proof of Prokhorov's Bound on Poisson Convergence Rate

**Prokhorov's Theorem.** Let $np(n) = \lambda > 0$. Then

$$\sum_{k=0}^{\infty} \left| P_n(k) - \pi_k \right| \leq \frac{2\lambda}{n} \cdot \min(2, \lambda),$$

where $P_n(k) = C_n^k p^k q^{n-k}$ is the binomial probability and $\pi_k = e^{-\lambda} \lambda^k / k!$ is the Poisson probability with parameter $\lambda$.

**Proof.** As indicated in the text (Section 6 of Chapter 1), the proof of this result is deferred to a later part of the book. The statement is presented here to exhibit the rate of convergence in Poisson's theorem, complementing the qualitative result that $P_n(k) \to \pi_k$ as $n \to \infty$ when $np(n) \to \lambda$.

The proof of a somewhat weaker estimate is given in **Section 12 of Chapter 3** of the same volume. The full Prokhorov bound, as stated above, gives a total variation distance estimate of order $O(1/n)$ for the convergence of the binomial distribution to the Poisson distribution when the mean $np = \lambda$ is held constant. Note that the bound involves the factor $\min(2, \lambda)$, which distinguishes the cases $\lambda \leq 2$ and $\lambda > 2$.
