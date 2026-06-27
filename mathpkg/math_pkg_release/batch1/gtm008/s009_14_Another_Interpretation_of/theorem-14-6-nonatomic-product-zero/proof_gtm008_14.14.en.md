---
role: proof
locale: en
of_concept: theorem-14-6-nonatomic-product-zero
source_book: gtm008
source_chapter: "14"
source_section: "14. Another Interpretation of V^{(B)}"
---

Suppose the product $a = \prod_{b \in S} b \cdot \prod_{b \in B \setminus S} (-b) \neq 0$. Then for any $b \in S$, $a \leq b$, and for any $b \in B \setminus S$, $a \leq -b$ (i.e., $a \cdot b = 0$). For any $b' \in B$ with $b' \leq a$: if $b' \in S$, then $b' \leq a \leq b'$, so $b' = a$; if $b' \in B \setminus S$, then $b' \cdot a \leq b' \cdot (-b') = 0$, so $b' = 0$. Hence $a$ is an atom, contradicting the nonatomicity of $B$.
