---
role: proof
locale: en
of_concept: operator-action-on-polynomial-ring
source_book: gtm059
source_chapter: "2"
source_section: "1"
---

Write $\zeta = \sum_{i=0}^{n} a_i R(X)^i$ with integral coefficients $a_i$. Then

$$
S^n = N^n - \sum_{i=0}^{n} a_i R(X) \frac{1}{k} [R_X]_{i=0}^{n-1} r_i^n.
$$

The factor $\frac{1}{k}$ appears from the fundamental identity $\frac{1}{k}(B_k(X+1) - B_k(X)) = X^{k-1}$. Applying the elementary formula for Bernoulli polynomials,

$$
\frac{N^{n-1}}{k} R_X\!\left(\frac{1}{k}\right) = \sum_{i=0}^{n-1} \binom{n}{i} B_i b^{n-i},
$$

which is obtained directly from the definition of the Bernoulli polynomials via the generating function. The integrality follows because each term on the right-hand side has integer coefficients when $b$ is an integer, as the Bernoulli numbers $B_i$ are rational numbers whose denominators are controlled by the von Staudt-Clausen theorem. After clearing denominators as appropriate, the expression is seen to be integral.
