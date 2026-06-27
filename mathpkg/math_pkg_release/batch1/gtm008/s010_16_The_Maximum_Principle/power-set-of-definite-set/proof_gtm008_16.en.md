---
role: proof
locale: en
of_concept: power-set-of-definite-set
source_book: gtm008
source_chapter: "16"
source_section: "The Maximum Principle"
---

Note that $B^{\mathcal{D}(u)} \subseteq V^{(\mathbf{B})}$ and $B^{\mathcal{D}(u)}$ is a set. Let $x \in V^{(\mathbf{B})}$ and $A_u = \{v \in V^{(\mathbf{B})} \mid \mathcal{D}(v) = \mathcal{D}(u)\}$. Then

$$\llbracket x \in B^{\mathcal{D}(u)} \times \{1\} \rrbracket = \sum_{v \in A_u} \llbracket x = v \rrbracket$$

since elements of $B^{\mathcal{D}(u)}$ are exactly functions from $\mathcal{D}(u)$ into $B$, which correspond to Boolean-valued sets with domain $\mathcal{D}(u)$. But since $u$ is definite, by Theorem 16.25,

$$\llbracket x \subseteq u \rrbracket = \sum_{v \in A_u} \llbracket x = v \rrbracket.$$

Therefore $\llbracket x \in \mathcal{P}(u) \rrbracket = \llbracket x \subseteq u \rrbracket = \llbracket x \in B^{\mathcal{D}(u)} \times \{1\} \rrbracket$, proving $\llbracket \mathcal{P}(u) = B^{\mathcal{D}(u)} \times \{1\} \rrbracket = 1$.
