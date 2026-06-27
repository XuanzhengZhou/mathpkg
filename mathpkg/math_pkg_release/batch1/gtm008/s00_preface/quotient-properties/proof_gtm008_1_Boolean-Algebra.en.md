---
role: proof
locale: en
of_concept: quotient-properties
source_book: gtm008
source_chapter: "1"
source_section: "Boolean Algebra"
---

**Proof.**

1. If $a/I = b/I$, then since $a(-a) + a(-a) = 0 \in I$, we have $a \in a/I$ and hence $a \in b/I$. Therefore $a(-b) + b(-a) \in I$. Conversely, if $a(-b) + b(-a) \in I$ and $x \in a/I$, then $a(-b), b(-a), x(-a), a(-x) \in I$ (by Theorem 1.42). Then $a(-b)x + b(-a)(-x) + x(-a)(-b) + a(-x)b \in I$, so $(x(-b) + b(-x))(a + -a) \in I$, giving $x(-b) + b(-x) \in I$, i.e., $x \in b/I$. Similarly, $x \in b/I \rightarrow x \in a/I$.

2-4. These follow from the fact that the symmetric difference relation is a congruence with respect to the Boolean operations, using the ideal properties.
