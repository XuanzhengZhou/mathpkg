---
role: proof
locale: en
of_concept: f2m-godel-number-property
source_book: gtm037
source_chapter: "4"
source_section: "1"
---

The claim follows from the definition of $f_2^m$ by induction on $m$. For $m = 1$, $f_2^1 x = \text{Cat}(2, f_1 x)$ encodes the word $0 \cdot 1^{(x+1)}$. For the inductive step, $f_2^{m+1}(x_0, \ldots, x_m) = \text{Cat}(f_2^m(x_0, \ldots, x_{m-1}), f_2^1 x_m)$ concatenates the encoding of $0 \cdot 1^{(x_0+1)} \cdot \ldots \cdot 0 \cdot 1^{(x_{m-1}+1)}$ with the encoding of $0 \cdot 1^{(x_m+1)}$, yielding the Gödel number of

$$0 \cdot 1^{(x_0+1)} \cdot \ldots \cdot 0 \cdot 1^{(x_m+1)}.$$
