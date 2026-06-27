---
role: proof
locale: en
of_concept: cartans-criterion-for-solvability
source_book: gtm009
source_chapter: "II"
source_section: "4.3"
---
It suffices to prove that $[LL]$ is nilpotent (by Engel's Theorem), or equivalently that each $x \in [LL]$ is a nilpotent endomorphism (by Lemma 3.2). Apply the trace lemma with $A = [LL]$ and $B = L$, so $M = \{x \in \mathfrak{gl}(V) \mid [x, L] \subset [LL]\}$. Clearly $L \subset M$.

The hypothesis gives $\operatorname{Tr}(xy) = 0$ for all $x \in [LL]$, $y \in L$, but the lemma requires $\operatorname{Tr}(xy) = 0$ for all $x \in [LL]$, $y \in M$. To bridge this gap, let $[x, y]$ be a typical generator of $[LL]$ (with $x, y \in L$) and let $z \in M$. Then $\operatorname{Tr}([x, y]z) = \operatorname{Tr}(x[y, z]) = \operatorname{Tr}([y, z]x)$. By definition of $M$, $[y, z] \in [LL]$, so the right side is $0$ by the hypothesis. Since $\operatorname{Tr}$ is linear and the commutators span $[LL]$, this extends to all of $[LL]$.

Thus the trace lemma applies: every $x \in [LL]$ is nilpotent. By Engel's Theorem, $[LL]$ is nilpotent, and therefore $L$ is solvable.
