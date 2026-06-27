---
role: proof
locale: en
of_concept: approximate-identity-distributions
source_book: gtm012
source_chapter: "7"
source_section: "7. Convolution of distributions"
---

# Proof of Approximation of Periodic Distributions by Smooth Functions

**Theorem 7.7.** Suppose $(\varphi_n)_{1}^{\infty} \subset \mathcal{P}$ is an approximate identity, and suppose $F \in \mathcal{P}'$. Let $F_n = F_{f_n}$, where $f_n = F * \varphi_n$. Then

$$F_n \to F \quad (\mathcal{P}').$$

If $(\varphi_n)_{n=1}^{\infty}$ is an approximate identity consisting of trigonometric polynomials, then the functions $f_n = F * \varphi_n$ are also trigonometric polynomials.

*Proof.* By Proposition 7.1, each $f_n = F * \varphi_n$ is a smooth periodic function, hence $F_n = F_{f_n}$ is a well-defined distribution induced by a smooth function. The convergence $F_n \to F$ in $\mathcal{P}'$ means that for every $u \in \mathcal{P}$,

$$F_n(u) = \frac{1}{2\pi} \int_0^{2\pi} f_n(x) u(x) \, dx \to F(u).$$

This follows from the approximate identity property and Proposition 7.4, which gives

$$F_{f_n}(u) = F(\tilde{\varphi}_n * u),$$

and since $\tilde{\varphi}_n * u \to u$ in $\mathcal{P}$ (by the definition of an approximate identity), the continuity of $F$ yields the result.

For the trigonometric polynomial case, let

$$e_k(x) = \exp(2\pi i k x).$$

Then

$$(F * e_k)(x) = F(T_x \tilde{e}_k).$$

But

$$(T_x \tilde{e}_k)(y) = \tilde{e}_k(y - x) = e_k(x - y) = e_k(x) \overline{e_k(y)} = e_k(x) e_{-k}(y).$$

Wait, more carefully:

$$(T_x \tilde{e}_k)(y) = \tilde{e}_k(y - x) = e_k(x - y) = e_k(x) e_k(-y) = e_k(x) \tilde{e}_k(y).$$

Thus

$$(F * e_k)(x) = F(e_k(x) \tilde{e}_k) = e_k(x) F(\tilde{e}_k) = F(e_{-k}) e_k(x).$$

So

$$F\left(\sum a_k e_k\right) = \sum a_k F(e_{-k}) e_k$$

is a trigonometric polynomial. $\square$

This theorem is the distributional analog of the classical result that smooth functions are dense in the space of distributions, and it shows that every periodic distribution can be approximated by trigonometric polynomials when a trigonometric polynomial approximate identity is used.
