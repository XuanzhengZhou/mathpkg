---
role: proof
locale: en
of_concept: uniqueness-irredundant-decomposition
source_book: gtm030
source_chapter: "3"
source_section: "5"
---

Applying Theorem 7 repeatedly, we can write
$$a = r_1' \cap q_2 \cap \cdots \cap q_m = r_1' \cap r_2' \cap q_3 \cap \cdots \cap q_m = \cdots = r_{1'} \cap r_{2'} \cap \cdots \cap r_{m'}.$$

Since the decomposition $a = r_1 \cap r_2 \cap \cdots \cap r_n$ is irredundant, all the $r_i$ must appear in the last line of this chain. Hence $m \geq n$. By symmetry, applying the same argument starting from the $r_j$ representation yields $n \geq m$. Therefore $m = n$.
