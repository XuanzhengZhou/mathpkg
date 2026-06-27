---
role: proof
locale: en
of_concept: sum-product-of-measurable-functions
source_book: gtm018
source_chapter: "IV"
source_section: "19"
---
**Proof.** We restrict to finite valued functions. For any real $c$,
$$\{x : f(x) + g(x) < c\} = \{x : f(x) < c - g(x)\},$$
so the measurability of $f+g$ follows from Theorem A of \S 18 (applied with $-g$). For the product,
$$fg = \frac{1}{4}[(f + g)^2 - (f - g)^2].$$
Since $t \mapsto t^2$ is Borel measurable and vanishes at $0$, each squared term is measurable by Theorem B, hence $fg$ is measurable.
