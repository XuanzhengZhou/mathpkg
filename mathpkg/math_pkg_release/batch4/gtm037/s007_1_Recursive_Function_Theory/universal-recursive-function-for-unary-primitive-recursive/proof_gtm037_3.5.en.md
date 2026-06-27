---
role: proof
locale: en
of_concept: universal-recursive-function-for-unary-primitive-recursive
source_book: gtm037
source_chapter: "3"
source_section: "3.1"
---

We first define an auxiliary binary function $h$ by a kind of recursion which is not primitive recursion, and afterwards we will show that $h$ is actually general recursive. We think of a number $x$ as coding information about an associated primitive recursive function $f$: $(x$ encodes the construction tree of $f$ from the initial functions via composition and primitive recursion).

[*Note: The proof is truncated in the source material. The continuation would define $h(x, n)$ to evaluate the primitive recursive function coded by $x$ on input $n$, showing that this evaluation function is itself general recursive by using a course-of-values recursion or similar technique that goes beyond primitive recursion but remains within the general recursive functions. The function $h$ then serves as the required universal function.*]
