---
role: proof
locale: en
of_concept: boolean-algebra-transport-of-structure
source_book: gtm037
source_chapter: "9"
source_section: "Elements of Logic"
---

Let $\mathfrak{A} = \langle A, +, \cdot, -, 0, 1 \rangle$. Define the operations of $\mathfrak{B}$ on $B$ as follows: for any $b, c \in B$,

$$b +' c = f(f^{-1}(b) + f^{-1}(c)),$$
$$b \cdot' c = f(f^{-1}(b) \cdot f^{-1}(c)),$$
$$-'\ b = f(-f^{-1}(b)),$$
$$0' = f(0), \quad 1' = f(1).$$

Set $\mathfrak{B} = \langle B, +', \cdot', -', 0', 1' \rangle$. The verification that $\mathfrak{B}$ satisfies the Boolean algebra axioms is routine, as each axiom for $\mathfrak{B}$ translates via $f^{-1}$ to the corresponding axiom in $\mathfrak{A}$. Moreover, $f$ is a homomorphism by construction: $f(x + y) = f(f^{-1}(f(x)) + f^{-1}(f(y))) = f(x) +' f(y)$, and similarly for the other operations. Since $f$ is bijective, it is an isomorphism.
