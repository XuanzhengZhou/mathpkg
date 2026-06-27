---
role: proof
locale: en
of_concept: gauss-lemma
source_book: gtm007
source_chapter: "I"
source_section: "3"
---

First note that if $s, s' \in S$ are distinct, then $s_a \neq s'_a$, for otherwise $s = \pm s'$, contradicting $S \cap (-S) = \emptyset$. Thus $s \mapsto s_a$ is a bijection of $S$ onto itself. Multiplying the equalities $as = e_s(a)s_a$ over all $s \in S$ yields:
\[
a^{(p-1)/2} \prod_{s \in S} s = \left(\prod_{s \in S} e_s(a)\right) \prod_{s \in S} s_a.
\]
Since $s \mapsto s_a$ is bijective, $\prod_{s \in S} s_a = \prod_{s \in S} s$, and this product is nonzero (all elements are in $\mathbb{F}_p^*$). Canceling, we get $a^{(p-1)/2} = \prod_{s \in S} e_s(a)$. But $a^{(p-1)/2} = \left(\frac{a}{p}\right)$ by definition of the Legendre symbol, proving the lemma.
