---
role: proof
locale: en
of_concept: chevalley-constructible-theorem
source_book: gtm053
source_chapter: "4"
source_section: "4.3"
---

The quantifier elimination statement in the language $L_1\text{Ar}$ can be translated into this form. By Tarski's theorem (4.2), every $L_1\text{Ar}$-formula is equivalent modulo $\text{ACF}_p$ to a quantifier-free formula. A quantifier-free formula in $L_1\text{Ar}$ with parameters is a Boolean combination of atomic formulas. Atomic formulas in $L_1\text{Ar}$ are equations between terms built from $+, \cdot, 0, 1$, and variables; each such equation $t_1(\bar{x}) = t_2(\bar{x})$ is equivalent to $p(\bar{x}) = 0$ for some polynomial $p$. Thus quantifier-free definable sets are exactly Boolean combinations of zero-sets of polynomials, i.e., constructible sets.

The second statement — that the family is also closed under projections — follows because if a set is definable, its projection is also definable (by existential quantification), and hence constructible by the first part.
