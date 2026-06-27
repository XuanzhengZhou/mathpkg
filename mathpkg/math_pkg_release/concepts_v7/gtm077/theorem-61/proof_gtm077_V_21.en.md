---
role: proof
locale: en
of_concept: theorem-61
source_book: gtm077
source_chapter: "V"
source_section: "§21"
---
# Proof of Theorem 61

**Theorem (Theorem 61).** The sum, difference, and product of two algebraic integers is again an algebraic integer. Hence every rational integral function (polynomial) of integers with rational integral coefficients is again an integer.

*Proof.* Let $\alpha$ and $\beta$ be algebraic integers. Let $\alpha_1, \ldots, \alpha_n$ be the conjugates of $\alpha$ (with respect to $k(1)$) and $\beta_1, \ldots, \beta_m$ be the conjugates of $\beta$. Since $\alpha$ is an integer, it satisfies a monic equation

$$\prod_{i=1}^n (x - \alpha_i) = x^n + a_1 x^{n-1} + \cdots + a_n = 0$$

where the coefficients $a_k$ are, up to sign, the elementary symmetric functions of the $\alpha_i$, and they are rational integers. Similarly, $\beta$ satisfies

$$\prod_{j=1}^m (x - \beta_j) = x^m + b_1 x^{m-1} + \cdots + b_m = 0$$

with rational integral coefficients $b_\ell$.

**Sum.** Consider the polynomial

$$F_+(x) = \prod_{i=1}^n \prod_{j=1}^m \bigl(x - (\alpha_i + \beta_j)\bigr).$$

The coefficients of $F_+(x)$ are symmetric polynomials in the $\alpha_i + \beta_j$ with integer coefficients. By the fundamental theorem of symmetric polynomials, they are expressible as polynomials with integer coefficients in the elementary symmetric functions of the $\alpha_i$ (namely $\pm a_k$) and of the $\beta_j$ (namely $\pm b_\ell$). Hence the coefficients of $F_+(x)$ are rational integers. Moreover, $F_+(x)$ is monic with degree $nm$. Since $\alpha + \beta$ is a root of $F_+$, by Theorem 60, $\alpha + \beta$ is an algebraic integer.

**Difference.** The same argument applied to

$$F_-(x) = \prod_{i=1}^n \prod_{j=1}^m \bigl(x - (\alpha_i - \beta_j)\bigr)$$

shows that $\alpha - \beta$ is an algebraic integer, since the coefficients are again symmetric in the conjugates and therefore rational integers.

**Product.** For the product, consider

$$F_\times(x) = \prod_{i=1}^n \prod_{j=1}^m (x - \alpha_i \beta_j).$$

The coefficients are symmetric functions of $\alpha_i \beta_j$. Each elementary symmetric function of the products $\alpha_i \beta_j$ can be expressed as a polynomial in the elementary symmetric functions of $\alpha_i$ and $\beta_j$ with integer coefficients. Hence the coefficients of $F_\times$ are rational integers. Since $F_\times$ is monic and $\alpha\beta$ is a root, Theorem 60 implies $\alpha\beta$ is an algebraic integer.

The final claim follows by induction: any polynomial in algebraic integers with rational integral coefficients is a finite combination of sums and products of algebraic integers, hence again an algebraic integer. ∎
