---
role: proof
locale: en
of_concept: con-closure-operation
source_book: gtm022
source_chapter: "II"
source_section: "3"
---

[Note: The full proof text for Lemma 3.9 is truncated in the extracted section. The following presents the reasoning for the closure operation properties based on the definition of Con as the semantic consequence operator.]

For (i): Let $p \in A$. For any valuation $v$ with $v(q) = 1$ for all $q \in A$, we have in particular $v(p) = 1$. Hence $p \in \text{Con}(A)$, showing $A \subseteq \text{Con}(A)$.

For (ii): Suppose $A_1 \subseteq A_2$. Let $p \in \text{Con}(A_1)$. Then for every valuation $v$ such that $v(q) = 1$ for all $q \in A_1$, we have $v(p) = 1$. If $v$ is any valuation with $v(q) = 1$ for all $q \in A_2$, then in particular $v(q) = 1$ for all $q \in A_1$ (since $A_1 \subseteq A_2$), so $v(p) = 1$. Hence $p \in \text{Con}(A_2)$, showing $\text{Con}(A_1) \subseteq \text{Con}(A_2)$.

[The remaining properties of a closure operation (idempotence: $\text{Con}(\text{Con}(A)) = \text{Con}(A)$) are not present in the truncated section text.]
