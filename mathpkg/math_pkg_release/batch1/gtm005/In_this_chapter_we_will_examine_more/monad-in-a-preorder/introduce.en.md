---
role: introduce
locale: en
content_hash: ""
written_against: ""
---

When specialized to a preorder viewed as a thin category, the definition of a monad simplifies dramatically. A functor $T: P \to P$ is just a monotone function, and the natural transformations $\eta$ and $\mu$ exist precisely when $x \leq Tx$ and $T(Tx) \leq Tx$ for all $x$. The commutative diagrams are automatically satisfied since in any preorder there is at most one arrow between two objects. Thus a monad in a preorder is exactly a closure operator: a monotone, inflationary ($x \leq Tx$), and idempotent ($T(Tx) \leq Tx$) function.
