---
role: introduce
locale: en
content_hash: ""
written_against: ""
---

This is a well-known algebraic fact in linear algebra: the first-order term in the expansion of $\det(E + At)$ as $t \to 0$ is $t$ times the trace of $A$. The constant term is $1$ (the determinant of the identity), and all higher-order terms are $O(t^2)$. The proof follows by direct expansion of the determinant: one obtains $1$ and $n$ terms linear in $t$ (each coming from a diagonal element $a_{ii}$), while the remaining terms involve products of at least two off-diagonal entries and are therefore $O(t^2)$.
