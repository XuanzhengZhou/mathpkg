---
role: proof
locale: en
of_concept: transfinite-induction
source_book: gtm053
source_chapter: "1"
source_section: "9"
---

Suppose $C$ does not contain all ordinals. Then there exists a least ordinal not in $C$. This ordinal cannot be the empty set by condition (a). It cannot be a limit ordinal, because by condition (c), if all smaller ordinals are in $C$, their union (which is the limit ordinal itself) is in $C$. And it cannot be any other ordinal (i.e., a successor ordinal), because by condition (b), if $\alpha \in C$, then $\alpha + 1 \in C$. Thus no least counterexample exists, and $C$ must contain all ordinals.

In concrete applications, the verifications of (a) and (c) are often trivial and are omitted.
