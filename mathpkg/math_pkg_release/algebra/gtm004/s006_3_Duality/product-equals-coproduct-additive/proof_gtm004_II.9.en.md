---
role: proof
locale: en
of_concept: product-equals-coproduct-additive
source_book: gtm004
source_chapter: "II"
source_section: "9"
---

# Proof of Product Equals Coproduct in an Additive Category

Let $\mathfrak{A}$ be an additive category and let $A_1, A_2 \in \mathfrak{A}$. Since $\mathfrak{A}$ is additive, the product $A_1 \oplus A_2$ exists with projections $p_1: A_1 \oplus A_2 \to A_1$, $p_2: A_1 \oplus A_2 \to A_2$. Define morphisms

$$i_1 = \{1_{A_1}, 0\}: A_1 \to A_1 \oplus A_2, \qquad i_2 = \{0, 1_{A_2}\}: A_2 \to A_1 \oplus A_2$$

using the universal property of the product.

**Lemma 9.2.** $i_1 p_1 + i_2 p_2 = 1_{A_1 \oplus A_2}$.

*Proof of Lemma.* Compute:

$$p_1(i_1 p_1 + i_2 p_2) = p_1 i_1 p_1 + p_1 i_2 p_2 = 1 \cdot p_1 + 0 \cdot p_2 = p_1,$$

$$p_2(i_1 p_1 + i_2 p_2) = p_2 i_1 p_1 + p_2 i_2 p_2 = 0 \cdot p_1 + 1 \cdot p_2 = p_2.$$

By the uniqueness property of the product, $i_1 p_1 + i_2 p_2 = 1$. $\square$

**Proof of Proposition 9.1.** We show $(A_1 \oplus A_2; i_1, i_2)$ is the coproduct. Given morphisms $\varphi_i: A_i \to B$, $i = 1, 2$, define

$$\langle \varphi_1, \varphi_2 \rangle = \varphi_1 p_1 + \varphi_2 p_2: A_1 \oplus A_2 \to B.$$

Then

$$\langle \varphi_1, \varphi_2 \rangle \circ i_1 = (\varphi_1 p_1 + \varphi_2 p_2) i_1 = \varphi_1 p_1 i_1 + \varphi_2 p_2 i_1 = \varphi_1 \cdot 1 + \varphi_2 \cdot 0 = \varphi_1,$$

and similarly $\langle \varphi_1, \varphi_2 \rangle \circ i_2 = \varphi_2$.

For uniqueness, suppose $f: A_1 \oplus A_2 \to B$ satisfies $f i_1 = \varphi_1$, $f i_2 = \varphi_2$. Then

$$f = f \cdot 1 = f(i_1 p_1 + i_2 p_2) = f i_1 p_1 + f i_2 p_2 = \varphi_1 p_1 + \varphi_2 p_2 = \langle \varphi_1, \varphi_2 \rangle.$$

Thus $A_1 \oplus A_2$ is simultaneously the product and coproduct of $A_1$ and $A_2$, with injections $i_1, i_2$ and projections $p_1, p_2$ related by $p_j i_k = \delta_{jk}$. This structure is called the **biproduct** or **direct sum**.
