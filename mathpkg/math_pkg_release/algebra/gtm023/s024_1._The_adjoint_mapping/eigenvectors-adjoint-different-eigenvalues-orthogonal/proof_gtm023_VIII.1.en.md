---
role: proof
locale: en
of_concept: eigenvectors-adjoint-different-eigenvalues-orthogonal
source_book: gtm023
source_chapter: "VIII"
source_section: "§1. The adjoint mapping"
---

From the eigenvalue equations $\varphi e = \lambda e$ and $\tilde{\varphi} \tilde{e} = \tilde{\lambda} \tilde{e}$, we compute using the defining relation (8.2):

$$(\varphi e, \tilde{e}) = (\lambda e, \tilde{e}) = \lambda (e, \tilde{e}).$$

On the other hand,

$$(\varphi e, \tilde{e}) = (e, \tilde{\varphi} \tilde{e}) = (e, \tilde{\lambda} \tilde{e}) = \tilde{\lambda} (e, \tilde{e}).$$

Equating the two expressions:

$$\lambda (e, \tilde{e}) = \tilde{\lambda} (e, \tilde{e}),$$

which yields $(\tilde{\lambda} - \lambda)(e, \tilde{e}) = 0$. If $\tilde{\lambda} \neq \lambda$, then $(e, \tilde{e}) = 0$.
