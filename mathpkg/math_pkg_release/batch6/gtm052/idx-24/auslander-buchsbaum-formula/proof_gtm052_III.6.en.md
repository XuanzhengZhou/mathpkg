---
role: proof
locale: en
of_concept: auslander-buchsbaum-formula
source_book: gtm052
source_chapter: "III"
source_section: "6"
---

See Matsumura [2, p. 113, Ex. 4] or Serre [11, IVD, Prop. 21].

The proof proceeds by induction on $\operatorname{pd} M$. If $\operatorname{pd} M = 0$, then $M$ is projective, hence free over the local ring $A$, so $\operatorname{depth} M = \dim A = n$, giving the formula. If $\operatorname{pd} M > 0$, choose a minimal free resolution and consider the first syzygy module $M_1$ of $M$. One shows $\operatorname{pd} M_1 = \operatorname{pd} M - 1$ and $\operatorname{depth} M_1 = \operatorname{depth} M + 1$ (using the fact that a regular sequence for $M$ lifts to one for $M_1$). The induction hypothesis applied to $M_1$ then yields the result.
