---
role: proof
locale: en
of_concept: exponential-lower-bound-for-return-probabilities
source_book: gtm034
source_chapter: "VI"
source_section: "32"
---

By recurrence, choose $a_1 > 0$, $a_2 > 0$ with $P(0,a_1) > 0$, $P(0,-a_2) > 0$. For large $n$,
$$P[S_1 = a_1, S_{n-1} - S_1 = a_2 - a_1, S_n = 0] = P(0,a_1) P[S_{n-2} = a_2 - a_1] P(0,-a_2) \geq (1-\epsilon)^n.$$

Subject $X_2, \ldots, X_{n-1}$ to all $n-2$ cyclic permutations. For each permutation $p$, form the polygonal line $L(p)$ connecting $(1,a_1), (2, a_1+X_{p(2)}), \ldots, (n-1,a_2)$. At least one permutation yields $L(p)$ lying entirely above its chord. Each permutation is equally likely. For the identity permutation $e$, $P_0[E_n(e)] \geq (1-\epsilon)^n/(n-2)$. Since $E_n(e)$ implies first return at time $n$, $F_n \geq (1-\epsilon)^n/(n-2)$.
