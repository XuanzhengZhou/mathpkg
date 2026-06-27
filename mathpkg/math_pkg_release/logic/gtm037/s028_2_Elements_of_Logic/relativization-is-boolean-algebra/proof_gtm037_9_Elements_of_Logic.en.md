---
role: proof
locale: en
of_concept: relativization-is-boolean-algebra
source_book: gtm037
source_chapter: "9"
source_section: "Elements of Logic"
---

The verification is routine. One checks that the operations $+'$, $\cdot'$, and $-'\ '$ satisfy the Boolean algebra axioms on the set $A \upharpoonright a = \{x \in A : x \leq a\}$. The key points are: $0$ acts as the zero element since $0 \leq a$ and $0 +' x = 0 + x = x$ for $x \in A \upharpoonright a$; $a$ acts as the unit element since $x \cdot' a = x \cdot a = x$ for $x \leq a$; the modified complement $-'\ x = a \cdot -x$ satisfies $x +' (-' x) = x + (a \cdot -x) = (x + a) \cdot (x + -x) = a \cdot 1 = a$ and $x \cdot' (-' x) = x \cdot (a \cdot -x) = a \cdot (x \cdot -x) = a \cdot 0 = 0$. The remaining axioms (commutativity, associativity, distributivity, absorption) are inherited directly from $\mathfrak{A}$ and hold because $A \upharpoonright a$ is closed under $+$ and $\cdot$.
