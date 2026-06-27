---
role: proof
locale: en
of_concept: integers-closed-under-ops
source_book: gtm077
source_chapter: "V"
source_section: "§21"
---
# Proof of Theorem 61: Algebraic Integers Closed Under Operations

**Theorem (Theorem 61).** The sum, difference, and product of two algebraic integers are again algebraic integers.

*Proof.* Let $\alpha, \beta$ be algebraic integers with conjugates $\alpha_1, \ldots, \alpha_n$ and $\beta_1, \ldots, \beta_m$ respectively.

For the **sum**, form

$$F_+(x) = \prod_{i=1}^n \prod_{j=1}^m \bigl(x - (\alpha_i + \beta_j)\bigr).$$

The coefficients of this monic polynomial are symmetric in the $nm$ quantities $\alpha_i + \beta_j$. By the theory of symmetric functions, each coefficient is an integer-coefficient polynomial in the elementary symmetric functions of the $\alpha_i$ (which are rational integers, since $\alpha$ is an integer) and of the $\beta_j$ (rational integers, since $\beta$ is an integer). Hence the coefficients of $F_+(x)$ are rational integers. Since $F_+(\alpha + \beta) = 0$ and $F_+$ is monic, Theorem 60 implies $\alpha + \beta$ is an algebraic integer.

For the **difference**, the same argument applied to

$$F_-(x) = \prod_{i=1}^n \prod_{j=1}^m \bigl(x - (\alpha_i - \beta_j)\bigr)$$

shows $\alpha - \beta$ is an algebraic integer.

For the **product**, the monic polynomial

$$F_\times(x) = \prod_{i=1}^n \prod_{j=1}^m (x - \alpha_i \beta_j)$$

has coefficients that are symmetric in $\alpha_i \beta_j$ and therefore rational integers. Since $F_\times(\alpha\beta) = 0$, Theorem 60 yields that $\alpha\beta$ is an algebraic integer. ∎
