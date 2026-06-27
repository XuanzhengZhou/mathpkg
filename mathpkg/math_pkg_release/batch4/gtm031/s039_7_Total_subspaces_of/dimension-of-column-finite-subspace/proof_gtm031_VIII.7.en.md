---
role: proof
locale: en
of_concept: dimension-of-column-finite-subspace
source_book: gtm031
source_chapter: "Chapter VIII: The Ring of Linear Transformations"
source_section: "7. Total subspaces of R*"
---
**Proof.** The $e_i^*$ are linearly independent since any finite linear combination $\sum \alpha_i e_i^*$ that vanishes must have all $\alpha_i = 0$ (evaluate at $e_k$ to get $\alpha_k = 0$). They span $\mathfrak{R}_0^*$ because any column-finite linear function $f$ with $f(e_i) = \beta_i$ (nonzero for only finitely many $i$) can be written as $f = \sum_i \beta_i e_i^*$, which is a finite sum by the column-finite condition. Hence $\dim \mathfrak{R}_0^* = \dim \mathfrak{R}$.
