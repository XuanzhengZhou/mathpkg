---
role: proof
locale: en
of_concept: integers-form-a-ring
source_book: gtm077
source_chapter: "V"
source_section: "§21"
---
# Proof that Algebraic Integers Form a Ring

**Theorem (Theorem 61).** The sum, difference, and product of two algebraic integers is again an algebraic integer. Thus the set of all algebraic integers forms a ring. Every polynomial with rational integral coefficients evaluated at algebraic integers yields an algebraic integer.

*Proof.* Let $\alpha$ and $\beta$ be algebraic integers with conjugates $\alpha_1, \ldots, \alpha_n$ and $\beta_1, \ldots, \beta_m$.

**Sum and difference.** The monic polynomial

$$F_\pm(x) = \prod_{i=1}^n \prod_{j=1}^m \bigl(x - (\alpha_i \pm \beta_j)\bigr)$$

has coefficients that are symmetric polynomials in $\alpha_i \pm \beta_j$. By the fundamental theorem of symmetric polynomials, each coefficient is an integer polynomial in the elementary symmetric functions of $\{\alpha_i\}$ and $\{\beta_j\}$. Since $\alpha$ and $\beta$ are integers, these elementary symmetric functions are rational integers (up to sign, they are the coefficients of the monic irreducible polynomials satisfied by $\alpha$ and $\beta$). Hence $F_\pm(x)$ has rational integer coefficients and is monic. Since $\alpha \pm \beta$ is a root, Theorem 60 yields that $\alpha \pm \beta$ is an algebraic integer.

**Product.** Similarly,

$$F_\times(x) = \prod_{i=1}^n \prod_{j=1}^m (x - \alpha_i \beta_j)$$

is monic with coefficients expressible as integer polynomials in the elementary symmetric functions of the $\alpha_i$ and $\beta_j$, hence rational integers. Therefore $\alpha\beta$ is an algebraic integer by Theorem 60.

Since addition, subtraction, and multiplication all stay within the set of algebraic integers, and the set contains $1$ (the root of $x-1=0$), the algebraic integers form a commutative ring with identity. The fact that any polynomial expression with rational integer coefficients evaluated at algebraic integers yields an algebraic integer follows by induction from the closure properties proved above. ∎
