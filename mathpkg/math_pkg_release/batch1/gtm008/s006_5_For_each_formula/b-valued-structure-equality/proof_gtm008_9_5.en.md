---
role: proof
locale: en
of_concept: b-valued-structure-equality
source_book: gtm008
source_chapter: "9"
source_section: "5"
---

1. $\llbracket t_1 = t_2 \rrbracket \llbracket t_2 \in t_3 \rrbracket \leq \sum_{t \in T_{\alpha}} \llbracket t = t_1 \rrbracket \llbracket t \in t_3 \rrbracket = \llbracket t_1 \in t_3 \rrbracket$ (by Theorem 9.31).

2. Let $\beta_1 = \max(\rho(t_1), \rho(t_2))$. Then $\llbracket t_1 = t_2 \rrbracket \llbracket t_3 \in t_1 \rrbracket = \sum_{t \in T_{\rho(t_1)}} \llbracket t = t_3 \rrbracket \prod_{s \in T_{\beta_1}} \llbracket s \in t_1 \leftrightarrow s \in t_2 \rrbracket \llbracket t \in t_1 \rrbracket \leq \sum_{t \in T_{\alpha}} \llbracket t = t_3 \rrbracket \llbracket t \in t_2 \rrbracket = \llbracket t_3 \in t_2 \rrbracket$.

3 and 4 follow from Theorem 9.30.
