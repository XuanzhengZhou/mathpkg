---
role: proof
locale: en
of_concept: determinant-as-row-function
source_book: gtm023
source_chapter: "4"
source_section: "3"
---

Let $\varphi$ be the linear transformation of $\Gamma^n$ whose matrix with respect to the standard basis $e_1, \ldots, e_n$ is $A$, so that $\varphi e_v = a_v$ (the $v$-th row). Let $\Delta$ be the determinant function in $\Gamma^n$ with $\Delta(e_1, \ldots, e_n) = 1$. Then

$$\Delta(a_1, \ldots, a_n) = \Delta(\varphi e_1, \ldots, \varphi e_n) = \det \varphi \, \Delta(e_1, \ldots, e_n) = \det \varphi,$$

and since $\det \varphi = \det M(\varphi) = \det A$, we have $\det A = \Delta(a_1, \ldots, a_n)$. The four properties now follow directly from the corresponding properties of the determinant function $\Delta$: (1) multilinearity of $\Delta$, (2) alternating property, (3) the fact that $\Delta(\ldots, a_i + \lambda a_j, \ldots) = \Delta(\ldots, a_i, \ldots) + \lambda \Delta(\ldots, a_j, \ldots)$ with the second term vanishing due to the alternating property, and (4) the characterization that $\Delta(a_1, \ldots, a_n) \neq 0$ iff the vectors are linearly independent. The column version follows by the same argument applied to $\det A = \Delta(b^1, \ldots, b^n)$ where $b^v$ are the column vectors.
