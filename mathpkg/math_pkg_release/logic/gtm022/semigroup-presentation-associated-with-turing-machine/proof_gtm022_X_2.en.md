---
role: proof
locale: en
of_concept: "semigroup-presentation-associated-with-turing-machine"
source_book: gtm022
source_chapter: "X"
source_section: "2"
---
Proof. Associate with $M$ a finite semigroup presentation whose relations simulate the operation of $M$ on instantaneous descriptions. Special words correspond to configurations of $M$, and the relations are: (a) $q_i s_j \sim s_j q_t$ for 'print' instructions, (b) relations simulating left and right moves, (c) relations for undefined transitions. Lemma 2.8 shows that two special words are equivalent iff there is a path of forward steps from one to the other. The word problem for this presentation would decide the halting problem for $M$, which is impossible by the choice of $E$. $\square$
