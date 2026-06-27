---
role: proof
locale: en
of_concept: image-of-generators-under-surjection
source_book: gtm023
source_chapter: "1"
source_section: "2"
---

Since $\varphi$ is surjective, every vector $y \in F$ can be written as $y = \varphi x$ for some $x \in E$. Since $S$ generates $E$, there exist vectors $x_i \in S$ and scalars $\xi^i \in \Gamma$ such that
$$
x = \sum_i \xi^i x_i.
$$
Applying $\varphi$ and using linearity,
$$
y = \varphi x = \varphi\left(\sum_i \xi^i x_i\right) = \sum_i \xi^i \varphi x_i.
$$
This shows that every vector $y \in F$ is a linear combination of vectors in $\varphi(S)$. Hence $\varphi(S)$ is a system of generators for $F$.
