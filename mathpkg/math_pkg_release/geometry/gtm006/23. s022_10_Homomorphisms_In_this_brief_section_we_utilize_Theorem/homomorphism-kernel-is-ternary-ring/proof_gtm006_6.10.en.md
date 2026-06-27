---
role: proof
locale: en
of_concept: homomorphism-kernel-is-ternary-ring
source_book: gtm006
source_chapter: "6"
source_section: "10. Homomorphisms"
---

As described in the text, the proof proceeds by analyzing the set $Z = \{ x \in R_1 \mid (x, 0)_1^\phi = (0, 0)_2 \}$ and defining $J = \{ x \in R_1 \mid xz = 1 \text{ for some } z \in Z \}$. Set $\overline{R}_1 = R_1 \setminus J$.

One must verify that $T_1(x, y, z) \in \overline{R}_1$ whenever $x, y, z \in \overline{R}_1$, i.e., that $\overline{R}_1$ is closed under the ternary operation $T_1$ inherited from $(R_1, T_1)$. The verification uses the fact that the homomorphism $\phi$ preserves the PTR structure on the coordinate level: the compatibility of $\phi$ with the coordinatizing quadrangles implies that the ternary operation behaves well with respect to the partition of $R_1$ into $\overline{R}_1$ and $J$. The details are laborious but elementary; see Exercise 6.5.
