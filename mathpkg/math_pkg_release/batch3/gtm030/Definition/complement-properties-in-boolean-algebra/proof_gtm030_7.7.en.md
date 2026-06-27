---
role: proof
locale: en
of_concept: complement-properties-in-boolean-algebra
source_book: gtm030
source_chapter: "7"
source_section: "7"
---

Let $a \in B$ and let $a'$ and $a_1$ satisfy $a \cup a' = 1$, $a \cap a' = 0$ and $a \cup a_1 = 1$, $a \cap a_1 = 0$. Then:

$$a_1 = a_1 \cap 1 = a_1 \cap (a \cup a') = (a_1 \cap a) \cup (a_1 \cap a') = 0 \cup (a_1 \cap a') = a_1 \cap a'.$$

Thus $a_1 \leq a'$. Symmetrically, $a' \leq a_1$, so $a' = a_1$, proving uniqueness.

Now $a$ is clearly a complement of $a'$, so by uniqueness $a'' = (a')' = a$. Hence the complement map is an involution and therefore a bijection.

If $a \leq b$, then $a \cap b' \leq b \cap b' = 0$, so $a \cap b' = 0$. Then:

$$b' = b' \cap 1 = b' \cap (a \cup a') = (b' \cap a) \cup (b' \cap a') = 0 \cup (b' \cap a') = b' \cap a'.$$

Hence $b' \leq a'$, showing the complement map is order-inverting. Since it is a bijection and order-inverting, the De Morgan laws follow:
$$(a \cup b)' = a' \cap b', \quad (a \cap b)' = a' \cup b'.$$
