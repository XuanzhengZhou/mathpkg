---
role: proof
locale: en
of_concept: b-valued-extensionality
source_book: gtm008
source_chapter: "9"
source_section: "5"
---

If $a, b \in M$, then there exists $\alpha$ such that $a \in M_{\alpha}$ and $b \in M_{\alpha}$. By Theorem 9.7,
$$
\llbracket (\forall x)[x \in a \leftrightarrow x \in b] \rrbracket = \prod_{x \in M_{\alpha}} \llbracket x \in a \leftrightarrow x \in b \rrbracket
= \prod_{x \in M_{\alpha}} \llbracket x \in a \leftrightarrow x \in b \rrbracket_{M_{\alpha}}
\leq \llbracket a = b \rrbracket_{M_{\alpha}}
$$
by condition 3 of the construction (each $M_{\alpha}$ satisfies extensionality). Since $M_{\alpha}$ is a $B$-valued substructure of $M$, $\llbracket a = b \rrbracket_{M_{\alpha}} = \llbracket a = b \rrbracket$. Thus $\llbracket (\forall x)[x \in a \leftrightarrow x \in b] \rrbracket \leq \llbracket a = b \rrbracket$, which is equivalent to the extensionality axiom holding with value $1$.
