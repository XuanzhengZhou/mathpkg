---
role: proof
locale: en
of_concept: multiple-derivation-andre-plane
source_book: gtm006
source_chapter: "X"
source_section: "3. Desarguesian Planes"
---

We prove some auxiliary results first.

**(a)** If $a \neq 0$ in $K$, then $x^{q-1} = a$ has $0$ or $q-1$ solutions.

*Proof.* If both $g$ and $h$ in $K$ are solutions, that is $g^{q-1} = h^{q-1} = a$, then clearly $(gh^{-1})^{q-1} = 1$. But since $K^*$ is a cyclic group of order $q^2 - 1$, it has a unique cyclic subgroup of order $q - 1$, and so $x^{q-1} = 1$ has $q-1$ solutions; it is now easy to see that each of the elements $gx$ satisfies $(gx)^{q-1} = a$, and there are no other solutions.

**(b)** If $a \neq 0$ in $K$, and $b, c$ are elements of $F$, then the equation $ax^{q} + bx + c = 0$ has either $0$, $1$, or $q$ solutions in $K$, and if it has $q$ solutions then $a \in F$.

The main proof then analyzes the set of points in $\mathcal{A}$ satisfying an equation derived from the derivation structure and shows that these points form an affine plane of order $q$. By identifying the line at infinity structure and the multiplication rule in the coordinatizing ternary ring, one verifies that the resulting plane satisfies the definition of an André plane. The case where one of the $t_i$ equals $1$ but some element of $F^*$ is not a $t_j$ is handled by finding a collineation that permutes the derivation sets appropriately. $\square$
