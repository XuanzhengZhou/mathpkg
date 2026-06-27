---
role: proof
locale: en
of_concept: euler-class-product-formula
source_book: gtm020
source_chapter: "8"
source_section: "8.2"
---

Let $\xi^n$ be a real vector bundle with total space $E'$, space of nonzero vectors $E'_0$, and fibre $F'_b$ over $b$; let $\eta^m$ have total space $E''$, space of nonzero vectors $E''_0$, and fibre $F''_b$; and let $\xi \oplus \eta$ have total space $E$, space of nonzero vectors $E_0$, and fibre $F_b$. Let $E_1$ be the union of $F'_{0,b} \times F''_b$ for all $b \in B$, and $E_2$ the union of $F'_b \times F''_{0,b}$ for all $b \in B$. We have $E_0 = E_1 \cup E_2$ and the projection maps are homotopy equivalences relating $(E, E_1)$ to $(E', E'_0)$ and $(E, E_2)$ to $(E'', E''_0)$.

By Definition (7.4), we have $e(\xi \oplus \eta) = p^{*-1}j^*(U)$, where $U$ is the Thom class of $\xi \oplus \eta$. Then we calculate
$$p^{*-1}j^*(U) = p^{*-1}j^*(q_1^*(U') \, q_2^*(U'')) = p^{*-1}[p_1^*j_1^*(U') \, p_2^*j_2^*(U'')] = e(\xi)e(\eta).$$
This proves the theorem.
