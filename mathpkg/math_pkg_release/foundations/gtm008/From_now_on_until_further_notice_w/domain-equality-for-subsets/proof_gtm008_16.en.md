---
role: proof
locale: en
of_concept: domain-equality-for-subsets
source_book: gtm008
source_chapter: "16"
source_section: "The Maximum Principle"
---

$v'$ is extensional by the same argument as in earlier results: $v'(x) = \llbracket x \in v \rrbracket$ implies $v'(x) = \llbracket x \in v' \rrbracket$. 

By the definition of $v'$, for every $x \in \mathcal{D}(v') = \mathcal{D}(u)$ we have $v'(x) = \llbracket x \in v \rrbracket$. Since $\llbracket v \subseteq u \rrbracket = 1$, the membership values for elements of $v$ coincide whether computed via $v$ or $v'$. Specifically, $\llbracket v' \subseteq v \rrbracket = 1$ follows from $v'(x) \leq \llbracket x \in v \rrbracket$.

It remains to show $\llbracket v \subseteq v' \rrbracket = 1$, i.e., $(\forall x \in \mathcal{D}(v))\; v(x) \leq \llbracket x \in v' \rrbracket$. Since $v$ is extensional, $v(x) = \llbracket x \in v \rrbracket$, and by definition $\llbracket x \in v' \rrbracket = \sum_{y \in \mathcal{D}(u)} v'(y) \cdot \llbracket x = y \rrbracket = \sum_{y \in \mathcal{D}(u)} \llbracket y \in v \rrbracket \cdot \llbracket x = y \rrbracket \geq \llbracket x \in v \rrbracket$, which gives the result. Hence $\llbracket v = v' \rrbracket = 1$.
