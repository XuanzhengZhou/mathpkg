---
role: proof
locale: en
of_concept: determinant-representation
source_book: gtm023
source_chapter: "IV"
source_section: "§1. Determinant functions"
---

Choose a basis $a_1, \ldots, a_n$ of $E$ such that $\Delta(a_1, \ldots, a_n) = 1$ (this is possible since $\Delta \neq 0$, so we can scale one basis vector appropriately). Set $b = \varphi(a_1, \ldots, a_n)$ and define $\psi: E^n \to F$ by
$$\psi(x_1, \ldots, x_n) = \Delta(x_1, \ldots, x_n) \cdot b.$$
Then $\psi$ is $n$-linear and skew symmetric. On the chosen basis,
$$\psi(a_1, \ldots, a_n) = \Delta(a_1, \ldots, a_n) \cdot b = 1 \cdot b = \varphi(a_1, \ldots, a_n).$$
Since both $\varphi$ and $\psi$ are skew symmetric $n$-linear maps agreeing on a basis, Proposition II implies $\varphi = \psi$. The vector $b$ is uniquely determined by (4.4) because if $\Delta(x_1,\ldots,x_n) \cdot b = \Delta(x_1,\ldots,x_n) \cdot b'$ for all $x_i$, choosing arguments with $\Delta \neq 0$ yields $b = b'$.
