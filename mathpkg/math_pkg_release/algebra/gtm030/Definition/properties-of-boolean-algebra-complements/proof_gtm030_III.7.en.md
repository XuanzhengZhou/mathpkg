---
role: proof
locale: en
of_concept: properties-of-boolean-algebra-complements
source_book: gtm030
source_chapter: "III"
source_section: "7"
---

**Uniqueness:** Let $a \in B$ and let $a'$ and $a_1$ be elements such that $a \cup a' = 1$, $a \cap a' = 0$, $a \cup a_1 = 1$, $a \cap a_1 = 0$. Then
$$a_1 = a_1 \cap 1 = a_1 \cap (a \cup a') = (a_1 \cap a) \cup (a_1 \cap a') = a_1 \cap a'.$$
Similarly, $a' = a' \cap a_1$. Hence $a' = a_1$, proving uniqueness.

**Involution:** Since $a$ is a complement of $a'$, we have $a'' = (a')' = a$, so the mapping is of period two. Consequently it is 1-1 of $B$ onto itself.

**Order-reversing:** If $a \leq b$, then $a \cap b' \leq b \cap b' = 0$, so
$$b' = b' \cap 1 = b' \cap (a \cup a') = (b' \cap a) \cup (b' \cap a') = b' \cap a'.$$
Hence $b' \leq a'$.

**De Morgan's laws:** Since $a \mapsto a'$ is a 1-1 order-inverting map of $B$ onto itself, the duality principle yields $(a \cup b)' = a' \cap b'$ and $(a \cap b)' = a' \cup b'$.
