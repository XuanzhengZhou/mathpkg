---
role: proof
locale: en
of_concept: projection-kernel-image-direct-sum
source_book: gtm023
source_chapter: "2"
source_section: "4"
---

Let $x \in E$ be an arbitrary vector. Writing

$$
x = y + \varphi x \quad \text{i.e.} \quad y = x - \varphi x
$$

we obtain that

$$
\varphi y = \varphi x - \varphi^2 x = 0
$$

whence $y \in \ker \varphi$. It follows that

$$
E = \ker \varphi + \operatorname{Im} \varphi. \tag{2.30}
$$

To show that the decomposition (2.30) is direct, let $z = \varphi x$ be an arbitrary vector of $\ker \varphi \cap \operatorname{Im} \varphi$. Then we have that

$$
0 = \varphi z = \varphi^2 x = \varphi x = z
$$

and thus $\ker \varphi \cap \operatorname{Im} \varphi = 0$.

To prove the representation $\varphi = \iota_{\operatorname{Im} \varphi} \oplus 0_{\ker \varphi}$ (equation (2.29)), we observe that the subspaces $\operatorname{Im} \varphi$ and $\ker \varphi$ are stable under $\varphi$ and that the induced transformations are the identity and the zero mapping respectively.
