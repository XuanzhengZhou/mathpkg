---
role: proof
locale: en
of_concept: integer-root-of-integer-coeff-equation
source_book: gtm077
source_chapter: "V"
source_section: "§21"
---
# Proof of Theorem 62: Integer Root of Equation with Integer Coefficients

**Theorem (Theorem 62).** If $\omega$ is a root of an equation whose coefficients are algebraic integers, then $\omega$ is also an algebraic integer.

*Proof.* Suppose $\omega$ satisfies

$$x^m + \alpha x^{m-1} + \beta x^{m-2} + \cdots + \lambda = 0$$

where $\alpha, \beta, \ldots, \lambda$ are algebraic integers. Let $\alpha^{(1)}, \ldots, \alpha^{(n_\alpha)}$ be the conjugates of $\alpha$, and similarly for $\beta, \ldots, \lambda$.

For each choice of a conjugate for each coefficient, $\omega$ satisfies a corresponding equation. Multiply all $n_\alpha \cdot n_\beta \cdots n_\lambda$ such equations together to obtain a monic polynomial $F(x)$ with $\omega$ as a root:

$$F(x) = \prod_{i,j,\ldots,k} \bigl( x^m + \alpha^{(i)} x^{m-1} + \beta^{(j)} x^{m-2} + \cdots + \lambda^{(k)} \bigr).$$

The coefficients of $F(x)$ are symmetric in the conjugates of each coefficient individually. By the fundamental theorem of symmetric polynomials, each coefficient is an integer polynomial in the elementary symmetric functions of the $\alpha^{(i)}$, the $\beta^{(j)}$, and so on. Since $\alpha$ is an algebraic integer, the elementary symmetric functions of its conjugates are rational integers (they are, up to sign, the coefficients of the irreducible monic polynomial for $\alpha$). The same holds for $\beta, \ldots, \lambda$. Therefore every coefficient of $F(x)$ is a rational integer.

Since $F(x)$ is monic with rational integer coefficients and $F(\omega) = 0$, Theorem 60 yields that $\omega$ is an algebraic integer. ∎
