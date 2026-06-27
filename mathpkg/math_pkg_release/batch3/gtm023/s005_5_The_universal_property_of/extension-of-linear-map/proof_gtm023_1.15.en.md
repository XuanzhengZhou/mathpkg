---
role: proof
locale: en
of_concept: extension-of-linear-map
source_book: gtm023
source_chapter: "1"
source_section: "1.15"
---

Let $E_2$ be a complementary subspace for $E_1$ in $E$,

$$E = E_1 \oplus E_2$$

and define $\varphi$ by

$$\varphi x = \varphi_1 y$$

where

$$x = y + z$$

is the decomposition of $x$ determined by the direct sum ($y \in E_1$, $z \in E_2$). Then

$$\varphi \sum_{i} \lambda^{i} x_{i} = \varphi \left( \sum_{i} \lambda_{i} y_{i} + \sum_{i} \lambda_{i} z_{i} \right) = \varphi_1 \sum_{i} \lambda^{i} y_{i} = \sum_{i} \lambda^{i} \varphi_1 y_{i} = \sum_{i} \lambda^{i} \varphi x_{i}$$

and so $\varphi$ is linear. It is trivial that $\varphi$ extends $\varphi_1$.
