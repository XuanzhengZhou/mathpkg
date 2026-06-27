---
role: proof
locale: en
of_concept: "recursive-iff-diophantine"
source_book: gtm022
source_chapter: "X"
source_section: "1"
---
Proof. (Sketch) The easy direction: if $f$ is diophantine, its graph is existentially defined by a polynomial equation, and the value can be computed by search (minimalisation), making $f$ recursive.

The hard direction (Matiyasevich-Robinson-Davis-Putnam): show that every recursive function is diophantine. Using the characterization in Theorem 1.2, it suffices to show: (1) the initial functions are diophantine, (2) diophantine functions are closed under composition, primitive recursion, and minimalisation. The critical step is closure under primitive recursion, which requires the sequence number function and bounded quantifiers. Matiyasevich (1970) completed the proof by showing the Fibonacci sequence satisfies a diophantine relation with exponential growth, allowing encoding of arbitrary sequences. $\square$
