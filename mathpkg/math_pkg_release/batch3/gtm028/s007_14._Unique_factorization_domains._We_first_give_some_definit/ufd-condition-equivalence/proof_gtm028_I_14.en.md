---
role: proof
locale: en
of_concept: ufd-condition-equivalence
source_book: gtm028
source_chapter: "I"
source_section: "14"
---

Assume UF1 and UF2 hold. Let $p$ be irreducible and suppose $p \mid ab$. By UF1, $a$ and $b$ can be factored into irreducibles: $a = \prod_i p'_i$, $b = \prod_j p''_j$. Then $ab = p \cdot \prod_k q_k$ where the $q_k$ come from the irreducible factorization of $ab$. On the other hand, $ab = \prod_i p'_i \cdot \prod_j p''_j$. By UF2, these two factorizations are the same up to order and unit factors. Hence $p$ must differ from one of the factors $p'_i, p''_j$ by a unit factor, which means $p$ divides either $a$ or $b$. This proves UF3.

Conversely, assume UF1 and UF3 hold. Since UF2 is obvious for factorizations into one irreducible factor, we proceed by induction on the number $s$ of irreducible factors. Assume UF2 holds for any element factorable into $s$ irreducible factors, and let $a$ be an element factorable into $s+1$ irreducible factors. Let

$$a = \prod_{i=1}^{s+1} p_i = \prod_{j=1}^{\sigma} p'_j$$

be two factorizations of $a$ into irreducibles, the left one involving exactly $s+1$ factors. Since $p_1$ divides the product of the $p'_j$, by UF3, $p_1$ must divide one of the $p'_j$, say $p'_1$. Since $p'_1$ is irreducible, $p_1$ and $p'_1$ are associates: $p'_1 = \epsilon p_1$ with $\epsilon$ a unit. Cancelling $p_1$ yields

$$\prod_{i=2}^{s+1} p_i = \epsilon \prod_{i=2}^{\sigma} p'_j.$$

The left side has $s$ irreducible factors, so by the induction hypothesis, the two factorizations in this equality differ only in order and by unit factors. Since $p'_1$ differs from $p_1$ by a unit factor, the original two factorizations of $a$ also differ only in order and by unit factors. Thus UF2 holds for $a$, completing the induction.
