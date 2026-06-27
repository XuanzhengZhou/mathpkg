---
role: proof
locale: en
of_concept: determinant-regularity-condition
source_book: gtm023
source_chapter: "4"
source_section: "2"
---

Let $e_1, \ldots, e_n$ be a basis of $E$ and let $\Delta \neq 0$ be a determinant function. From Definition 4.4,

$$\Delta(\varphi e_1, \ldots, \varphi e_n) = \det \varphi \, \Delta(e_1, \ldots, e_n). \tag{4.9}$$

If $\varphi$ is regular, then $\varphi e_1, \ldots, \varphi e_n$ are linearly independent, so $\Delta(\varphi e_1, \ldots, \varphi e_n) \neq 0$. Since $\Delta(e_1, \ldots, e_n) \neq 0$, equation (4.9) gives $\det \varphi \neq 0$.

Conversely, assume $\det \varphi \neq 0$. Then from (4.9) we obtain $\Delta(\varphi e_1, \ldots, \varphi e_n) \neq 0$, which implies the vectors $\varphi e_1, \ldots, \varphi e_n$ are linearly independent. Hence the image of a basis spans an $n$-dimensional subspace, which must be all of $E$; therefore $\varphi$ is regular.
