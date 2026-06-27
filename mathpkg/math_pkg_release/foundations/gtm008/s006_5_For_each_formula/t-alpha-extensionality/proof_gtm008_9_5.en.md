---
role: proof
locale: en
of_concept: t-alpha-extensionality
source_book: gtm008
source_chapter: "9"
source_section: "5"
---

By Definition 9.27.6, for any $t_1, t_2 \in T_{\alpha}$,
$$
\llbracket t_1 = t_2 \rrbracket_{\mathbf{T}_{\alpha}} = \prod_{t \in T_{\alpha}} \llbracket t \in t_1 \leftrightarrow t \in t_2 \rrbracket_{\mathbf{T}_{\alpha}}.
$$

Now for the extensionality axiom:
$$
\llbracket (\forall z)(z \in x \leftrightarrow z \in y) \to x = y \rrbracket_{\mathbf{T}_{\alpha}}
= \prod_{t \in T_{\alpha}} \llbracket t \in t_1 \leftrightarrow t \in t_2 \rrbracket_{\mathbf{T}_{\alpha}} \Rightarrow \llbracket t_1 = t_2 \rrbracket_{\mathbf{T}_{\alpha}} = 1,
$$
since the antecedent and consequent are exactly the same product. Taking the product over all $t_1, t_2 \in T_{\alpha}$ yields $1$, establishing the extensionality axiom with value $1$ in $\mathbf{T}_{\alpha}$.
