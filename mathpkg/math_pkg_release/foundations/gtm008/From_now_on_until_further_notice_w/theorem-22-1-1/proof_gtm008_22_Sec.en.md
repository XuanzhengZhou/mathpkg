---
role: proof
locale: en
of_concept: theorem-22-1-1
source_book: gtm008
source_chapter: "22"
source_section: "22 The Completion of a Boolean Algebra

For the following let"
---
1. Let $A \subseteq S$; then obviously

$$A^{-S} \subseteq A^{-} \cap S:$$

Conversely, let $p \in A^{-} \cap S$. Then

$$p \in S \land (\forall N(p))[N(p) \cap A \neq 0]$$

$$(\forall N(p))[N(p) \cap S \cap A \neq 0] \quad \text{since } A \subseteq S$$

$$(\forall N^{S}(p))[N^{S}(p) \cap A \neq 0]$$

i.e.,

$$p \in A^{-S}.$$

2. Follows from 1.
