---
role: proof
locale: en
of_concept: theorem-62
source_book: gtm077
source_chapter: "V"
source_section: "§21"
---
# Proof of Theorem 62

**Theorem (Theorem 62).** If $\omega$ is a root of an equation

$$x^m + \alpha x^{m-1} + \beta x^{m-2} + \cdots + \lambda = 0$$

where $\alpha, \beta, \ldots, \lambda$ are algebraic integers, then $\omega$ is also an algebraic integer.

*Proof.* The argument proceeds in a manner similar to the proof of Theorem 61 and relies on Theorem 51. Let $\alpha^{(1)}, \ldots, \alpha^{(n_\alpha)}$ be the conjugates of $\alpha$; let $\beta^{(1)}, \ldots, \beta^{(n_\beta)}$ be the conjugates of $\beta$; and so on for all coefficients up to $\lambda$.

For each choice of conjugates, we obtain an equation satisfied by $\omega$:

$$x^m + \alpha^{(i)} x^{m-1} + \beta^{(j)} x^{m-2} + \cdots + \lambda^{(k)} = 0.$$

Take the product of all such equations over all combinations of conjugates of the coefficients. This yields a monic polynomial equation satisfied by $\omega$:

$$F(x) = \prod_{i,j,\ldots,k} \Bigl( x^m + \alpha^{(i)} x^{m-1} + \beta^{(j)} x^{m-2} + \cdots + \lambda^{(k)} \Bigr) = 0.$$

The coefficients of $F(x)$ are symmetric polynomials in the conjugates of each of the coefficients $\alpha, \beta, \ldots, \lambda$. By the fundamental theorem of symmetric polynomials, each coefficient of $F(x)$ is expressible as a polynomial with integer coefficients in the elementary symmetric functions of the conjugates of $\alpha$, of $\beta$, \ldots, of $\lambda$. Since $\alpha, \beta, \ldots, \lambda$ are algebraic integers, their elementary symmetric functions are rational integers. Hence the coefficients of $F(x)$ are rational integers, and $F(x)$ is monic. By Theorem 60, $\omega$ is an algebraic integer.

In particular, taking $\alpha = \beta = \cdots = \lambda = 0$, we see that the $m$th root of an algebraic integer $\mu$ (which satisfies $x^m - \mu = 0$, an equation whose coefficients are algebraic integers) is again an algebraic integer. ∎
