---
role: proof
locale: en
of_concept: dual-generalized-eigenspaces
source_book: gtm023
source_chapter: "13"
source_section: "13.8"
---
Let $y^* \in F_i^*$ be arbitrarily chosen. For each $x \in E_i$, we have
$$\langle f_i^{k_i}(\varphi^*) y^*, x \rangle = \langle y^*, f_i^{k_i}(\varphi) x \rangle = \langle y^*, 0 \rangle = 0,$$
since $x \in E_i = K(f_i^{k_i})$ implies $f_i^{k_i}(\varphi)x = 0$.

In view of the duality between $E_i$ and $F_i^*$ (which follows from the definitions and sec. 2.30), the fact that $f_i^{k_i}(\varphi^*)y^*$ annihilates all of $E_i$ under the pairing implies $f_i^{k_i}(\varphi^*)y^* = 0$; i.e.,
$$y^* \in E_i^*.$$

This establishes $F_i^* \subset E_i^*$. Comparing the decompositions (13.23) and (13.25) and using dimension considerations yields equality $F_i^* = E_i^*$.
