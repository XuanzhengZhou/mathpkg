---
role: proof
locale: en
of_concept: gauss-lemma
source_book: gtm007
source_chapter: "I"
source_section: "§3 Appendix"
---

Remark first that, if $s$ and $s'$ are two distinct elements of $S$, then $s_a \neq s'_a$ (for otherwise $s = \pm s'$ contrary to the choice of $S$). This shows that $s \mapsto s_a$ is a bijection of $S$ onto itself.

Multiplying the equalities $as = e_s(a)s_a$, we obtain
$$a^{(p-1)/2} \prod_{s \in S} s = \left(\prod_{s \in S} e_s(a)\right) \prod_{s \in S} s_a = \left(\prod_{s \in S} e_s(a)\right) \prod_{s \in S} s,$$
where we used that $s \mapsto s_a$ is a bijection. Canceling $\prod_{s \in S} s \neq 0$ yields
$$a^{(p-1)/2} = \prod_{s \in S} e_s(a).$$

Since $\left(\frac{a}{p}\right) \equiv a^{(p-1)/2} \pmod{p}$ by Euler's criterion, and both sides are $\pm 1$, the equality holds in $\{\pm 1\}$.
