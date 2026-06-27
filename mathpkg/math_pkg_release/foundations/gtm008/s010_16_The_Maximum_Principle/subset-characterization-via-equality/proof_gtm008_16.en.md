---
role: proof
locale: en
of_concept: subset-characterization-via-equality
source_book: gtm008
source_chapter: "16"
source_section: "The Maximum Principle"
---

Let $b = \sum_{v' \in A} \llbracket v = v' \rrbracket$. From Theorem 16.24 (which states that for extensional $v$ with $\llbracket v \subseteq u \rrbracket$, there exists $v' \in A$ with $\llbracket v = v' \rrbracket = 1$), we have

$$\llbracket v \subseteq u \rrbracket \leq b.$$

On the other hand,

$$b = \sum_{v' \in A} \llbracket v = v' \rrbracket \leq \sum_{v' \in A} \llbracket v' \subseteq u \rrbracket \cdot \llbracket v' = v \rrbracket \leq \llbracket v \subseteq u \rrbracket.$$

The first inequality uses that $\llbracket v = v' \rrbracket \leq \llbracket v' \subseteq u \rrbracket$ (since equality implies inclusion), and the second follows from $\llbracket v' \subseteq u \rrbracket = 1$ for $v' \in A$ and the transitivity of equality.

Thus $\llbracket v \subseteq u \rrbracket = b = \sum_{v' \in A} \llbracket v = v' \rrbracket$.
