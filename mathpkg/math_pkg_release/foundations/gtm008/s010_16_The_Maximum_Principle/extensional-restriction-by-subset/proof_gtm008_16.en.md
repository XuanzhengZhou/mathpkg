---
role: proof
locale: en
of_concept: extensional-restriction-by-subset
source_book: gtm008
source_chapter: "16"
source_section: "The Maximum Principle"
---

1. $v'$ is extensional: This is obvious from the definition of $b \cdot v$.

2. $\llbracket v' \subseteq u \rrbracket = \prod_{x \in \mathcal{D}(v)} (v'(x) \Rightarrow \llbracket x \in u \rrbracket)$
   $= \prod_{x \in \mathcal{D}(v)} (\llbracket v \subseteq u \rrbracket \cdot \llbracket x \in v \rrbracket \Rightarrow \llbracket x \in u \rrbracket)$ since $v$ is extensional
   $= \prod_{x \in \mathcal{D}(v)} \llbracket (v \subseteq u) \land (x \in v) \rightarrow x \in u \rrbracket$
   $= 1$.

3. $\llbracket v = v' \rrbracket = \llbracket v = v' \rrbracket \cdot \llbracket v' \subseteq u \rrbracket \leq \llbracket v \subseteq u \rrbracket = b$ by (2).
   Also, $\llbracket v = v' \rrbracket = \llbracket v = b \cdot v \rrbracket \geq b$ by Exercise 1 (properties of $b \cdot v$ for extensional $v$).
   Hence $\llbracket v = v' \rrbracket = b = \llbracket v \subseteq u \rrbracket$.
