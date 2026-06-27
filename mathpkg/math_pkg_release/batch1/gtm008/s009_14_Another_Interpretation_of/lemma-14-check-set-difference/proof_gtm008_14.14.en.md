---
role: proof
locale: en
of_concept: lemma-14-check-set-difference
source_book: gtm008
source_chapter: "14"
source_section: "14. Another Interpretation of V^{(B)}"
---

$$\check{k}_1 \setminus \check{k}_2 = \{ \langle \check{k}, 1 \rangle \mid k \in k_1 \} \setminus \{ \langle \check{k}, 1 \rangle \mid k \in k_2 \}
= \{ \langle \check{k}, 1 \rangle \mid k \in k_1 \setminus k_2 \} = (k_1 \setminus k_2)^{\vee}.$$

The equality holds because the check of a set $k$ is $\{\langle \check{k}', 1 \rangle \mid k' \in k\}$.
