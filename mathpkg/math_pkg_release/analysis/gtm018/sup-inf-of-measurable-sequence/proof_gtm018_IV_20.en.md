---
role: proof
locale: en
of_concept: sup-inf-of-measurable-sequence
source_book: gtm018
source_chapter: "IV"
source_section: "20"
---
**Proof.** Reduce to finite valued case. The equation
$$\{x : g(x) < c\} = \bigcup_{n=1}^{\infty} \{x : f_n(x) < c\}$$
implies the measurability of $g$. For $h$, use $h(x) = -\inf\{-f_n(x): n=1,2,\dots\}$. The measurability of $\limsup$ and $\liminf$ follows from
$$f^*(x) = \inf_{n \geq 1} \sup_{m \geq n} f_m(x), \quad f_*(x) = \sup_{n \geq 1} \inf_{m \geq n} f_m(x).$$
