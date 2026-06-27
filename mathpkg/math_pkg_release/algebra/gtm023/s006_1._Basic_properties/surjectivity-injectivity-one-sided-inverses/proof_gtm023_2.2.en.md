---
role: proof
locale: en
of_concept: surjectivity-injectivity-one-sided-inverses
source_book: gtm023
source_chapter: "2"
source_section: "§2. Operations with linear mappings, 2.11"
---
**Injectivity.** Suppose $\varphi$ has a left inverse $\psi$, so $\psi \circ \varphi = \iota_E$. If $\varphi(x) = 0$, then $x = \psi(\varphi(x)) = \psi(0) = 0$, so $\varphi$ is injective.

Conversely, if $\varphi$ is injective, consider the restriction $\varphi_1$ of $\varphi$ to $E$, mapping onto $\operatorname{Im} \varphi$. Then $\varphi_1: E \xrightarrow{\cong} \operatorname{Im} \varphi$ is a linear isomorphism. Let $\pi: F \to \operatorname{Im} \varphi$ be a linear projection (i.e., a linear map such that $\pi(y) = y$ for $y \in \operatorname{Im} \varphi$, which exists by Corollary II of Proposition I, sec. 1.15). Define $\psi: F \to E$ by
$$\psi = \varphi_1^{-1} \circ \pi.$$

Then for any $x \in E$,
$$\psi(\varphi(x)) = \varphi_1^{-1}(\pi(\varphi(x))) = \varphi_1^{-1}(\varphi(x)) = \varphi_1^{-1}(\varphi_1(x)) = x,$$
so $\psi \circ \varphi = \iota_E$. Hence $\varphi$ has a left inverse.

**Surjectivity.** If $\varphi$ has a right inverse $\psi$, so $\varphi \circ \psi = \iota_F$, then for every $y \in F$ we have $y = \varphi(\psi(y))$, hence $y \in \operatorname{Im} \varphi$, so $\varphi$ is surjective.

Conversely, if $\varphi$ is surjective, let $E_1$ be a complementary subspace of $\ker \varphi$ in $E$, so $E = E_1 \oplus \ker \varphi$. The restriction $\varphi|_{E_1}: E_1 \to F$ is then a linear isomorphism. Define $\psi: F \to E$ as the composition of the inverse of this restriction with the inclusion $E_1 \hookrightarrow E$. Then $\varphi \circ \psi = \iota_F$, so $\varphi$ has a right inverse.
