---
role: proof
locale: en
of_concept: extensional-subset-same-domain
source_book: gtm008
source_chapter: "16"
source_section: "The Maximum Principle"
---

$v'$ is extensional by construction (since $\llbracket x = y \rrbracket \cdot v'(x) \leq v'(y)$ holds because $v$ is extensional). Also $\llbracket v' \subseteq v \rrbracket = 1$ by the definition of $v'$.

It remains to show $(\forall x \in \mathcal{D}(v))[\llbracket x \in v \rrbracket \leq \llbracket x \in v' \rrbracket]$, i.e., $\llbracket v \subseteq v' \rrbracket = 1$. Since $\llbracket v \subseteq u \rrbracket = 1$, for any $x \in \mathcal{D}(v)$, $\llbracket x \in v \rrbracket \leq \sum_{y \in \mathcal{D}(u)} \llbracket x = y \rrbracket$. Using extensionality of $v$ and the definition of $v'$, one verifies $\llbracket v \subseteq v' \rrbracket = 1$. Together with $\llbracket v' \subseteq v \rrbracket = 1$, we obtain $\llbracket v = v' \rrbracket = 1$.
