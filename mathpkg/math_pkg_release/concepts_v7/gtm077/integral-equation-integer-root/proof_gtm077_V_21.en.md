---
role: proof
locale: en
of_concept: integral-equation-integer-root
source_book: gtm077
source_chapter: "V"
source_section: "§21"
---
# Proof of Theorem 62: Integral Equation Implies Integer Root

**Theorem (Theorem 62).** If $\omega$ is a root of an equation

$$x^m + \alpha x^{m-1} + \beta x^{m-2} + \cdots + \lambda = 0$$

where $\alpha, \beta, \ldots, \lambda$ are algebraic integers, then $\omega$ is also an algebraic integer.

*Proof.* Let $\{\alpha^{(i)}\}$, $\{\beta^{(j)}\}$, \ldots, $\{\lambda^{(k)}\}$ be the complete sets of conjugates (with respect to $k(1)$) of the coefficients $\alpha, \beta, \ldots, \lambda$, respectively. For each tuple of conjugates, $\omega$ satisfies

$$\omega^m + \alpha^{(i)} \omega^{m-1} + \beta^{(j)} \omega^{m-2} + \cdots + \lambda^{(k)} = 0.$$

Form the product over all such equations:

$$F(x) = \prod_{i,j,\ldots,k} \Bigl( x^m + \alpha^{(i)} x^{m-1} + \beta^{(j)} x^{m-2} + \cdots + \lambda^{(k)} \Bigr).$$

The polynomial $F(x)$ is monic, and its coefficients are symmetric in the conjugates of each coefficient $\alpha, \beta, \ldots, \lambda$. By Theorem 51 (or the fundamental theorem on symmetric functions), each coefficient of $F(x)$ is an integer-coefficient polynomial in the elementary symmetric functions of the conjugates of $\alpha$, of $\beta$, \ldots, of $\lambda$.

Since $\alpha, \beta, \ldots, \lambda$ are algebraic integers, their elementary symmetric functions (taken with respect to their respective conjugate sets) are rational integers. Therefore the coefficients of $F(x)$ are rational integers. Since $F(\omega) = 0$ and $F$ is monic, Theorem 60 implies that $\omega$ is an algebraic integer. ∎
