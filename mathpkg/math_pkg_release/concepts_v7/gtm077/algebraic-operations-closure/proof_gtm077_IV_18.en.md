---
role: proof
locale: en
of_concept: algebraic-operations-closure
source_book: gtm077
source_chapter: "IV"
source_section: "18"
---
# Proof of Theorem 50: Algebraic Numbers Closed Under Operations

Let $\alpha$ and $\beta$ be algebraic numbers over the number field $k$. Denote by $\alpha_1, \ldots, \alpha_n$ the conjugates of $\alpha$ with respect to $k$, and by $\beta_1, \ldots, \beta_m$ the conjugates of $\beta$ with respect to $k$. The elementary symmetric functions of the $\alpha_i$, as well as those of the $\beta_j$, are numbers in $k$ (being, up to sign, the coefficients of the minimal polynomials of $\alpha$ and $\beta$ over $k$).

**For $\alpha + \beta$:** Consider the product

$$H(x) = \prod_{k=1}^{m} \prod_{i=1}^{n} (x - (\alpha_i + \beta_k)).$$

This expression is symmetric in the $\alpha_i$ (under any permutation of the $\alpha_i$, the double product remains unchanged) and symmetric in the $\beta_k$. By the fundamental theorem on symmetric functions, $H(x)$ can be expressed as a polynomial in the elementary symmetric functions of the $\alpha_i$ and the elementary symmetric functions of the $\beta_k$, with coefficients computed from the coefficients of the original expression using only addition, subtraction, and multiplication. Since the elementary symmetric functions lie in $k$, the coefficients of $H(x)$ also lie in $k$. Hence $H(x)$ is a polynomial over $k$, and $\alpha + \beta$ is among its roots. Therefore $\alpha + \beta$ is algebraic over $k$.

**For $\alpha - \beta$:** Replace $\beta_k$ by $-\beta_k$ in the above argument. The conjugates of $-\beta$ are $-\beta_1, \ldots, -\beta_m$, which are algebraic over $k$ with the same elementary symmetric functions (up to sign). The same construction yields a polynomial over $k$ having $\alpha - \beta$ as a root.

**For $\alpha\beta$:** Consider the product

$$H(x) = \prod_{k=1}^{m} \prod_{i=1}^{n} (x - \alpha_i \beta_k).$$

Again this is symmetric in the $\alpha_i$ and in the $\beta_k$, so its coefficients lie in $k$ by the fundamental theorem on symmetric functions. Thus $\alpha\beta$ is algebraic over $k$.

**For $\alpha/\beta$ (with $\beta \neq 0$):** The conjugates of $1/\beta$ are $1/\beta_1, \ldots, 1/\beta_m$. Since $\beta$ is algebraic over $k$, the elementary symmetric functions of $1/\beta_1, \ldots, 1/\beta_m$ are rational expressions in the elementary symmetric functions of $\beta_1, \ldots, \beta_m$ (specifically, each is the quotient of a symmetric function by the product $\beta_1\cdots\beta_m$), and hence lie in $k$. Then the product

$$H(x) = \prod_{k=1}^{m} \prod_{i=1}^{n} (x - \alpha_i / \beta_k)$$

is symmetric in the $\alpha_i$ and in the $1/\beta_k$, so its coefficients lie in $k$, proving $\alpha/\beta$ is algebraic over $k$.

Thus $\alpha + \beta$, $\alpha - \beta$, $\alpha\beta$, and (when $\beta \neq 0$) $\alpha/\beta$ are all algebraic numbers over $k$.
