---
role: proof
locale: en
of_concept: equivalence-relation-corresponds-to-partition
source_book: gtm054
source_chapter: "I"
source_section: "IB"
---
**Proof.** Let $ be an equivalence relation on $. For each  \in U$ let  = \{w \in U : (x, w) \in R\}$. Since $ is reflexive,  \in S_x$ and so  \neq \varnothing$ for each  \in U$. Let , y \in U$ and suppose  \in S_x \cap S_y$. Thus $ and  \in R$. Since $ is symmetric,  \in R$, and since $ is transitive,  \in R$. Now let  \in S_y$; hence  \in R$. Again by transitivity,  \in R$ and  \in S_x$. This proves that  \subseteq S_x$. By a symmetrical argument we see that  \subseteq S_y$. Thus exactly one of the following holds for any , y$:  = S_y$ or  \cap S_y = \varnothing$. The collection of distinct $'s forms a partition $\mathcal{Q}$ of $, and  \in R \iff x, y \in S_x \iff x, y$ are in the same cell.

Conversely, given a partition $\mathcal{Q}$, define  \in R \iff x$ and $ belong to the same cell. Reflexivity and symmetry are immediate. For transitivity, if  \in R$ and  \in R$, then , y$ are in the same cell and , z$ are in the same cell; since cells are disjoint or equal, $ and $ must be in the same cell, so  \in R$.
