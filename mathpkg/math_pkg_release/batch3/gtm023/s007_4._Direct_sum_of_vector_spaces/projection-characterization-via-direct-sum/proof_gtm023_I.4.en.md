---
role: proof
locale: en
of_concept: projection-characterization-via-direct-sum
source_book: gtm023
source_chapter: "I"
source_section: "4. Direct sum of vector spaces"
---

**Proof.** ($\Rightarrow$) Assume $\varphi^2 = \varphi$. Let $x \in E$ be arbitrary and write $x = y + \varphi x$, so $y = x - \varphi x$. Then
$$\varphi y = \varphi x - \varphi^2 x = 0,$$
so $y \in \ker \varphi$. It follows that
$$E = \ker \varphi + \operatorname{Im} \varphi.$$

To show the sum is direct, let $z = \varphi x \in \ker \varphi \cap \operatorname{Im} \varphi$. Then
$$0 = \varphi z = \varphi^2 x = \varphi x = z,$$
so $\ker \varphi \cap \operatorname{Im} \varphi = 0$. Hence $E = \ker \varphi \oplus \operatorname{Im} \varphi$.

The subspaces $\operatorname{Im} \varphi$ and $\ker \varphi$ are stable under $\varphi$, and the induced transformations are the identity and the zero mapping respectively. Therefore,
$$\varphi = \iota_{\operatorname{Im} \varphi} \oplus 0_{\ker \varphi}.$$

($\Leftarrow$) Conversely, if $E = E_1 \oplus E_2$ is a direct decomposition, define $\varphi = \iota_{E_1} \oplus 0_{E_2}$. For any $x = x_1 + x_2$ with $x_i \in E_i$,
$$\varphi^2(x_1 + x_2) = \varphi(x_1) = x_1 = \varphi(x_1 + x_2),$$
so $\varphi^2 = \varphi$, and $\varphi$ is a projection operator. $\square$
