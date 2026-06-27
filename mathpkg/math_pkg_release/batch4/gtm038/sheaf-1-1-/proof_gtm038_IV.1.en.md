---
role: proof
locale: en
of_concept: sheaf-1-1-
source_book: gtm038
source_chapter: "IV"
source_section: "1. Sheaves of Sets"
---
**Proof.** A presheaf $\mathcal{F}$ on a topological space $ is a sheaf if for every open set $ and every open covering $\{U_i\}$ of $, the sequence

30506310 \to \mathcal{F}(U) \to \prod_i \mathcal{F}(U_i) \rightrightarrows \prod_{i,j} \mathcal{F}(U_i \cap U_j)3050631

is exact. This encodes the two sheaf axioms: (1) locality: sections that agree on all overlaps are equal; (2) gluing: compatible families of sections glue uniquely. The verification follows directly from the definitions. $\square$
