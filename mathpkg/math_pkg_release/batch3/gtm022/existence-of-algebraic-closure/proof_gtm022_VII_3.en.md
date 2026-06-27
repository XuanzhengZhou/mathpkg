---
role: proof
locale: en
of_concept: "existence-of-algebraic-closure"
source_book: gtm022
source_chapter: "VII"
source_section: "3"
---
Proof. Let $T$ be elementary field theory augmented by the addition of the elements of $F$ to the set of constants and of all atomic relations holding in $F$ to the axioms. The models of $T$ are the extension fields of $F$. Put $R = F[x]$, the ring of polynomials over $F$. For each $r \in R$, let $F_r$ be a splitting field of $r$. Put $J_r = \{s \in R \mid r \text{ splits over } F_s\}$. Since $r_1 r_2 \cdots r_n \in J_{r_1} \cap \cdots \cap J_{r_n}$, the family $\{J_r\}$ has the finite intersection property. There exists an ultrafilter $\mathcal{F}$ on $R$ containing all $J_r$. The ultraproduct $F^* = \prod_{r \in R} F_r / \mathcal{F}$ is an extension field of $F$ in which every polynomial over $F$ splits. The set of elements of $F^*$ algebraic over $F$ is then an algebraic closure of $F$. $\square$
