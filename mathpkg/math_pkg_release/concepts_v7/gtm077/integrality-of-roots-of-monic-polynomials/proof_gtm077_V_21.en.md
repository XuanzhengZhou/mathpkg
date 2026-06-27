---
role: proof
locale: en
of_concept: integrality-of-roots-of-monic-polynomials
source_book: gtm077
source_chapter: "V"
source_section: "§21"
---
# Proof of Integrality of Roots of Monic Polynomials with Integer Coefficients

**Theorem (Theorem 62).** If $\omega$ is a root of an equation

$$x^m + \alpha x^{m-1} + \beta x^{m-2} + \cdots + \lambda = 0$$

where $\alpha, \beta, \ldots, \lambda$ are algebraic integers, then $\omega$ is also an algebraic integer. In particular, the $m$th root of an algebraic integer is an algebraic integer.

*Proof.* Let the conjugates of $\alpha$ be $\alpha^{(1)}, \ldots, \alpha^{(n_\alpha)}$, those of $\beta$ be $\beta^{(1)}, \ldots, \beta^{(n_\beta)}$, and so on through $\lambda$. For each combination of conjugates $(i, j, \ldots, k)$, we have an equation

$$x^m + \alpha^{(i)} x^{m-1} + \beta^{(j)} x^{m-2} + \cdots + \lambda^{(k)} = 0$$

satisfied by $\omega$. Multiplying all such equations together yields a monic polynomial

$$F(x) = \prod_{i,j,\ldots,k} \bigl( x^m + \alpha^{(i)} x^{m-1} + \beta^{(j)} x^{m-2} + \cdots + \lambda^{(k)} \bigr)$$

with $F(\omega) = 0$. The coefficients of $F(x)$ are symmetric in the conjugates of each of $\alpha, \beta, \ldots, \lambda$, and hence, by the fundamental theorem of symmetric polynomials, are integer polynomials in the elementary symmetric functions of those conjugate sets. Since $\alpha, \beta, \ldots, \lambda$ are algebraic integers, their elementary symmetric functions are rational integers. Thus $F(x)$ has rational integer coefficients.

Since $F(x)$ is monic, Theorem 60 implies $\omega$ is an algebraic integer.

For the special case of the $m$th root, consider $\omega$ satisfying $x^m - \mu = 0$ where $\mu$ is an algebraic integer. The coefficient $-\mu$ is an algebraic integer, so by the theorem, $\omega$ (an $m$th root of $\mu$) is an algebraic integer. ∎
