---
role: proof
locale: en
of_concept: ultrafilter-equivalent-characterizations
source_book: gtm026
source_chapter: "5"
source_section: "5.13"
---

Clearly (3) implies (2), (2) implies (1), and we have (1) implying (3) since $(X - A_1), \ldots, (X - A_n), (A_1 \cup \cdots \cup A_n)$ have empty intersection.

(1) implies (4): If $F \in \mathcal{F} \supset \mathcal{U}$ and $F \notin \mathcal{U}$ then $X - F \in \mathcal{U}$ so that $\mathcal{F}$ doesn't have the finite intersection property.

(4) implies (5): If $A \notin \mathcal{U}$ then $\mathcal{U} \cup \{A\}$ doesn't have the finite intersection property and $U_1 \cap \cdots \cap U_n \cap A = \varnothing$ with $U_i \in \mathcal{U}$. If $U = U_1 \cap \cdots \cap U_n \notin \mathcal{U}$ then similarly $U \cap V_1 \cap \cdots \cap V_m = \varnothing$ with $V_i \in \mathcal{U}$, a contradiction.

(5) implies (1): If $A \cap U = \varnothing$ and $(X - A) \cap V = \varnothing$ with $U, V \in \mathcal{U}$ then $U \cap V = \varnothing$, a contradiction.
