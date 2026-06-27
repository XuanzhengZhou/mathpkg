---
role: proof
locale: en
of_concept: automorphism-group-dual-isomorphism
source_book: gtm054
source_chapter: "II Algebraic Structures on Finite Sets"
source_section: "IIE The Automorphism Groups of Systems"
---

Consider the dual system $\Lambda^* = (E, f^*, V)$ where $f^*(x) = \{e \in E : x \in f(e)\}$ for $x \in V$. The automorphism group $G(\Lambda^*)$ consists of pairs $(q, p)$ with $q \in \Pi(E)$, $p \in \Pi(V)$ such that $p[f^*(x)] = f^*(q(x))$ for all $x \in V$.

Define $\varphi: G(\Lambda) \to G(\Lambda^*)$ by $\varphi(p, q) = (q, p)$. This map is well-defined because the condition $q[f(e)] = f(p(e))$ for all $e \in E$ is equivalent, by duality, to $p[f^*(x)] = f^*(q(x))$ for all $x \in V$. The map $\varphi$ is clearly a bijection and preserves the group operation:
$$\varphi((p_2, q_2)(p_1, q_1)) = \varphi(p_2p_1, q_2q_1) = (q_2q_1, p_2p_1) = (q_2, p_2)(q_1, p_1) = \varphi(p_2, q_2)\varphi(p_1, q_1).$$

Thus $\varphi$ is a group isomorphism, and $G(\Lambda) \cong G(\Lambda^*)$ as abstract groups.
