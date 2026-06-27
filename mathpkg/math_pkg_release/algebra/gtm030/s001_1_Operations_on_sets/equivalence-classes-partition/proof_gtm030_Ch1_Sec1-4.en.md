---
role: proof
locale: en
of_concept: equivalence-classes-partition
source_book: gtm030
source_chapter: "Chapter I: Basic Concepts"
source_section: "1-4"
---

Let $\bar{a}$ and $\bar{b}$ be two equivalence classes. If $\bar{a} \cap \bar{b} = \varnothing$, we are done. Otherwise, pick $c \in \bar{a} \cap \bar{b}$. Then $c \sim a$ and $c \sim b$. By symmetry, $a \sim c$, and by transitivity $a \sim b$. For any $x \in \bar{a}$, we have $x \sim a \sim b$, so $x \in \bar{b}$, giving $\bar{a} \subseteq \bar{b}$. By symmetry, $\bar{b} \subseteq \bar{a}$. Hence $\bar{a} = \bar{b}$. Since every $a \in S$ belongs to $\bar{a}$ (by reflexivity), the equivalence classes cover $S$ and form a partition.
