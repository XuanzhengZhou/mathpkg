---
role: exercise
locale: en
chapter: "11"
section: "11.8"
exercise_number: 5
---
# Exercise 11.5

Let $(A, X, \Omega, f)$ be a maximum modulus algebra such that, for some integer $n$, $\# f^{-1}(\lambda) \leq n$ for all $\lambda \in \Omega$ and such that there exists $\lambda_0 \in \Omega$ with $\# f^{-1}(\lambda_0) = n$.

Show that, for all $g \in A$, there exist bounded analytic functions $a_1, a_2, \ldots, a_n$ on $\Omega$ such that, for each $\lambda \in \Omega$, if $f^{-1}(\lambda) = \{p_1(\lambda), \ldots, p_k(\lambda)\}$ with $k \leq n$ (counting multiplicities), then the values $g(p_j(\lambda))$, $j = 1, \ldots, k$, are the roots of the monic polynomial

$$z^n + a_1(\lambda) z^{n-1} + a_2(\lambda) z^{n-2} + \cdots + a_n(\lambda) = 0,$$

where the remaining $n - k$ roots are taken to be zero (or any prescribed value).

*Hint:* The coefficient functions $a_j(\lambda)$ are, up to sign, the elementary symmetric functions of the values of $g$ on the fiber $f^{-1}(\lambda)$. Express $\prod_{j=1}^k (z - g(p_j(\lambda)))$ as a polynomial in $z$, and note that the coefficients are analytic on $\Omega_n = \{\lambda : \# f^{-1}(\lambda) = n\}$ by Corollary 11.3, and extend analytically to all of $\Omega$ using Rado's theorem and the fact that the exceptional set is discrete (Theorem 11.8).
