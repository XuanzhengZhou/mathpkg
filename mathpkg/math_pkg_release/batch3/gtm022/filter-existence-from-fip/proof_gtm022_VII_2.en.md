---
role: proof
locale: en
of_concept: "filter-existence-from-fip"
source_book: gtm022
source_chapter: "VII"
source_section: "2"
---
Proof. Necessity is immediate: any filter satisfies FIP so any subset of a filter does too. For sufficiency, suppose $S$ has FIP. Put $T = \{U \subseteq I \mid U = J_1 \cap \cdots \cap J_n \text{ for some } n \text{ and } J_i \in S\}$. Define $\mathcal{F} = \{F \subseteq I \mid F \supseteq U \text{ for some } U \in T\}$. Then $\mathcal{F}$ is a filter containing $S$, as verified by checking the three filter axioms. $\square$
