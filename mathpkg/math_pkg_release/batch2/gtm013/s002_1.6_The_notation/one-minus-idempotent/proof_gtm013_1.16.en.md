---
role: proof
locale: en
of_concept: one-minus-idempotent
source_book: gtm013
source_chapter: "1"
source_section: "1.16"
---

Compute directly:

$$(1 - e)^2 = (1 - e)(1 - e) = 1 - e - e + e^2.$$

Since $e^2 = e$, we obtain

$$(1 - e)^2 = 1 - e - e + e = 1 - e,$$

so $1 - e$ is idempotent. For centrality: if $e \in \operatorname{Cen} R$, then for any $x \in R$,

$$(1 - e)x = x - ex = x - xe = x(1 - e),$$

so $1 - e \in \operatorname{Cen} R$.
