---
role: proof
locale: en
of_concept: monad-in-a-preorder
source_book: gtm005
source_chapter: "VI. Monads and Algebras"
source_section: "1. Monads in a Category"
---

Consider a preorder $P$ viewed as a thin category: for any two objects $x, y \in P$, there is at most one morphism $x \to y$, which exists exactly when $x \leq y$.

A functor $T: P \to P$ is just a function on objects that preserves the order relation: $x \leq y$ implies $Tx \leq Ty$ (monotonicity).

Natural transformations $\eta: I_P \to T$ and $\mu: T^2 \to T$ consist of families of arrows $\eta_x: x \to Tx$ and $\mu_x: T^2 x \to Tx$. Since $P$ is a thin category, such natural transformations exist precisely when $x \leq Tx$ and $T^2 x \leq Tx$ for all $x \in P$; naturality is automatic.

The monad diagrams (2) involve parallel pairs of arrows in $P$. In a thin category, any two parallel arrows are equal, so these diagrams commute automatically once the arrows exist.

Therefore, a monad in $P$ is precisely a monotonic function $T: P \to P$ satisfying
$$
x \leq Tx, \quad T(Tx) \leq Tx \qquad \text{for all } x \in P.
$$

Since $T$ is monotone, $x \leq Tx$ implies $Tx \leq T(Tx)$. Together with $T(Tx) \leq Tx$, this gives $Tx = T(Tx)$ up to equivalence (or exactly $Tx \cong T(Tx)$ in the preorder, meaning equality if $P$ is a poset). Thus a monad in a poset is exactly a closure operator.
