---
role: proof
locale: en
of_concept: dimensionality-relation-modular-lattices
source_book: gtm030
source_chapter: "3"
source_section: "3"
---

Assume $L$ is modular with $0, 1$ and has finite length. For $a \in L$, the sublattice $L_a = \{x \mid x \leq a\}$ satisfies the same conditions; let $l(a)$ denote the length of $L_a$, called the rank of $a$.

If $a \geq b$, then $l(a) = l(b) + \text{length}(I[a, b])$, since any composition chain from $a$ down to $0$ can be formed by concatenating a composition chain from $a$ to $b$ with one from $b$ to $0$.

Now for arbitrary $a, b \in L$, we have

$$l(a \cup b) = l(a) + \text{length}(I[a \cup b, a]),$$
$$l(b) = l(a \cap b) + \text{length}(I[b, a \cap b]).$$

By Theorem 4, the intervals $I[a \cup b, a]$ and $I[b, a \cap b]$ are isomorphic, hence have equal lengths. Therefore

$$l(a \cup b) - l(a) = l(b) - l(a \cap b),$$

which rearranges to

$$l(a \cup b) = l(a) + l(b) - l(a \cap b).$$
