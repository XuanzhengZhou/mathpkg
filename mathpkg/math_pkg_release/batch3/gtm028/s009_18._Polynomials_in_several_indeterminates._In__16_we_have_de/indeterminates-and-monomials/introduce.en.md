---
role: introduce
locale: en
content_hash: ""
written_against: ""
---

## Indeterminates and Monomials

Given the polynomial ring $S = R[X_1, \dots, X_n]$ defined via finitely-supported mappings, the element $X_\nu$ (for $\nu = 1, \dots, n$) is defined as the mapping that assigns the identity $1_R$ to the $n$-tuple $(j^\nu) = (0, \dots, 1, \dots, 0)$ (with $1$ in position $\nu$) and $0$ to every other $n$-tuple. 

A **monomial** is an element of the form $a_{(i)} X_1^{i_1} X_2^{i_2} \cdots X_n^{i_n}$, which as a mapping associates the coefficient $a_{(i)} \in R$ to the $n$-tuple $(i) = (i_1, \dots, i_n)$ and $0$ to all others. Every polynomial $f \in S$ is a finite sum of monomials, and $f = 0$ if and only if all coefficients $a_{(i)} = 0$.
