---
role: proof
locale: en
of_concept: definable-b-valued-subset
source_book: gtm008
source_chapter: "9"
source_section: "5"
---

We compute $\llbracket x \in b \rrbracket$:
$$\llbracket x \in b \rrbracket = \sum_{x' \in M_{\alpha}} \llbracket x = x' \rrbracket \llbracket x' \in a \rrbracket \llbracket \varphi(x', a_1, \ldots, a_n) \rrbracket_{M_{\alpha}}.$$
Since $M_{\alpha}$ is a $B$-valued substructure of $M$ and $\varphi$ is quantifier-free (for limited formulas),
$$\llbracket x \in b \rrbracket = \sum_{x' \in M_{\alpha}} \llbracket x = x' \rrbracket \llbracket x' \in a \rrbracket \llbracket \varphi(x', a_1, \ldots, a_n) \rrbracket$$
$$= \llbracket x \in a \rrbracket \llbracket \varphi(x, a_1, \ldots, a_n) \rrbracket.$$
This equality expresses $\llbracket x \in b \rrbracket$ entirely in terms of $M_{\alpha}$, proving $b$ is defined over $M_{\alpha}$.
