---
role: proof
locale: en
of_concept: lemma-14-triple-rotation
source_book: gtm008
source_chapter: "14"
source_section: "14. Another Interpretation of V^{(B)}"
---

Let $u \in V^{(B)}$. Then

$$[u \in \{ \langle x, y, z \rangle \mid \langle x, z, y \rangle \in \check{k}_1 \}]$$
$$= [[(\exists x, w) [\langle x, w \rangle \in \check{k}_1 \land (\exists y, z) [w = \langle z, y \rangle \land u = \langle x, y, z \rangle]]]$$
$$= \sum_{\langle k_3, k_4 \rangle \in k_1} [[(\exists y)(\exists z) [\check{k}_4 = \langle z, y \rangle \land u = \langle \check{k}_3, y, z \rangle]]]$$
$$= \sum_{\langle k_3, k_4 \rangle \in k_1} \sum_{\langle k_6, k_5 \rangle = k_4} [[u = \langle \check{k}_3, \check{k}_5, \check{k}_6 \rangle]]$$
$$= \sum_{k \in \{ \langle k_3, k_5, k_6 \rangle \mid \langle k_3, k_6, k_5 \rangle \in k_1 \}} [[u = \check{k}]]$$
$$= [[u \in \{ \langle x, y, z \rangle \mid \langle x, z, y \rangle \in k_1 \}^{\vee}]].$$
