---
role: proof
locale: en
of_concept: block-multiplication-matrices
source_book: gtm040
source_chapter: "1"
source_section: "1"
---

We prove only the first identity since the others are similar. For $i \in K'$ and $j \in N'$:

$$(C_1)_{ij} = C_{ij} = \sum_{m \in M} A_{im} B_{mj} = \sum_{m \in M'} A_{im} B_{mj} + \sum_{m \in \tilde{M}'} A_{im} B_{mj} = (A_1 B_1)_{ij} + (A_2 B_3)_{ij}.$$

The first equality holds because $C_1$ is the restriction of $C$ to $K' \times N'$. The second equality is the definition of matrix multiplication. The third splits the sum over $M$ into the sum over $M'$ and its complement $\tilde{M}'$. The fourth identifies these partial sums as the entries of the block products $A_1 B_1$ and $A_2 B_3$ respectively. The other three identities follow by the same reasoning with different index restrictions.
