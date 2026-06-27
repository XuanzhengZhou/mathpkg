---
role: proof
locale: en
of_concept: minus-part-injectivity
source_book: gtm059
source_chapter: "3"
source_section: "4.6 The (±1)-conjectures"
---

Let $K = \mathbb{Q}(\zeta_m)$ and let $\tau$ denote complex conjugation. Let $C_K$ be the ideal class group of $K$. The minus eigenspace is defined as

$$
C_K^- = \{ c \in C_K : c^{1+\tau} = 1 \}.
$$

Since $C_K^- \subseteq C_K$ by definition, the inclusion map $\iota: C_K^- \to C_K$ is trivially injective. To verify that $C_K^-$ is indeed a subgroup of $C_K$, let $c_1, c_2 \in C_K^-$. Then $c_1^{1+\tau} = 1$ and $c_2^{1+\tau} = 1$, so

$$
(c_1 c_2^{-1})^{1+\tau} = c_1^{1+\tau} (c_2^{-1})^{1+\tau} = 1 \cdot 1 = 1,
$$

which shows $c_1 c_2^{-1} \in C_K^-$, confirming that $C_K^-$ is a subgroup of $C_K$, and hence the inclusion is injective.

Consequently, $h^- = |C_K^-|$ is an integer dividing $h_K = |C_K|$.
