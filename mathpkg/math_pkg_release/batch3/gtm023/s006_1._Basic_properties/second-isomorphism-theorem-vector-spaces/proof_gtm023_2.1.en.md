---
role: proof
locale: en
of_concept: second-isomorphism-theorem-vector-spaces
source_book: gtm023
source_chapter: "2"
source_section: "§1. Basic properties, 2.4"
---
Consider the canonical projection
$$\pi: E_1 + E_2 \to (E_1 + E_2)/E_2$$
and let $\varphi$ be the restriction of $\pi$ to $E_1$, so $\varphi: E_1 \to (E_1 + E_2)/E_2$. Then $\varphi$ is surjective. Indeed, if $x = x_1 + x_2$ with $x_1 \in E_1, x_2 \in E_2$ is any vector of $E_1 + E_2$, we have
$$\pi(x) = \pi(x_1 + x_2) = \pi(x_1) = \varphi(x_1).$$

Now compute the kernel:
$$\ker \varphi = \ker \pi \cap E_1 = E_2 \cap E_1.$$

By the first isomorphism theorem, $\varphi$ induces a linear isomorphism
$$\bar{\varphi}: E_1 / (E_1 \cap E_2) \xrightarrow{\cong} (E_1 + E_2) / E_2.$$

If $E = E_1 \oplus E_2$, then $E_1 \cap E_2 = 0$ and $E_1 + E_2 = E$, so the formula reduces to $E_1 \cong E/E_2$.
