---
role: proof
locale: en
of_concept: exponential-lower-bound-for-return-probability
source_book: gtm034
source_chapter: "VII"
source_section: "32"
---

By recurrence, choose $a_1 > 0$, $a_2 > 0$ with $P(0,a_1) > 0$, $P(0,-a_2) > 0$. Then $P[S_1 = a_1, S_{n-1} - S_1 = a_2 - a_1, S_n = 0] \geq (1-\epsilon)^n$ for large $n$, since this equals $P(0,a_1)P[S_{n-2} = a_2 - a_1]P(0,-a_2)$. Consider all $n-2$ cyclic permutations of $X_2,\ldots,X_{n-1}$. For each permutation $p$, form polygonal line $L(p)$ connecting $(1,a_1)$ to $(n-1,a_2)$. By geometry, at least one permutation yields a polygon lying entirely above its chord. If $e$ is the identity and $E_n(e)$ the event $X_1=a_1$, $X_n=-a_2$, and $L(e)$ above its chord, then $P_0[E_n(e)] \geq (1-\epsilon)^n/(n-2)$. The event $E_n(e)$ implies first return at time $n$, so $F_n \geq (1-\epsilon)^n/(n-2)$.
