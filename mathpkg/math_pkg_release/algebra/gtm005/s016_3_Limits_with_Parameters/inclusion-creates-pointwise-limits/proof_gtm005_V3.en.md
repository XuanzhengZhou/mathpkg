---
role: proof
locale: en
of_concept: inclusion-creates-pointwise-limits
source_book: gtm005
source_chapter: "V"
source_section: "3. Limits with Parameters"
---

This theorem follows from the pointwise limits theorem. Given a diagram $D : J \rightarrow X^P$, composing with $i^*$ yields $i^* D : J \rightarrow X^{|P|}$, which is simply the collection of diagrams $E_p D : J \rightarrow X$ for each $p \in P$. If this has a limit in $X^{|P|}$, then for each object $p \in P$ the diagram $E_p D$ has a limit in $X$. By the pointwise limits theorem, these limits assemble into a limit of $D$ in $X^P$. Moreover, $i^*$ preserves this limit by construction, and the universal property follows from the universal property of each pointwise limit. Hence $i^*$ creates the limit.
