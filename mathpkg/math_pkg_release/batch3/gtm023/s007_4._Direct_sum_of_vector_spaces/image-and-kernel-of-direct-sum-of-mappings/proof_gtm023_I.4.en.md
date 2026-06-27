---
role: proof
locale: en
of_concept: image-and-kernel-of-direct-sum-of-mappings
source_book: gtm023
source_chapter: "I"
source_section: "4. Direct sum of vector spaces"
---

**Proof.** By definition, $(\varphi_1 \oplus \varphi_2)(x_1, x_2) = (\varphi_1 x_1, \varphi_2 x_2)$. 

For the image: if $(y_1, y_2) \in \operatorname{Im}(\varphi_1 \oplus \varphi_2)$, then there exists $(x_1, x_2) \in E_1 \oplus E_2$ such that $y_1 = \varphi_1 x_1$ and $y_2 = \varphi_2 x_2$, so $y_1 \in \operatorname{Im} \varphi_1$ and $y_2 \in \operatorname{Im} \varphi_2$, hence $(y_1, y_2) \in \operatorname{Im} \varphi_1 \oplus \operatorname{Im} \varphi_2$. Conversely, if $y_1 = \varphi_1 x_1$ and $y_2 = \varphi_2 x_2$, then $(y_1, y_2) = (\varphi_1 \oplus \varphi_2)(x_1, x_2) \in \operatorname{Im}(\varphi_1 \oplus \varphi_2)$.

For the kernel: $(x_1, x_2) \in \ker(\varphi_1 \oplus \varphi_2)$ if and only if $(\varphi_1 x_1, \varphi_2 x_2) = (0, 0)$, which means $\varphi_1 x_1 = 0$ and $\varphi_2 x_2 = 0$, i.e., $x_1 \in \ker \varphi_1$ and $x_2 \in \ker \varphi_2$, so $(x_1, x_2) \in \ker \varphi_1 \oplus \ker \varphi_2$. $\square$
