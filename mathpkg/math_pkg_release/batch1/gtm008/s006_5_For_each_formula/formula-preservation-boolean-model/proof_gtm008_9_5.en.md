---
role: proof
locale: en
of_concept: formula-preservation-boolean-model
source_book: gtm008
source_chapter: "9"
source_section: "5"
---

Since $M_{\alpha}$ is a $B$-valued substructure of $M$, the interpretation of the atomic predicates $\in$ and $=$ is the same in both structures when restricted to elements of $M_{\alpha}$. For quantifier-free formulas, the Boolean truth value is built from these atomic predicates using only the Boolean operations (meet, join, complement), which are computed identically in $M_{\alpha}$ and $M$ when applied to elements of $M_{\alpha}$.

Therefore, by induction on the complexity of quantifier-free formulas $\varphi$,
$$
\llbracket \varphi(a_1, \ldots, a_n) \rrbracket_{M_{\alpha}} = \llbracket \varphi(a_1, \ldots, a_n) \rrbracket
$$
for all $a_1, \ldots, a_n \in M_{\alpha}$.
