---
role: proof
locale: en
of_concept: "consequence-closure-operation"
source_book: gtm022
source_chapter: "II"
source_section: "3"
---
Proof. (i) If $p \in A$ and $v(A) \subseteq \{1\}$, then $v(p) = 1$, so $p \in \operatorname{Con}(A)$.

(ii) If $p \in \operatorname{Con}(A_1)$ and $v(A_2) \subseteq \{1\}$, then $v(A_1) \subseteq \{1\}$ since $A_1 \subseteq A_2$, so $v(p) = 1$, hence $p \in \operatorname{Con}(A_2)$.

(iii) Clearly $\operatorname{Con}(A) \subseteq \operatorname{Con}(\operatorname{Con}(A))$ by (i). Conversely, suppose $p \in \operatorname{Con}(\operatorname{Con}(A))$ and let $v$ be a valuation with $v(A) \subseteq \{1\}$. For any $q \in \operatorname{Con}(A)$, $v(q) = 1$, so $v(\operatorname{Con}(A)) \subseteq \{1\}$, and therefore $v(p) = 1$. Hence $p \in \operatorname{Con}(A)$. $\square$
