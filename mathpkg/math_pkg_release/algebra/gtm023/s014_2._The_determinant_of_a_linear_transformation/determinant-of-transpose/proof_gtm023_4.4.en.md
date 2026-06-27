---
role: proof
locale: en
of_concept: determinant-of-transpose
source_book: gtm023
source_chapter: "4"
source_section: "4"
---

Let $\Delta^*$ and $\Delta$ be dual determinant functions in $E^*$ and $E$ respectively, so that by (4.26),

$$\Delta^*(x^{*1}, \ldots, x^{*n}) \Delta(x_1, \ldots, x_n) = \det(\langle x^{*i}, x_j \rangle).$$

Replacing $x_j$ by $\varphi x_j$ gives

$$\Delta^*(x^{*1}, \ldots, x^{*n}) \Delta(\varphi x_1, \ldots, \varphi x_n) = \det(\langle x^{*i}, \varphi x_j \rangle).$$

Since $\langle \varphi^* x^{*i}, x_j \rangle = \langle x^{*i}, \varphi x_j \rangle$, the right-hand side also equals $\det(\langle \varphi^* x^{*i}, x_j \rangle)$. By the same duality relation applied to the arguments $\varphi^* x^{*i}$ and $x_j$, we obtain

$$\Delta^*(\varphi^* x^{*1}, \ldots, \varphi^* x^{*n}) \Delta(x_1, \ldots, x_n) = \Delta^*(x^{*1}, \ldots, x^{*n}) \Delta(\varphi x_1, \ldots, \varphi x_n).$$

But $\Delta^*(\varphi^* x^{*1}, \ldots, \varphi^* x^{*n}) = \det \varphi^* \cdot \Delta^*(x^{*1}, \ldots, x^{*n})$ and $\Delta(\varphi x_1, \ldots, \varphi x_n) = \det \varphi \cdot \Delta(x_1, \ldots, x_n)$. Substituting,

$$(\det \varphi^* - \det \varphi) \, \Delta^*(x^{*1}, \ldots, x^{*n}) \, \Delta(x_1, \ldots, x_n) = 0,$$

whence $\det \varphi^* = \det \varphi$. For matrices, let $M(\varphi) = A$, then $\det A^* = \det M(\varphi)^* = \det M(\varphi^*) = \det \varphi^* = \det \varphi = \det A$.
