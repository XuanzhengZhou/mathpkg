---
role: proof
locale: en
of_concept: connected-elations-same-prime-order
source_book: gtm006
source_chapter: "XIII"
source_section: "3"
---

We first note, although the observation is unnecessary for the proof, that the axes of $\alpha$ and $\beta$ must also belong to $\mathcal{S}$.

Since $A$ and $B$ are in the non-trivial connected set $\mathcal{S}$, they are connected by a sequence of elation flags: there exist elation flags $F_1, F_2, \dots, F_k$ in $\mathcal{S}$ such that $A$ is the centre of $F_1$, $B$ is the centre of $F_k$, and for each $i = 1, 2, \dots, k-1$, the flags $F_i$ and $F_{i+1}$ have an element in common (they share either a common centre or a common axis).

By Theorem 4.14 and its dual, any two elations whose centre-axis flags have an element in common have the same prime order. Applying this successively along the chain:
- The elation corresponding to $F_1$ (which is $\alpha$, with centre $A$) has the same prime order as the elation corresponding to $F_2$,
- The elation corresponding to $F_2$ has the same prime order as the elation corresponding to $F_3$,
- And so on, until we reach the elation corresponding to $F_k$ (which is $\beta$, with centre $B$).

Thus repeated use of Theorem 4.14 and its dual proves that $\alpha$ and $\beta$ have the same prime order.
