---
role: proof
locale: en
of_concept: relative-complements-in-complemented-modular-lattice
source_book: gtm030
source_chapter: "VII"
source_section: "7. Complemented modular lattices"
---

Let $L$ be a complemented modular lattice and let $a, b \in L$ with $b \leq a$. Since $L$ is complemented, there exists $b' \in L$ such that
$$b \cup b' = 1, \quad b \cap b' = 0.$$
By modularity (since $b \leq a$),
$$a = a \cap 1 = a \cap (b \cup b') = b \cup (a \cap b').$$
Set $b_1 = a \cap b'$. Clearly $b_1 \leq a$. Moreover,
$$b \cap b_1 = b \cap (a \cap b') = (b \cap a) \cap b' = b \cap b' = 0,$$
since $b \leq a$ implies $b \cap a = b$. Therefore,
$$b \cup b_1 = a, \quad b \cap b_1 = 0, \quad b_1 \leq a,$$
so $b_1$ is a complement of $b$ relative to $a$.
