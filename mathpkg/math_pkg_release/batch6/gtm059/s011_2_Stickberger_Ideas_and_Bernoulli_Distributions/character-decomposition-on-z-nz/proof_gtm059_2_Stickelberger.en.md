---
role: proof
locale: en
of_concept: character-decomposition-on-z-nz
source_book: gtm059
source_chapter: "2"
source_section: "Stickelberger Ideals and Bernoulli Distributions"
---

**Proof.**

By the Chinese Remainder Theorem, for $n = \prod_i p_i^{e_i}$ with pairwise coprime prime powers $p_i^{e_i}$, we have a ring isomorphism

$$\mathbb{Z}/n\mathbb{Z} \cong \prod_i \mathbb{Z}/p_i^{e_i}\mathbb{Z}.$$

This isomorphism induces an isomorphism of the corresponding groups of units:

$$(\mathbb{Z}/n\mathbb{Z})^\times \cong \prod_i (\mathbb{Z}/p_i^{e_i}\mathbb{Z})^\times.$$

Any character $\chi$ on $\mathbb{Z}/n\mathbb{Z}$ is determined by its restriction to the group of units, and by the universal property of the direct product, there exist unique characters $\chi_i$ on each $\mathbb{Z}/p_i^{e_i}\mathbb{Z}$ such that for every $x = (x_i)_i \in \prod_i \mathbb{Z}/p_i^{e_i}\mathbb{Z}$,

$$\chi(x) = \prod_i \chi_i(x_i).$$

Conversely, given any collection of characters $\chi_i$ on $\mathbb{Z}/p_i^{e_i}\mathbb{Z}$, the product $\chi = \prod_i \chi_i$ defines a valid character on $\mathbb{Z}/n\mathbb{Z}$. This establishes the one-to-one correspondence between characters on $\mathbb{Z}/n\mathbb{Z}$ and tuples of characters on the prime power components.
