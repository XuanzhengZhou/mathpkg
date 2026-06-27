---
role: proof
locale: en
of_concept: zeta-c-projective-system-of-units
source_book: gtm059
source_chapter: "7"
source_section: "7"
---

*Proof.* We check that for a suitable choice of $\lambda$ (depending on $k$) the Kummer-Takagi exponent given by Theorem 1.2 is $0 \bmod p$. Then $U_c(\theta)$ generates $U_c(\theta)$ over $U_c$ by Nakayama's lemma.

For the computation of the Kummer-Takagi exponents, we need only compute $u_c(\theta)$ and $\theta$. We have
$$\frac{u_c(\theta)}{b} = \frac{\alpha b}{b^0} (1 - \alpha b)\theta.$$
The associated power series is
$$f(X) = \frac{b}{b^0} (1 - X)\theta.$$
Then
$$f'(X) = -\frac{1}{b} \left(1 - \lambda X\right) - \frac{1}{b} \sum_{k=0}^{\infty} X(k)\theta.$$
We prove that $D^*_k O^*(f) \neq 0 \bmod p$ for the required indices.

For the power series computation, we have
$$D[f] = (1 + X[f])^2(J)X = \frac{1}{2} + \frac{1}{2} = 1 + \frac{1}{2}.$$
Since $D = TD_h$, it suffices to prove that for $2 \le k \le p - 2$,
$$\left( TD_h \right)^2 \left( \frac{1}{2} \right) = \left( \frac{1}{2} \right) \bigcup_{j \neq k} 0 \bmod p.$$
By induction,
$$\left( TD_h \right)^2 \left( \frac{1}{2} \right) = \frac{T^{2k-1}}{(1 - p^2)} + P_0 \left( TD_h \right)$$
where $P_0(T, i)$ is a polynomial with $1 \leq \text{degree} \leq m - 2$ and coefficients in $\mathbb{Z}_p$.

The statement $2^{2k-1} P_0(T, i)$ is polynomial in $1 \leq \text{degree} \leq p - A$. It is clearly valid iteratively over $m$ and has a term nonzero modulo $p$. We can therefore choose $1 \leq i_1, i_2, \dots, i_k$ such that $i_i \neq i_k$ is not a root of the polynomial, completing the proof.
