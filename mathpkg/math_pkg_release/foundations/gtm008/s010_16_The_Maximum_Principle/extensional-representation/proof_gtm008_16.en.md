---
role: proof
locale: en
of_concept: extensional-representation
source_book: gtm008
source_chapter: "16"
source_section: "The Maximum Principle"
---

For $v \in V^{(\mathbf{B})}$ and $d \subseteq V^{(\mathbf{B})}$ such that $\mathcal{D}(v) \subseteq d$, define $u: d \rightarrow B$ by

$$(\forall x \in d)[u(x) = \llbracket x \in v \rrbracket].$$

Then for $x \in d$,

$$u(x) = \llbracket x \in v \rrbracket \leq \llbracket x \in u \rrbracket = \sum_{y \in d} \llbracket y \in v \rrbracket \cdot \llbracket x = y \rrbracket.$$

But also

$$\sum_{y \in d} \llbracket y \in v \rrbracket \cdot \llbracket x = y \rrbracket \leq \sum_{y \in d} \llbracket y \in v \rrbracket \cdot \llbracket y \in v \rightarrow x \in v \rrbracket \leq \llbracket x \in v \rrbracket = u(x).$$

Thus $u(x) = \llbracket x \in u \rrbracket$, i.e., $u$ is extensional. That $\llbracket u = v \rrbracket = 1$ was already proved in Theorem 16.1 (take a singleton family).
