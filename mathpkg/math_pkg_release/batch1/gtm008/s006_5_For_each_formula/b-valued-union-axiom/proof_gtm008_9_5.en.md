---
role: proof
locale: en
of_concept: b-valued-union-axiom
source_book: gtm008
source_chapter: "9"
source_section: "5"
---

Given $a \in M$, let $\alpha$ be such that $a \in M_{\alpha}$. By condition 5, there exists $b \in M_{\alpha+1}$ such that for all $x \in M_{\alpha}$,
$$
\llbracket x \in b \rrbracket = \llbracket (\exists y \in a)(x \in y) \rrbracket_{M_{\alpha}}.
$$
By Theorem 9.7 (handling bounded quantifiers), this value equals $\llbracket (\exists y \in a)(x \in y) \rrbracket$ in $M$. Thus $b$ serves as the union of $a$ in $M$.
