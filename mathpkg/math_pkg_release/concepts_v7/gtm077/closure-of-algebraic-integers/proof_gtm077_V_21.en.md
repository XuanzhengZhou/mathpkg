---
role: proof
locale: en
of_concept: closure-of-algebraic-integers
source_book: gtm077
source_chapter: "V"
source_section: "§21"
---
# Proof of Theorem 61: Closure of Algebraic Integers

**Theorem (Theorem 61).** The sum, difference, and product of two algebraic integers is again an algebraic integer. Hence every polynomial in algebraic integers with rational integer coefficients is again an algebraic integer.

*Proof.* Let $\alpha$ and $\beta$ be algebraic integers with conjugates $\alpha_1, \ldots, \alpha_n$ and $\beta_1, \ldots, \beta_m$ respectively. Since $\alpha$ is an algebraic integer, the elementary symmetric functions of $\alpha_1, \ldots, \alpha_n$ are rational integers; likewise for the $\beta_j$.

For the **sum** $\alpha + \beta$, form the polynomial

$$F_+(x) = \prod_{i=1}^n \prod_{j=1}^m \bigl(x - (\alpha_i + \beta_j)\bigr).$$

This is a monic polynomial of degree $nm$. Its coefficients are symmetric polynomials in all the $\alpha_i + \beta_j$. Since any symmetric polynomial in $\alpha_i + \beta_j$ can be expressed as a polynomial with integer coefficients in the elementary symmetric functions of the $\alpha_i$ and the $\beta_j$, the coefficients of $F_+(x)$ are rational integers. As $F_+(\alpha + \beta) = 0$, Theorem 60 implies $\alpha + \beta$ is an algebraic integer.

For the **difference** $\alpha - \beta$, replace $\beta_j$ by $-\beta_j$ in the above construction. Since $-\beta$ is also an algebraic integer (its defining polynomial is obtained by substituting $x \mapsto -x$), the same argument shows $\alpha - \beta$ is an algebraic integer.

For the **product** $\alpha\beta$, consider the monic polynomial

$$F_\times(x) = \prod_{i=1}^n \prod_{j=1}^m (x - \alpha_i \beta_j).$$

The elementary symmetric functions of the $nm$ numbers $\alpha_i \beta_j$ are symmetric in the $\alpha_i$ for each fixed set of $\beta_j$, and symmetric in the $\beta_j$ overall. Hence they are integer polynomials in the elementary symmetric functions of the $\alpha_i$ and of the $\beta_j$, and therefore rational integers. Theorem 60 then yields that $\alpha\beta$ is an algebraic integer.

The extension to arbitrary polynomial expressions follows by induction on the number of operations. ∎
