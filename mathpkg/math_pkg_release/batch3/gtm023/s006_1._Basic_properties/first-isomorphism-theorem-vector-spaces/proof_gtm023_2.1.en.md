---
role: proof
locale: en
of_concept: first-isomorphism-theorem-vector-spaces
source_book: gtm023
source_chapter: "2"
source_section: "§1. Basic properties, 2.4"
---
Since $\varphi(\ker \varphi) = 0$, applying the induced map theorem (sec. 2.3) with $E_1 = \ker \varphi$ and $F_1 = (0)$ yields a linear mapping $\bar{\varphi}: E/\ker \varphi \to F$ satisfying $\bar{\varphi} \circ \pi = \varphi$, where $\pi: E \to E/\ker \varphi$ is the canonical projection.

To show $\bar{\varphi}$ is injective, suppose $\bar{\varphi}(\bar{x}) = 0$ for some $\bar{x} \in E/\ker \varphi$. Write $\bar{x} = \pi(x)$. Then $0 = \bar{\varphi}(\pi(x)) = \varphi(x)$, so $x \in \ker \varphi$, which means $\bar{x} = \pi(x) = 0$ in $E/\ker \varphi$. Hence $\bar{\varphi}$ is injective.

Restricting the codomain of $\bar{\varphi}$ to $\operatorname{Im} \varphi$ gives the canonical isomorphism $E/\ker \varphi \cong \operatorname{Im} \varphi$.
