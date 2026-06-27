---
role: proof
locale: en
of_concept: existence-of-symplectic-basis
source_book: gtm023
source_chapter: "11"
source_section: "7"
---

The proof is left as an exercise to the reader in the source text. The standard argument proceeds by induction on $2n = \dim E$:

For $n=0$, the empty basis is symplectic.

Assume the result holds for all symplectic spaces of dimension $<2n$. Let $E$ be a symplectic space of dimension $2n$. By non-degeneracy of $\langle\, , \,\rangle$, there exist vectors $a_1, b_1' \in E$ such that $\langle a_1, b_1' \rangle \neq 0$. Rescaling, choose $b_1$ such that $\langle a_1, b_1 \rangle = 1$. Note that $a_1$ and $b_1$ are linearly independent: if $b_1 = \lambda a_1$, then $\langle a_1, b_1 \rangle = \lambda \langle a_1, a_1 \rangle = 0$ by skew-symmetry, contradiction.

Define $E_1 = \operatorname{span}\{a_1, b_1\}$ and let $E_1^\perp = \{x \in E : \langle x, a_1 \rangle = 0,\ \langle x, b_1 \rangle = 0\}$. Since $\langle\, , \,\rangle$ is non-degenerate, $E = E_1 \oplus E_1^\perp$ and the restriction of $\langle\, , \,\rangle$ to $E_1^\perp$ is again a non-degenerate skew-symmetric bilinear form. Thus $E_1^\perp$ is a symplectic space of dimension $2(n-1)$. By induction hypothesis, $E_1^\perp$ has a symplectic basis $a_2, \ldots, a_n, b_2, \ldots, b_n$. Together with $a_1, b_1$, this yields a symplectic basis of $E$.
