---
role: proof
locale: en
of_concept: linear-dependence-of-powers-of-linear-transformation
source_book: gtm031
source_chapter: "3"
source_section: "1"
---

Consider the subspaces $[1], [1, A], [1, A, A^2], [1, A, A^2, A^3], \ldots$ of $\mathfrak{L}$. Each is contained in the next, and their dimensions are bounded by $\dim \mathfrak{L} = n^2$. Hence the strictly increasing chain must terminate: there exists a smallest $m$ such that $\dim[1, A, \ldots, A^{m-1}] = \dim[1, A, \ldots, A^m]$, which implies $A^m \in [1, A, \ldots, A^{m-1}]$. Then $A^m = \mu_0 1 + \mu_1 A + \cdots + \mu_{m-1} A^{m-1}$ for some $\mu_i \in \Phi$. Multiplying by $A$ and using the algebra condition $\gamma(AB) = (\gamma A)B = A(\gamma B)$ gives $A^{m+1} = \mu_0 A + \mu_1 A^2 + \cdots + \mu_{m-1} A^m \in [1, A, \ldots, A^{m-1}]$. By induction, all higher powers $A^k$ ($k \geq m$) lie in the same subspace.
