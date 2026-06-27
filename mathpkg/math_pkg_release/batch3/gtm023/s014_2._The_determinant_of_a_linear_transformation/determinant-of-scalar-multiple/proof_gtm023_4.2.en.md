---
role: proof
locale: en
of_concept: determinant-of-scalar-multiple
source_book: gtm023
source_chapter: "4"
source_section: "2"
---

If $\varphi = \lambda \iota$, then for any non-trivial determinant function $\Delta$, we have by Definition 4.4:

$$\Delta(\varphi x_1, \ldots, \varphi x_n) = \det \varphi \, \Delta(x_1, \ldots, x_n).$$

The left-hand side evaluates to $\Delta(\lambda x_1, \ldots, \lambda x_n)$. Since $\Delta$ is multilinear, factoring out $\lambda$ from each argument yields $\lambda^n \Delta(x_1, \ldots, x_n)$. Thus

$$\lambda^n \Delta(x_1, \ldots, x_n) = \det \varphi \, \Delta(x_1, \ldots, x_n).$$

Since $\Delta \neq 0$, we can cancel $\Delta(x_1, \ldots, x_n) \neq 0$ for a suitably chosen tuple, obtaining $\det(\lambda \iota) = \lambda^n$. Setting $\lambda = 1$ gives $\det \iota = 1$, and setting $\lambda = 0$ gives $\det 0 = 0$.
