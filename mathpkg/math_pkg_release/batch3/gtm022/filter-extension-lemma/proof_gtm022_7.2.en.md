---
role: proof
locale: en
of_concept: filter-extension-lemma
source_book: gtm022
source_chapter: "VII"
source_section: "2"
---

Necessity is immediate. For sufficiency, put $T = \{U \subseteq I \mid U = J_1 \cap \cdots \cap J_n \text{ for some } n, J_i \in S\}$ and $\mathcal{F} = \{F \subseteq I \mid F \supseteq U \text{ for some } U \in T\}$. Then $\mathcal{F}$ is a filter containing $S$: $\varnothing \notin \mathcal{F}$ by the finite intersection property, upward closure is by definition, and finite intersections of sets in $\mathcal{F}$ contain finite intersections of elements of $T$, which are again in $T$.
