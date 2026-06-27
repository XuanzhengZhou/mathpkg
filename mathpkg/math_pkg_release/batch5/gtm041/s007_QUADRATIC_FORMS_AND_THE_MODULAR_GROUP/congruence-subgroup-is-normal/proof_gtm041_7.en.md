---
role: proof
locale: en
of_concept: congruence-subgroup-is-normal
source_book: gtm041
source_chapter: ""
source_section: "Quadratic Forms and the Modular Group"
---

First, $\Gamma^{(n)}$ is a subgroup: the identity $I \in \Gamma^{(n)}$ since $I \equiv I \pmod{n}$. If $B_1, B_2 \in \Gamma^{(n)}$, then $B_1 \equiv I \pmod{n}$ and $B_2 \equiv I \pmod{n}$, so by the compatibility of matrix congruence with multiplication,
$$B_1B_2 \equiv I \cdot I = I \pmod{n},$$
hence $B_1B_2 \in \Gamma^{(n)}$. Also, if $B \equiv I \pmod{n}$, then by the compatibility of congruence with inversion,
$$B^{-1} \equiv I^{-1} = I \pmod{n},$$
so $B^{-1} \in \Gamma^{(n)}$. Thus $\Gamma^{(n)}$ is a subgroup.

For normality: let $A \in \Gamma$ and $B \in \Gamma^{(n)}$. Since $B \equiv I \pmod{n}$ and $A \equiv A \pmod{n}$, using the compatibility of congruence with multiplication and inversion,
$$A^{-1}BA \equiv A^{-1} I A = A^{-1}A = I \pmod{n}.$$
Therefore $A^{-1}BA \in \Gamma^{(n)}$, proving that $\Gamma^{(n)}$ is a normal subgroup of $\Gamma$.
