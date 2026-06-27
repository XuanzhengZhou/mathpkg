---
role: introduce
locale: en
content_hash: ""
written_against: ""
---

A primitive Skolem expansion of a first-order language $L$ adds, for each existential formula $\exists v_i \varphi$, a new operation symbol $S_{\exists v_i \varphi}$ whose arity equals the number of free variables in the existential formula. These Skolem function symbols are intended to serve as "witness selectors": they pick, for each assignment to the free variables, a value that satisfies the existential claim whenever one exists.

A full Skolem expansion is obtained by iterating this process $\omega$ times, adding Skolem functions for existential formulas at each stage. The union of all stages yields a language in which every existential formula has an associated Skolem function symbol.

In the effectivized setting, the mapping from formula indices to the Gödel numbers of the corresponding Skolem symbols is required to be partial recursive, ensuring that the expansion is computationally well-behaved.
