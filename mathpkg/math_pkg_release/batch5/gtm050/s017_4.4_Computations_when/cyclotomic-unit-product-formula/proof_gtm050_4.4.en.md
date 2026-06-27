---
role: proof
locale: en
of_concept: cyclotomic-unit-product-formula
source_book: gtm050
source_chapter: "4"
source_section: "4.4"
---

**Proof (sketch).** Consider the polynomial identity in the indeterminate $t$:

$$
t^{\lambda-1} + t^{\lambda-2} + \cdots + t + 1 = \prod_{j=1}^{\lambda-1} (t - \alpha^j).
$$

Evaluating at $t = 1$ gives $\lambda = \prod_{j=1}^{\lambda-1} (1 - \alpha^j)$. Now consider the logarithmic derivative approach.

Alternatively, rewrite the desired product using the identity $\alpha^j - 1 = (\alpha - 1)(\alpha^{j-1} + \alpha^{j-2} + \cdots + \alpha + 1)$. Then

$$
\prod_{j=2}^{\lambda-1} (\alpha^j - 1) = \prod_{j=2}^{\lambda-1} (\alpha - 1)\sum_{k=0}^{j-1} \alpha^k = (\alpha - 1)^{\lambda-2} \prod_{j=2}^{\lambda-1} \frac{\alpha^j - 1}{\alpha - 1}.
$$

A more direct approach: since $\alpha^\lambda = 1$ and $1 + \alpha + \cdots + \alpha^{\lambda-1} = 0$, the product $\prod_{j=2}^{\lambda-1} (\alpha^j - 1)$ can be computed by expanding and repeatedly applying the relation $\alpha^\lambda = 1$. The result simplifies to the stated formula with descending coefficients.

**Verification for small $\lambda$.** For $\lambda = 5$, the formula gives:

$$
(\alpha^2 - 1)(\alpha^3 - 1)(\alpha^4 - 1) = 4\alpha^4 + 3\alpha^3 + 2\alpha^2 + \alpha.
$$

Expanding the left side: $(\alpha^2-1)(\alpha^3-1) = \alpha^5 - \alpha^2 - \alpha^3 + 1 = 1 - \alpha^2 - \alpha^3 + 1 = 2 - \alpha^2 - \alpha^3$. Multiplying by $(\alpha^4-1)$: $(2 - \alpha^2 - \alpha^3)(\alpha^4-1) = 2\alpha^4 - 2 - \alpha^6 + \alpha^2 - \alpha^7 + \alpha^3$. Using $\alpha^5 = 1$, so $\alpha^6 = \alpha$ and $\alpha^7 = \alpha^2$, we obtain $2\alpha^4 - 2 - \alpha + \alpha^2 - \alpha^2 + \alpha^3 = 2\alpha^4 - 2 - \alpha + \alpha^3$. Using $1 + \alpha + \alpha^2 + \alpha^3 + \alpha^4 = 0$, we have $-2 = 2(\alpha + \alpha^2 + \alpha^3 + \alpha^4)$, giving $(2\alpha^4 + 2\alpha + 2\alpha^2 + 2\alpha^3 + 2\alpha^4) - \alpha + \alpha^3 = 4\alpha^4 + 3\alpha^3 + 2\alpha^2 + \alpha$, confirming the formula.
