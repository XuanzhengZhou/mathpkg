---
role: proof
locale: en
of_concept: recursive-functions-strongly-definable
source_book: gtm022
source_chapter: "IX"
source_section: "6"
---

The Turing machine's step-by-step behavior is encoded using the sequence number function. For each quadruple of $M$, a formula $M_{\alpha,\beta}(x,y,z)$ describes one computation step. A formula $\psi(u,v;x,y,z)$ expresses that $x$ codes the $y$-th configuration of the computation on input $u$ with output $z$ at position $y$, with the computation having length $v$. The function computed is then extracted by existential quantification over computation codes.
