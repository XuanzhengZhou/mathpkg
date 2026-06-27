---
role: proof
locale: en
of_concept: equality-substitution-b-valued
source_book: gtm008
source_chapter: "9"
source_section: "5"
---

1. Using Theorem 9.31:
$$
\llbracket t_1 = t_2 \rrbracket \llbracket t_2 \in t_3 \rrbracket \leq \sum_{t \in T_{\alpha}} \llbracket t_1 = t_2 \rrbracket \llbracket t = t_2 \rrbracket \llbracket t \in t_3 \rrbracket
$$
$$
\leq \sum_{t \in T_{\alpha}} \llbracket t = t_1 \rrbracket \llbracket t \in t_3 \rrbracket = \llbracket t_1 \in t_3 \rrbracket.
$$

2. Let $\beta_1 = \max(\rho(t_1), \rho(t_2))$:
$$
\llbracket t_1 = t_2 \rrbracket \llbracket t_3 \in t_1 \rrbracket = \llbracket t_1 = t_2 \rrbracket \sum_{t \in T_{\rho(t_1)}} \llbracket t = t_3 \rrbracket \llbracket t \in t_1 \rrbracket
$$
$$
= \sum_{t \in T_{\rho(t_1)}} \llbracket t = t_3 \rrbracket \prod_{s \in T_{\beta_1}} \llbracket s \in t_1 \leftrightarrow s \in t_2 \rrbracket \llbracket t \in t_1 \rrbracket
$$
$$
\leq \sum_{t \in T_{\rho(t_1)}} \llbracket t = t_3 \rrbracket \llbracket t \in t_2 \rrbracket
$$
$$
\leq \sum_{t \in T_{\alpha}} \llbracket t = t_3 \rrbracket \llbracket t \in t_2 \rrbracket = \llbracket t_3 \in t_2 \rrbracket
$$
(since $\rho(t_1) < \alpha$).

3 and 4 follow from Theorem 9.30 and the properties established above.
