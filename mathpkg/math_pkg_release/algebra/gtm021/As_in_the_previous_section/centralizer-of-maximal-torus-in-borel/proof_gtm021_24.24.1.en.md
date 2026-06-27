---
role: proof
locale: en
of_concept: centralizer-of-maximal-torus-in-borel
source_book: gtm021
source_chapter: "24"
source_section: "24.1"
---
First we show that $W$ acts transitively. Let $B_1, B_2 \in \mathfrak{B}^T$. The conjugacy theorem shows that $xB_2x^{-1} = B_1$, for some $x \in G$. Since $xTx^{-1}$ and $T$ are maximal tori of $B_1$, there also exists $y \in B_1$, such that $yxTx^{-1}y^{-1} = T$, so $z = yx \in N_G(T)$. But $zB_2z^{-1} = B_1$, so the coset of $z$ in $W$ sends $B_2$ to $B_1$.

To say that $W$ acts simply transitively is just to say that the isotropy group in $W$ of $B \in \mathfrak{B}^T$ is trivial, i.e., that if $x \in N_G(T)$ satisfies $xBx^{-1} = B$, then $x \in C_G(T)$. But $N_G(B) = B$ (23.1), while $N_B(T) = C_B(T)$ (19.4), so this follows.
