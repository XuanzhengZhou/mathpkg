---
role: proof
locale: en
of_concept: ex-17-3-product-projective-not-projective
source_book: gtm013
source_chapter: "5"
source_section: "17"
---

**Proof.** Exercise 17.3. [Hint: Let $K$ consist of those $x \in \mathbb{Z}^{\mathbb{N}}$ such that each power of $2$ divides all but finitely many $\pi_n(x)$. Show that if $\mathbb{Z}^{\mathbb{N}}$ is free, then $K$ is free of uncountable rank. Now consider $K/2K$.]

The idea: if $\mathbb{Z}^{\mathbb{N}}$ were projective (hence free as a $\mathbb{Z}$-module), its subgroup $K$ would also be free (since subgroups of free abelian groups are free). But $K/2K$ would then be a vector space over $\mathbb{F}_2$ whose dimension equals the rank of $K$, leading to a cardinality contradiction because $K$ would have uncountable rank while being a subgroup of a countable product of countable sets.
