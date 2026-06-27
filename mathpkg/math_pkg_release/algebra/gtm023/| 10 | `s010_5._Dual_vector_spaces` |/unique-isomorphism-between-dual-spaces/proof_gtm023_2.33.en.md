---
role: proof
locale: en
of_concept: unique-isomorphism-between-dual-spaces
source_book: gtm023
source_chapter: "II"
source_section: "2.33"
---

Let $\Phi_1: E_1^* \rightarrow L(E)$ and $\Phi_2: E_2^* \rightarrow L(E)$ be the canonical injections. By Proposition I, both $\Phi_1$ and $\Phi_2$ are linear isomorphisms since $\dim E$ is finite. Define $\varphi = \Phi_2^{-1} \circ \Phi_1: E_1^* \rightarrow E_2^*$. Then $\varphi$ is a linear isomorphism, and for all $x^* \in E_1^*, x \in E$,

$$\langle \varphi x^*, x \rangle = \langle \Phi_2^{-1}(\Phi_1 x^*), x \rangle = (\Phi_1 x^*)(x) = \langle x^*, x \rangle.$$

Uniqueness follows because if $\varphi_1, \varphi_2$ both satisfy the condition, then $\langle (\varphi_1 - \varphi_2)x^*, x \rangle = 0$ for all $x$, so $(\varphi_1 - \varphi_2)x^* = 0$ for all $x^*$, hence $\varphi_1 = \varphi_2$.
