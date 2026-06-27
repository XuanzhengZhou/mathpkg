---
role: proof
locale: en
of_concept: "$C"
source_book: gtm007
source_chapter: "I"
source_section: "Appendix"
---
If $s, s' \in S$ are distinct, then $s_a \neq s'_a$, for otherwise $s = \pm s'$, contradicting the choice of $S$. Thus $s \mapsto s_a$ is a bijection of $S$ onto itself. Multiplying the equalities $as = e_s(a) s_a$ gives

$$a^{(p-1)/2} \prod_{s \in S} s = \left(\prod_{s \in S} e_s(a)\right) \prod_{s \in S} s_a = \left(\prod_{s \in S} e_s(a)\right) \prod_{s \in S} s.$$

Cancelling $\prod_{s \in S} s$ (which is nonzero in $\mathbb{F}_p$) yields $a^{(p-1)/2} = \prod_{s \in S} e_s(a)$. The left side equals $\left(\frac{a}{p}\right)$ by Euler's criterion.
