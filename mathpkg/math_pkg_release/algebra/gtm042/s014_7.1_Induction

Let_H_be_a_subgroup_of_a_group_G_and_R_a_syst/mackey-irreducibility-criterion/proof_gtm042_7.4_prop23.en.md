---
role: proof
locale: en
of_concept: mackey-irreducibility-criterion
source_book: gtm042
source_chapter: "7"
source_section: "7.4"
---

We apply Mackey's formula (Section 7.3) to the case $K = H$. For $s \in G$, denote by $H_s$ the subgroup $sHs^{-1} \cap H$ of $H$. The representation $\rho$ of $H$ defines a representation $\operatorname{Res}_s(\rho)$ by restriction to $H_s$, which should not be confused with the representation $\rho^s$ defined in Section 7.3.

Computing the intertwining number $\langle V, V \rangle_G$ using the scalar product of characters and applying the decomposition from Section 7.3, one obtains a sum over double coset representatives $s \in H \backslash G / H$. For $s = 1$ the contribution is $d_1 = \langle \rho, \rho \rangle_H \geqslant 1$. For $s \neq 1$, the contribution $d_s$ is the intertwining number of $\operatorname{Res}_s(\rho)$ and $\rho^s$ on $H_s$.

In order that $\langle V, V \rangle_G = 1$ (which characterizes irreducibility), it is thus necessary and sufficient that $d_1 = 1$ (i.e., $W$ is irreducible) and $d_s = 0$ for all $s \neq 1$ in $H \backslash G / H$ (i.e., the two representations are disjoint). These are exactly conditions (a) and (b).
