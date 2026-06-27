---
role: introduce
locale: en
content_hash: ""
written_against: ""
---

Rice's theorem is a fundamental result in recursion theory stating that any non-trivial property of partial recursive functions is undecidable from the index alone. More precisely, if $F$ is any non-empty proper subset of the unary partial recursive functions, then the index set $\{e : \varphi^1_e \in F\}$ is not recursive. This means no algorithm can determine, given a Turing machine (or partial recursive function index), whether the function it computes has a specific semantic property.

The theorem has far-reaching consequences: it implies that essentially all interesting questions about the behavior of programs (whether a function is constant, whether a value is in its range, whether two programs compute the same function) are algorithmically undecidable. Rice's theorem is proved via a simple diagonalization argument using the fixed-point theorem.
