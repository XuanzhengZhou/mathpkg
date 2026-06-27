---
role: proof
locale: en
of_concept: proposition-1-11
source_book: gtm040
source_chapter: "1"
source_section: "11"
---

**Proof:** We prove only the first identity since the others are similar.

$$(C_1)_{ij} = C_{ij} = \sum_{m \in M} A_{im}B_{mj} = \sum_{m \in M'} A_{im}B_{mj} + \sum_{m \in M'} A_{im}B_{mj}$$
$$= (A_1B_1)_{ij} + (A_2B_3)_{ij}.$$

Notice that if the submatrix $A_1$ has at least one infinite index set, then the representation of $A$ by

$$A = \begin{pmatrix} A_1 & A_2 \\ A_3 & A_4 \end{pmatrix}$$

is not the standard one

$$A = \begin{pmatrix} A_{00} & A_{01} & \ldots \\ A_{10} & A_{11} & \ldots \\ \vdots & \vdots & \ldots \end{pmatrix}.$$

The ordering on the index sets of $A$ is not of the same type as that of the non-negative integers. We recall once more, however, that the fundamental properties of matrices are independent of any orderings on the index sets. It is only the representation of a matrix as an array which requires these orderings.

Limits of matrices play an important part in the study of denumerable Markov chains. We shall touch only briefly at this time on the problems involved.
