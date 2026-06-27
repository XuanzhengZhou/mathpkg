---
role: proof
locale: en
of_concept: theorem-14-7-atom-f-equals-check-s
source_book: gtm008
source_chapter: "14"
source_section: "14. Another Interpretation of V^{(B)}"
---

Since $b_0$ is an atom, $b \in S \iff -b \in B \setminus S$. By Theorem 13.16, $[x = \check{b}] = 0$ unless $x = b$, and by Theorem 13.2, $[b \in F] = F(\check{b})$. Then

$$[F = \check{S}] = \prod_{b \in B} \left(F(\check{b}) \Rightarrow [\check{b} \in \check{S}]\right) \cdot \prod_{b \in S} F(\check{b})$$
$$= \prod_{b \in B \setminus S} (-b) \cdot \prod_{b \in S} b \cdot b_0 = b_0.$$

The last equality holds since for $b \in S$, $b_0 \leq b$, and the meet of all $b \in S$ with $b_0$ equals $b_0$. For $b \in B \setminus S$, $b_0 \cdot b = 0$, so $b_0 \leq -b$, making the product over $B \setminus S$ equal to 1 when intersected with $b_0$.
