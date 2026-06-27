---
role: proof
locale: en
of_concept: bounding-all-elements-of-rank-alpha
source_book: gtm008
source_chapter: "9"
source_section: "5"
---

By condition 5 of the construction (page 87-88), for any formula $\varphi$,
$$(\forall a_1, \ldots, a_n \in M_{\alpha})(\exists b \in M_{\alpha+1})(\forall a \in M_{\alpha}) \llbracket \varphi(a, a_1, \ldots, a_n) \rrbracket_{M_{\alpha}} = \llbracket a \in b \rrbracket.$$
Take $\varphi(x)$ to be the formula $x = x$. Then $\llbracket a = a \rrbracket_{M_{\alpha}} = 1$, so we obtain $b \in M_{\alpha+1}$ such that $\llbracket a \in b \rrbracket = 1$ for all $a \in M_{\alpha}$. Since $M_{\alpha+1} \subseteq M$, we have $b \in M$.
