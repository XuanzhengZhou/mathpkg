---
role: introduce
locale: en
content_hash: ""
written_against: ""
---

Kleene's recursion theorem is a fundamental fixed-point result in recursion theory. It states that for any partial recursive function $f$ of $m \geq 2$ arguments, there exists an index $e$ such that the $(m-1)$-ary partial recursive function $\varphi^{m-1}_e$ computed by the $e$-th Turing machine coincides with $f$ applied to its own index $e$ together with the remaining arguments. This theorem underpins many diagonalization arguments and is the basis for Rice's theorem and the unsolvability of the halting problem.

The theorem justifies self-referential constructions in computability theory: one may define a partial recursive function in terms of its own index, and the recursion theorem guarantees the existence of such an index. It is often used to prove that certain sets of indices are non-recursive.
