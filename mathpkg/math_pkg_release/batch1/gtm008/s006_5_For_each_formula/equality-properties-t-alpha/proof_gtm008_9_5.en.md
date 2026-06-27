---
role: proof
locale: en
of_concept: equality-properties-t-alpha
source_book: gtm008
source_chapter: "9"
source_section: "5"
---

Both statements follow directly from Definition 9.27.

1. By Definition 9.27.6, $\llbracket t_1 = t_1 \rrbracket_{\mathbf{T}_{\alpha}} = \prod_{t \in T_{\alpha}} \llbracket t \in t_1 \leftrightarrow t \in t_1 \rrbracket_{\mathbf{T}_{\alpha}}$. Since $\llbracket t \in t_1 \leftrightarrow t \in t_1 \rrbracket = (\llbracket t \in t_1 \rrbracket \Rightarrow \llbracket t \in t_1 \rrbracket) \land (\llbracket t \in t_1 \rrbracket \Rightarrow \llbracket t \in t_1 \rrbracket) = 1$, the product is $1$.

2. Symmetry is obvious from the definition, since $\llbracket t \in t_1 \leftrightarrow t \in t_2 \rrbracket$ is symmetric in $t_1$ and $t_2$ by the properties of the Boolean biconditional.
