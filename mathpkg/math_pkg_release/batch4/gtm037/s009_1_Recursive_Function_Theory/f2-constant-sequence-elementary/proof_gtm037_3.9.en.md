---
role: proof
locale: en
of_concept: f2-constant-sequence-elementary
source_book: gtm037
source_chapter: "3"
source_section: "9"
---

$f_2 x = \prod_{i \leq x} p_i^2$. Since $p_i^2$ for each $i \leq x$ is a prime squared, this is the G\"{o}del number of a sequence of length $x+1$ where each entry is $1$ (because the exponent $2 = 1 + 1$ encodes the value $1$ under the encoding $gh = \prod p_i^{h_i + 1}$). Hence $f_2 x = g 1^{(x+1)}$. The function $f_2$ is elementary because it is a finite product of $p_i^2$, which is defined by bounded iteration.
