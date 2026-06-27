---
role: proof
locale: en
of_concept: character-conductor-sum
source_book: gtm059
source_chapter: "2"
source_section: "9"
---

For (i), the statement is immediate from the distribution relation, since at level $N$, the sum over all elements decomposes into a sum over the subgroup where the character is trivial, giving the claimed relation.

For (ii), we have

$$
\sum_{a \in G(N)} \chi(a) g(p,a) = \sum_{a \in G(N)} \chi(a) g(p,a).
$$

By the distribution relation, we decompose the sum over $G(N)$ into a sum over the kernel of reduction modulo $M$ and its complement. The elements that are not primitive under the map $c \mapsto pc$ contribute the factor $(1 - \chi(p))$, leading to the stated formula.
