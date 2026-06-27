---
role: proof
locale: en
of_concept: algebraic-closure-existence-via-ultraproducts
source_book: gtm022
source_chapter: "VII"
source_section: "3"
---

Let $T$ be elementary field theory augmented with constants for $F$ and axioms for the field operations of $F$. For each polynomial $r \in F[x]$, let $F_r$ be a splitting field of $r$. Let $J_r = \{s \in F[x] \mid r \text{ splits over } F_s\}$. The family $\{J_r\}$ has the finite intersection property (since $r_1\cdots r_n \in J_{r_1} \cap \cdots \cap J_{r_n}$). By Lemmas 2.4 and 2.5, there exists an ultrafilter $\mathcal{F}$ containing all $J_r$. The ultraproduct $F^* = \prod F_r / \mathcal{F}$ is a field extension of $F$. For any monic polynomial $r$ over $F$, the set of indices where $r$ splits is in $\mathcal{F}$, so by Łoś's Theorem $r$ splits in $F^*$. Thus $F^*$ is algebraically closed. Let $\bar{F}$ be the subfield of $F^*$ of elements algebraic over $F$. Then $\bar{F}$ is an algebraic closure of $F$.
