---
role: introduce
locale: en
content_hash: ""
written_against: ""
---

Theorem 3.8 establishes that not every number-theoretic function is recursive. Although this follows from cardinality considerations (there are $\aleph_0$ recursive functions but $2^{\aleph_0}$ number-theoretic functions), one can also give an explicit nonrecursive function via a diagonal argument. Enumerate all unary recursive functions as $f_0, f_1, \ldots$ and define $g(m) = f_m(m) + 1$. Then $g$ differs from every $f_m$ at the argument $m$, so $g$ cannot appear in the enumeration and is therefore not recursive.
