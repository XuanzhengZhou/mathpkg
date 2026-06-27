---
role: proof
locale: en
of_concept: fubini-theorem-for-measurable-sets
source_book: gtm002
source_chapter: "14"
source_section: "14"
---

By Theorem 3.15, any plane measurable set $E$ can be represented as the union of an $F_\sigma$ set $A$ and a nullset $N$. We have $E_x = A_x \cup N_x$ for all $x$. Any section of a closed set is closed, hence $A_x$ is an $F_\sigma$ for every $x$ (as a countable union of closed sets). In particular, $A_x$ is measurable for every $x$. By Fubini's theorem for nullsets (Theorem 14.2), $N_x$ is a nullset, hence measurable, for all $x$ except a set of linear measure zero. Therefore $E_x$, as the union of a measurable set $A_x$ and a measurable set $N_x$, is measurable for all $x$ except a set of linear measure zero.
