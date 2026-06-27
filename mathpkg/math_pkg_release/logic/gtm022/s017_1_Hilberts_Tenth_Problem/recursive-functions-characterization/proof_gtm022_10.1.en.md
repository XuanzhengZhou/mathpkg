---
role: proof
locale: en
of_concept: recursive-functions-characterization
source_book: gtm022
source_chapter: "10"
source_section: "1"
---

For a detailed proof of Theorem 1.2, we refer the reader to [3]. Other accounts of the subject may be found, for example, in [6], [10] or [13].

The proof proceeds by showing two inclusions:

1. Every function obtainable from the initial functions $I$ by finite iterations of composition, primitive recursion, and minimalisation is recursive (i.e., Turing-computable). This direction is straightforward: one constructs a Turing machine for each initial function, and then shows that the operations of composition, primitive recursion, and minimalisation preserve Turing-computability.

2. Every recursive function can be obtained from $I$ by finite iterations of the operations. This is the deep direction. Given a Turing machine $T_f$ computing $f$, one encodes its computation history (instantaneous descriptions) as natural numbers and expresses the step-by-step transition relation using primitive recursive functions, ultimately exhibiting $f$ as built from $I$ via the permitted operations.

Together, the two inclusions establish that the set of recursive functions coincides with the closure of $I$ under composition, primitive recursion, and minimalisation.
