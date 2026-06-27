---
role: proof
locale: en
of_concept: direct-sum-decomposition-yields-projection
source_book: gtm023
source_chapter: "2"
source_section: "4"
---

Given $E = E_1 \oplus E_2$, define $\varphi = \iota_{E_1} \oplus 0_{E_2}$. For any $x = x_1 + x_2$ with $x_1 \in E_1$, $x_2 \in E_2$, we have

$$
\varphi(x) = \varphi(x_1 + x_2) = \iota_{E_1}(x_1) + 0_{E_2}(x_2) = x_1.
$$

Then

$$
\varphi^2(x) = \varphi(x_1) = x_1 = \varphi(x),
$$

so $\varphi$ is idempotent. Since the identity and zero maps are linear and the direct sum of linear maps is linear, $\varphi$ is a projection operator.
