---
role: proof
locale: en
of_concept: factoring-via-kernel-containment
source_book: gtm023
source_chapter: "2"
source_section: "§1. Basic properties, 2.4"
---
Since $\psi$ maps $\ker \varphi$ into $0$, it induces a linear mapping $\bar{\psi}: E/\ker \varphi \to G$ such that
$$\bar{\psi} \circ \pi = \psi$$
where $\pi: E \to E/\ker \varphi$ is the canonical projection.

Let $\bar{\varphi}: E/\ker \varphi \xrightarrow{\cong} \operatorname{Im} \varphi$ be the linear isomorphism determined by $\varphi$ (by the first isomorphism theorem), and define a linear mapping $\bar{\psi}_1: \operatorname{Im} \varphi \to G$ by
$$\bar{\psi}_1 = \bar{\psi} \circ \bar{\varphi}^{-1}.$$

Finally, let $\chi: F \to G$ be any linear mapping which extends $\bar{\psi}_1$ (this is possible since $\operatorname{Im} \varphi$ is a subspace of $F$). Then we have
$$\bar{\varphi}^{-1} \circ \varphi = \bar{\varphi}^{-1} \circ \bar{\varphi} \circ \pi = \pi,$$
whence
$$\chi \circ \varphi = \bar{\psi}_1 \circ \varphi = \bar{\psi} \circ \bar{\varphi}^{-1} \circ \varphi = \bar{\psi} \circ \pi = \psi.$$
Thus $\psi$ factors through $\varphi$.
