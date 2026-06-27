---
role: proof
locale: en
of_concept: orientation-by-direct-decomposition
source_book: gtm023
source_chapter: "Chapter IV"
source_section: "§8. Oriented vector spaces"
---

Let $\bar{a}_i$ and $\bar{b}_j$ be two other positive bases of $E_1$ and $E_2$. Define linear transformations $\varphi: E_1 \to E_1$ and $\psi: E_2 \to E_2$ by $\varphi a_i = \bar{a}_i$ and $\psi b_j = \bar{b}_j$. Since both $a_i$ and $\bar{a}_i$ are positive bases of $E_1$, we have $\det \varphi > 0$; similarly $\det \psi > 0$.

Now the transformation from the concatenated basis $(a_1, \ldots, a_p, b_1, \ldots, b_q)$ to $(\bar{a}_1, \ldots, \bar{a}_p, \bar{b}_1, \ldots, \bar{b}_q)$ is given by the block diagonal matrix whose blocks are $\varphi$ and $\psi$. Its determinant is $\det \varphi \cdot \det \psi > 0$, so both concatenated bases determine the same orientation. Hence the induced orientation on $E$ is well-defined.
