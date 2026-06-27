---
role: proof
locale: en
of_concept: fundamental-theorem-of-symmetric-polynomials
source_book: gtm030
source_chapter: "II"
source_section: "11"
---

It suffices to prove the result for homogeneous symmetric polynomials since any polynomial is a unique sum of its homogeneous parts, and symmetrization preserves degree.

Let $f(x_1, \cdots, x_r)$ be a homogeneous symmetric polynomial of degree $m$. Introduce the lexicographic ordering on monomials $a x_1^{k_1} x_2^{k_2} \cdots x_r^{k_r}$ (with $a \neq 0$): compare exponents $(k_1, \cdots, k_r)$ lexicographically. Choose the highest monomial in $f$, say $a x_1^{k_1} x_2^{k_2} \cdots x_r^{k_r}$.

Note that the highest term of $p_k$ is $x_1 x_2 \cdots x_k$ (since the product $x_1 x_2 \cdots x_k$ is the lexicographically largest term in $\sum_{i_1 < \cdots < i_k} x_{i_1} \cdots x_{i_k}$). Hence the highest term of $p_1^{k_1-k_2} p_2^{k_2-k_3} \cdots p_r^{k_r}$ is $x_1^{k_1} x_2^{k_2} \cdots x_r^{k_r}$.

Set $f_1 = f - a p_1^{k_1-k_2} p_2^{k_2-k_3} \cdots p_r^{k_r}$. Then $f_1$ is a homogeneous symmetric polynomial whose highest term is lexicographically smaller. Repeating this process, since there are only finitely many monomials below a given one, we eventually obtain a representation of $f$ as a polynomial in the $p_i$.

For algebraic independence, suppose $\sum a_{d_1 \cdots d_r} p_1^{d_1} \cdots p_r^{d_r} = 0$. If some coefficient is nonzero, define $k_i = d_i + d_{i+1} + \cdots + d_r$. The highest term of $a_{d_1 \cdots d_r} p_1^{d_1} \cdots p_r^{d_r}$ is $a_{d_1 \cdots d_r} x_1^{k_1} \cdots x_r^{k_r}$. For different exponent tuples $(d_1, \cdots, d_r)$, the corresponding $(k_1, \cdots, k_r)$ tuples differ, so the highest terms do not cancel. Hence the coefficient of the lexicographically largest monomial must be zero, contradiction. Thus the $p_i$ are algebraically independent.
