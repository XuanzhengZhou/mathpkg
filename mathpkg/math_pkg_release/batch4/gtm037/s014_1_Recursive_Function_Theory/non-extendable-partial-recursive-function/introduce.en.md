---
role: introduce
locale: en
content_hash: ""
written_against: ""
---

Not every partial recursive function can be extended to a total recursive function. Theorem 5.7 constructs a concrete counterexample using Gödel numbering of Turing machines: the function returns $0$ on non-machine indices, and $V(\mu u((x,x,u)\in T_1))+1$ on machine indices when the computation halts, and is undefined otherwise. The proof uses the undecidability of the halting problem to show that any total extension would contradict the unsolvability results established earlier.
