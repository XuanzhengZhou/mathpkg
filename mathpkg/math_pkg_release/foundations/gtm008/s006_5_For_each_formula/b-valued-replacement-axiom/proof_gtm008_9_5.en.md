---
role: proof
locale: en
of_concept: b-valued-replacement-axiom
source_book: gtm008
source_chapter: "9"
source_section: "5"
---

First note $(\forall x \in M) \llbracket (\exists y)\varphi'(x, y) \rrbracket = 1$. If $a \in M$, then $(\exists \alpha)[a \in M_{\alpha}]$. By Corollary 9.15, there exists $\beta$ such that for all $x \in M_{\alpha}$, $\sum_{y \in M_{\beta}} \llbracket \varphi'(x, y) \rrbracket = 1$. By Theorem 9.23, there exists $b$ with $(\forall y \in M_{\beta}) \llbracket y \in b \rrbracket = 1$. Hence $\llbracket x \in a \rrbracket \leq \llbracket (\exists y \in b)\varphi'(x, y) \rrbracket$, yielding $\llbracket (\forall x \in a)(\exists y \in b)\varphi'(x, y) \rrbracket = 1$.
