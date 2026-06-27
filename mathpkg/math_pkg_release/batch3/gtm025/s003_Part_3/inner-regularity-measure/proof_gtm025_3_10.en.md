---
role: proof
locale: en
of_concept: inner-regularity-measure
source_book: gtm025
source_chapter: "3"
source_section: "10"
---

**Proof.** (I) Suppose $\iota(A) < \infty$. Given $\varepsilon > 0$, use (9.24) to select an open set $V$ with $A \subset V$ and $\iota(V) < \iota(A) + \varepsilon$. Use (9.24) again to find a compact $E \subset V$ with $\iota(V \cap E') < \varepsilon/2$. Then choose open $W$ with $V \cap A' \subset W \subset V$ and $\iota(W) < \varepsilon/2$. The set $F = E \cap W'$ is compact, $F \subset A$, and $\iota(A \cap F') < \varepsilon$.

(II) If $\iota(A) = \infty$, write $A = \bigcup A_n$ with $\iota(A_n) < \infty$ and apply (I) to each $A_n$. $\square$
