---
role: proof
locale: en
of_concept: restriction-map-biendomorphism-ring
source_book: gtm013
source_chapter: "4"
source_section: "14"
---

The first assertion is an immediate consequence of the fact that direct summands are invariant under biendomorphisms: if $e \in \operatorname{End}({}_R M)$ is the idempotent for $M'$ and $b \in \operatorname{BiEnd}({}_R M)$, then $b(M') = b(Me) = (bM)e \subseteq M'$.

For the others, let $S = \operatorname{End}({}_R M)$ and let $e \in S$ be the idempotent for $M'$. By (5.9) there is a ring isomorphism $\rho: eSe \to \operatorname{End}({}_R M')$ where $\rho(ese): x \mapsto xese$ for $x \in M'$. Thus $\operatorname{BiEnd}({}_R M') = \operatorname{End}(M'_{eSe})$.

Now let $b \in \operatorname{BiEnd}({}_R M)$ and suppose $(b \mid M') = 0$. If $M'$ generates $M''$, then $M'$ generates $M$ (8.4), whence $b = 0$. This proves (1).

For (2), if $M'$ both generates and cogenerates $M''$, then each biendomorphism of $M'$ extends uniquely to a biendomorphism of $M$, giving the isomorphism. $\square$
