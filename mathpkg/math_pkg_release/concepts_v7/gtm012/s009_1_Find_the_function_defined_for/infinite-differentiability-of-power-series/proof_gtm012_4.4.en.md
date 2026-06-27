---
role: proof
locale: en
of_concept: infinite-differentiability-of-power-series
source_book: gtm012
source_chapter: "4"
source_section: "4"
---

# Proof of Infinite Differentiability of Power Series

**Corollary 4.5.** The function $f$ defined by the power series

$$f(x) = \sum_{n=0}^{\infty} a_n (x - x_0)^n, \quad |x - x_0| < R,$$

with $R > 0$, is infinitely differentiable on $|x - x_0| < R$, and its $k$-th derivative is given by the termwise differentiated series

$$f^{(k)}(x) = \sum_{n=k}^{\infty} n(n-1)(n-2) \cdots (n-k+1) a_n (x - x_0)^{n-k}, \quad |x - x_0| < R. \tag{4.11}$$

**Proof.** The proof proceeds by induction on $k$.

*Base case $k = 1$.* Theorem 4.4 (termwise differentiation of power series) states that $f$ is differentiable on $|x - x_0| < R$ and

$$f'(x) = \sum_{n=1}^{\infty} n a_n (x - x_0)^{n-1}, \quad |x - x_0| < R.$$

This is exactly formula (4.11) for $k = 1$.

*Inductive step.* Assume that $f$ is $k$ times differentiable and that (4.11) holds for some $k \geq 1$. The series on the right-hand side of (4.11) is itself a power series in $(x - x_0)$ with coefficients

$$b_n = (n+k)(n+k-1) \cdots (n+1) a_{n+k},$$

and its radius of convergence is also $R$ (by the same argument as in Theorem 4.4). Applying Theorem 4.4 to this series, we may differentiate it termwise once more, obtaining

$$f^{(k+1)}(x) = \sum_{n=k}^{\infty} n(n-1) \cdots (n-k+1) a_n \cdot (n-k)(x - x_0)^{n-k-1}$$
$$= \sum_{n=k+1}^{\infty} n(n-1)(n-2) \cdots (n-k) a_n (x - x_0)^{n-(k+1)}, \quad |x - x_0| < R.$$

This is exactly formula (4.11) with $k$ replaced by $k+1$. By induction, $f$ is infinitely differentiable and (4.11) holds for all $k \in \mathbb{N}$. $\square$
