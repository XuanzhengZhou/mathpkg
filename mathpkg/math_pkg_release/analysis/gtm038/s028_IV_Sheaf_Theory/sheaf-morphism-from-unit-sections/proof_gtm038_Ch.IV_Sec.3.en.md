---
role: proof
locale: en
of_concept: sheaf-morphism-from-unit-sections
source_book: gtm038
source_chapter: "IV"
source_section: "3. Sheaf Morphisms"
---

Let $e_i = j_i \circ 1 = (0, \ldots, 1, \ldots, 0)$ be the unit sections of $q\mathcal{O}$. For any $(a_1, \ldots, a_q) \in q\mathcal{O}_{\mathfrak{z}}$, we have $(a_1, \ldots, a_q) = \sum_{i=1}^{q} a_i e_i(\mathfrak{z})$. Applying the $\mathcal{O}_{\mathfrak{z}}$-linear homomorphism $\varphi_{\mathfrak{z}}$ yields $\varphi(a_1, \ldots, a_q) = \sum_i a_i \varphi(e_i(\mathfrak{z})) = \sum_i a_i s_i(\mathfrak{z})$, where $s_i = \varphi \circ e_i \in \Gamma(B, \mathcal{S})$.

Conversely, given $s_1, \ldots, s_q \in \Gamma(B, \mathcal{S})$, the formula $\varphi(a_1, \ldots, a_q) := \sum_i a_i s_i(\mathfrak{z})$ defines a stalk-wise $\mathcal{O}_{\mathfrak{z}}$-linear map whose continuity follows from the continuity of the sections $s_i$, hence an analytic sheaf morphism.
