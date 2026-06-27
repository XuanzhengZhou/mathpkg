---
role: proof
locale: en
of_concept: equal-transcendence-degree-isomorphism
source_book: gtm028
source_chapter: "II. Elements of Field Theory"
source_section: "§12. Transcendental Extensions"
---

We use the notations of the proof of the preceding theorem. Let $L' = \{x'_1, x'_2, \dots, x'_n\}$ be a transcendence basis of $R'/k$, and let $L = \{x_1, x_2, \dots, x_n\}$ be the set of preimages chosen in $R$ such that $x'_i = x_i\tau$ for each $i$. As shown in Theorem 28, $L$ is a transcendence set of cardinality $n$.

Since $\operatorname{tr.d.} R/k = n$, the set $L$ must itself be a transcendence basis of $R/k$. In particular, every element of $R$ is algebraic over $k(L)$.

Now suppose $\tau$ is not injective, and let $a \in R$ be a nonzero element with $a\tau = 0$. Since $a$ is algebraic over $k(L)$, there is a minimal polynomial relation expressing $a$ in terms of $x_1, \dots, x_n$. Applying $\tau$ to this relation and using that $a\tau = 0$ yields a polynomial relation among $x'_1, \dots, x'_n$, contradicting their algebraic independence unless the relation is trivial. Hence no such nonzero $a$ can exist, and $\tau$ is injective, thus an isomorphism.

**Remark.** If $R$ is a field, then Theorem 29 is trivial and is true without any condition on the transcendence degrees, since a field does not admit proper homomorphisms (that is, homomorphisms which are not isomorphisms).
