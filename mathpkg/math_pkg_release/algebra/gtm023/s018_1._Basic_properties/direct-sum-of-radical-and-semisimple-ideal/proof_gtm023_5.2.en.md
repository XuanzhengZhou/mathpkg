---
role: proof
locale: en
of_concept: direct-sum-of-radical-and-semisimple-ideal
source_book: gtm023
source_chapter: "5"
source_section: "§2. Ideals"
---

Let $B$ be a complementary ideal for $\operatorname{rad} A$, so $A = \operatorname{rad} A \oplus B$. Since $B \cong A/\operatorname{rad} A$, $B$ contains no nonzero nilpotent elements, hence $B^2 \neq 0$. By the hereditary property, $B$ is totally reducible and therefore semisimple.

To show $(\operatorname{rad} A)^2 = 0$, let $k$ be the degree of nilpotency of $\operatorname{rad} A$, so $(\operatorname{rad} A)^k = 0$. Then $(\operatorname{rad} A)^{k-1}$ is an ideal in $\operatorname{rad} A$, and there exists a complementary ideal $J$ with $(\operatorname{rad} A)^{k-1} \oplus J = \operatorname{rad} A$. Now:

$$
(\operatorname{rad} A^{k-1})^2 = \operatorname{rad} A^k = 0,
$$
$$
J \cdot (\operatorname{rad} A)^{k-1} = 0,
$$
$$
J^{k-1} \subset (\operatorname{rad} A)^{k-1} \cap J = 0.
$$

These relations yield $(\operatorname{rad} A)^{\max(2, k-1)} = 0$. But $(\operatorname{rad} A)^{k-1} \neq 0$, so $(\operatorname{rad} A)^2 = 0$.
