---
role: proof
locale: en
of_concept: prop-if-is-recurrent-on-but-if
source_book: gtm034
source_chapter: "6"
source_section: "013"
---

Proof: Nothing more is involved than a simple rephrasing of definitions. When $x \in A$, $P_x[A_0] = 1$, so that $H_A(x) = 1$, and when $x \in R - A$ the statement of P7 concerning $H_A(x)$ is the definition of $H_A(x)$. Since the events $B_n = \bigcup_{k=n}^{\infty} A_k$ form a monotone sequence,

$$P_x \left[ \bigcap_{n=1}^{\infty} \bigcup_{k=n}^{\infty} A_k \right] = \lim_{n \to \infty} P_x[B_n].$$

Here $B_n$ is the event of a visit to the set $A$ at or after time $n$, but in a finite time. It follows from the probability interpretation of $B_n$ that

$$P_x[B_n] = \sum_{y \in R} P_n(x,y) H_A(y),$$

and the definition of $h_A(x)$ in P4 completes the proof of P7.

The stage is now set for the last step—the somewhat delicate argument required to show that any set $A$ is either visited infinitely often with probability one or with probability zero. As one might hope, this dichotomy corresponds in a natural way to the classification in D2.
