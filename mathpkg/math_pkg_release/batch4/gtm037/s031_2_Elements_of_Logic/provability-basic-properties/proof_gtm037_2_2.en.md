---
role: proof
locale: en
of_concept: provability-basic-properties
source_book: gtm037
source_chapter: ""
source_section: ""
---

The proof uses the inductive definition of $\vdash$ from 10.23. For (i), if $\Gamma \subseteq \Delta$, then every axiom and rule instance available from $\Gamma$ is also available from $\Delta$, so any $\Gamma$-proof is also a $\Delta$-proof. For (ii), a proof is a finite sequence, so it can only reference finitely many members of $\Gamma$; let $\Theta$ be that finite subset. Then $\Theta \vdash \varphi$.

For (iii), assume $\Gamma \vdash \chi$ for each $\chi \in \Delta$ and $\Delta \vdash \varphi$. Let $\Theta \subseteq \Delta$ be a finite subset such that $\Theta \vdash \varphi$ (by (ii)). For each $\chi \in \Theta$, we have a $\Gamma$-proof of $\chi$. Concatenating these proofs with the $\Theta$-proof of $\varphi$ yields a $\Gamma$-proof of $\varphi$, hence $\Gamma \vdash \varphi$.
