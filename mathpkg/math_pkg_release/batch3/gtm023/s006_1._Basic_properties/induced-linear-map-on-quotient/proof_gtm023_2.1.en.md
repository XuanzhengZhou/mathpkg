---
role: proof
locale: en
of_concept: induced-linear-map-on-quotient
source_book: gtm023
source_chapter: "2"
source_section: "§1. Basic properties, 2.3"
---
It follows from the assumptions that there is a well-defined set map $\bar{\varphi}: E/E_1 \to F/F_1$ satisfying $\bar{\varphi} \circ \pi_E = \pi_F \circ \varphi$. To prove that $\bar{\varphi}$ is linear, let $\bar{x}, \bar{y} \in E/E_1$ be arbitrary and choose vectors $x, y \in E$ such that $\pi_E(x) = \bar{x}$ and $\pi_E(y) = \bar{y}$. Then using the defining relation:

$$\bar{\varphi}(\lambda \bar{x} + \mu \bar{y}) = \bar{\varphi} \pi_E(\lambda x + \mu y) = \pi_F \varphi(\lambda x + \mu y) = \pi_F(\lambda \varphi(x) + \mu \varphi(y))$$
$$= \lambda \pi_F \varphi(x) + \mu \pi_F \varphi(y) = \lambda \bar{\varphi}(\bar{x}) + \mu \bar{\varphi}(\bar{y}).$$

Hence $\bar{\varphi}$ is a linear mapping. The relation $\bar{\varphi}(\bar{x}) = \overline{\varphi(x)}$ follows directly from the commutativity of the diagram.
