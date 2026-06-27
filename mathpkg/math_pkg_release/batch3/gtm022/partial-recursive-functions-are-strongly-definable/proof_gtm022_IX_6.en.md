---
role: proof
locale: en
of_concept: "partial-recursive-functions-are-strongly-definable"
source_book: gtm022
source_chapter: "IX"
source_section: "6"
---
Proof. The proof constructs, for any Turing machine $M$, formulas in the language of arithmetic that code the computation of $M$. Using the sequence number function, one can express: there exists a sequence of numbers $x$ (coding the entire computation) such that $x$ codes a valid computation of $M$ on input $n$ with output $m$. The definability of the step-by-step transition function of $M$ is shown using the formulas $M_{\alpha,\beta}$ for each quadruple of $M$. $\square$
