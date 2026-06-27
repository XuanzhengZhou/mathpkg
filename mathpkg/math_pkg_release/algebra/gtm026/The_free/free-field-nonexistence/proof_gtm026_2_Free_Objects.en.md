---
role: proof
locale: en
of_concept: free-field-nonexistence
source_book: gtm026
source_chapter: "2"
source_section: "Free Objects"
---

Suppose such a free field $(F, \eta)$ existed. Let $\mathbb{Z}_2$ be the two-element field and let $f: n \longrightarrow \mathbb{Z}_2 U$ be a bijection. From the universal property diagram and the dual of Proposition 1.42, $\eta$ is injective.

Now consider the zero morphism $0: n \longrightarrow F U$ that sends both elements of $n$ to $0_F \in F$. By the universal property, there exists a unique field homomorphism $\psi: F \longrightarrow F$ such that $0 = \eta \cdot (\psi U)$. Since $\eta$ is injective, the restriction of $\psi$ to the image of $\eta$ sends two distinct elements to $0_F$, which forces the kernel of $\psi$ to contain a nonzero element. Moreover, $\psi$ is a homomorphism of fields sending $1_F$ to $1_F$, so $\ker(\psi) \neq F$.

Thus $\ker(\psi)$ is a nontrivial proper ideal of $F$. This contradicts the fact that a field has no nontrivial ideals. Therefore, no free field over a two-element set exists.

The deeper reason for this failure is that field theory is not part of universal algebra: the multiplicative inverse operation is not defined at $0$, so fields cannot be presented by finitary total operations and equations.
