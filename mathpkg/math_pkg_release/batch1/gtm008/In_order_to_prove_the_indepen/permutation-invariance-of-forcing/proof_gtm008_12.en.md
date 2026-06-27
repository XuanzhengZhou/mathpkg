---
role: proof
locale: en
of_concept: permutation-invariance-of-forcing
source_book: gtm008
source_chapter: "12"
source_section: "12. The Independence of the AC"
---

The proof proceeds by transfinite induction on $	ext{Ord}(arphi)$.

Let $p \in \prod_{i \in \omega}^{w} P_i$ and $\pi$ be a permutation of $\omega$. The mapping $\pi$ acts on conditions by permuting coordinates:
$$\pi(p)(i) = p(\pi^{-1}(i))$$
and on formulas by permuting the indices of the predicate symbols $F_i$ appearing in them. The action on terms is defined analogously.

For atomic formulas, the result follows from the definition of the forcing relation for the weak product:
$$p \Vdash F_i(x) \iff (\exists q \leq p_i)\,[q \Vdash x = \check{a}]$$
where $p_i$ is the $i$-th coordinate of $p$. Under the permutation $\pi$, this becomes a condition about $F_{\pi(i)}$, which matches $\pi(arphi)$.

The inductive steps for propositional connectives ($\land, \lor, 
eg, ightarrow$) follow from the definition of the forcing relation and the induction hypothesis.

For the quantifier steps:
- $p \Vdash \exists x\, arphi(x)$ iff $(\exists t \in T)\,[p \Vdash arphi(t)]$. By induction hypothesis, $p \Vdash arphi(t) \leftrightarrow \pi(p) \Vdash \pi(arphi(t))$, and since $\pi$ maps terms to terms, we obtain the equivalence.
- $p \Vdash orall x\, arphi(x)$ iff $(orall t \in T)\,[p \Vdash arphi(t)]$. The same reasoning applies.

Thus by transfinite induction on the ordinal rank of formulas, the equivalence holds for all $arphi$.
