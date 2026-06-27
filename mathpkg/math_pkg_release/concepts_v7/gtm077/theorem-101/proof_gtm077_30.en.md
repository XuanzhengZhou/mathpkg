---
role: proof
locale: en
of_concept: theorem-101
source_book: gtm077
source_chapter: "30"
source_section: "Second Type of Decomposition Theorem for Rational Primes"
---

# Proof of Theorem 101

The numbers $\lambda$ with the property (64) cannot have arbitrarily large ideal denominators. This is true since the hypothesis is equivalent to $n$ equations

$$S(\lambda \alpha_k) = g_k \quad (k = 1, 2, \ldots, n),$$

where the $g_k$ are rational integers, and from the $n$ linear equations for $\lambda^{(1)}, \ldots, \lambda^{(n)}$ these $\lambda^{(i)}$ are obtained as quotients of two determinants. The denominator is the fixed determinant of the $\alpha_k^{(i)}$ which is equal to $N(\mathfrak{a})\sqrt{d}$. The numerator is an integral polynomial in the $\alpha_k^{(i)}$. Consequently there is an integer $\omega$ depending only on the $\mathfrak{a}$, such that $\omega\lambda$ is an integer. Moreover, if $\lambda_1$ and $\lambda_2$ belong to this set of $\lambda$, then for all integers $\xi_1, \xi_2$,

$$S((\lambda_1\xi_1 + \lambda_2\xi_2)\alpha) = \xi_1 S(\lambda_1\alpha) + \xi_2 S(\lambda_2\alpha)$$

is an integer. Hence the set $\mathfrak{m}$ forms an ideal.

Now set

$$S(\lambda \alpha_k) = g_k \quad (k = 1, 2, \ldots, n),$$

where $\lambda$ satisfies (64). Then we also have

$$S(\lambda_0 \alpha_k) = g_k \quad \text{for } \lambda_0 = g_1 \beta_1 + \cdots + g_n \beta_n.$$

Consequently

$$\lambda = \lambda_0 = g_1 \beta_1 + \cdots + g_n \beta_n$$

and the $\beta_1, \ldots, \beta_n$ form a basis for $\mathfrak{m}(\mathfrak{a})$, provided they are numbers in $K$. The latter fact is obtained directly from the representation of the solutions of (65) as a determinant. Alternatively by multiplication by $\alpha_i^{(q)}$ and summation over $i$ we can deduce from (65) the equivalent system of equations

$$\sum_p \alpha_k^{(p)} \sum_i \beta_i^{(p)} \alpha_i^{(q)} = \sum_i e_{ik} \alpha_i^{(q)} = \alpha_k^{(q)} = \sum_p e_{pq} \alpha_k^{(p)}$$

and from this we deduce

$$\sum_i \beta_i^{(p)} \alpha_i^{(q)} = e_{pq}, \quad \sum_i \beta_i^{(p)} \sum_q \alpha_q^{(q)} = \sum_q e_{pq} \alpha_k^{(q)}$$

or

$$\sum_{i=1}^{n} \beta_i^{(p)} S(\alpha_i \alpha_k) = \alpha_k^{(p)}.$$

Since the coefficients on the left-hand side are now rational, the $\beta_i^{(p)}$ are numbers in $K^{(p)}$. Hence Theorem 101 is proved.
