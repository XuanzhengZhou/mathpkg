---
role: proof
locale: en
of_concept: representation-by-extensional-set
source_book: gtm008
source_chapter: "16"
source_section: "The Maximum Principle"
---

For $v \in V^{(B)}$ and $d \subseteq V^{(B)}$ such that $\mathcal{D}(v) \subseteq d$, define $u: d \rightarrow B$ by $(\forall x \in d)[u(x) = \llbracket x \in v \rrbracket]$. Then for $x \in d$,

$$u(x) \leq \llbracket x \in u \rrbracket = \sum_{y \in d} \llbracket y \in v \rrbracket \cdot \llbracket x = y \rrbracket \leq \llbracket x \in v \rrbracket = u(x),$$

so $u(x) = \llbracket x \in u \rrbracket$, i.e., $u$ is extensional. That $\llbracket u = v \rrbracket = 1$ follows from the argument in Theorem 16.1.
