---
role: proof
locale: en
of_concept: minimal-separating-set-planarity-g3-g3
source_book: gtm054
source_chapter: "4"
source_section: "Section 13"
---

If $\Gamma$ is planar, then so are $\Gamma_1$ and $\Gamma_2$ by E15.

The converse follows from E17 in the case $|W| = 1$. We will prove the converse in the case $|W| = 3$, leaving the simpler case $|W| = 2$ to the reader.

Let $W = \{x_1, x_2, x_3\}$, and let $\{x_0, e_1, e_2, e_3\}$ be a set of four distinct elements disjoint from all sets in question. For $j = 1, 2$, let $V_j = U_j + W + \{x_0\}$; let $F_1$ be the edge set of $\Gamma_{W+U_1}$; let $F_2 = E + F_1$; let $E_j = F_j \cup \{e_1, e_2, e_3\}$; and finally let $\Theta_j = (V_j, f_j, E_j)$ where

$$f_j(e) = \begin{cases} \{x_0, x_i\} & \text{if } e = e_i \ (i = 1, 2, 3); \\ f(e) & \text{otherwise} \end{cases}$$

(see Figure G4). One easily sees that $\Theta_j$ is a subcontraction of $\Gamma$.
