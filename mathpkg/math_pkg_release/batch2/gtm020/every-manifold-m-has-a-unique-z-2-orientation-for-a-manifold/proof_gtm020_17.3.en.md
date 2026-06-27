---
locale: en
of_concept: every-manifold-m-has-a-unique-z-2-orientation-for-a-manifold
role: proof
source_book: gtm020
source_chapter: 17. Chern Classes and Stiefel-Whitney Classes
source_section: '3'
---

Let $\omega_x$ be the nonzero element of $H_n(M, M - x; Z_2)$. Then for a ball $W$ around $x$ in the domain of a chart we have $H_n(M, M - W; Z_2) = Z_2$, and the nonzero element is mapped onto $\omega_y$ for each $y \in W$. This proves the first statement.

For the equivalence of statements (1) to (3), we begin by assuming (2). Then for a $Z$-orientation of $M$ we define $\omega_x = (\phi^{-1})_*(\alpha_n)$, where $\alpha_n \in H_n(\phi(U), \phi(U) - \phi(x))$ is the canonical class used in (3.4), and $(U, \phi) \in A$. By (3.4) and (2), change of coordinate is orientation preserving, and $\omega$ is a well-defined orientation. Conversely, let $A$ be the atlas of those charts such that $\omega_x = (\phi^{-1})_*(\alpha_n)$ for $x \in U$ and $\alpha_n \in H_n(\phi(U), \phi(U) - \phi(x))$. This verifies the equivalence of (1) and (2).

To see that (2) implies (3), observe that the transition functions $D(\psi \phi^{-1})(\phi(x))$, where $x \in U \cap V$, have a positive determinant and are homotopic to transition functions in $

Proof. We consider for which compact sets $K \subset M$ the theorem is true. First, we prove that if the theorem is true for $K_1, K_2$, and $K_1 \cap K_2$ it is true for $K_1 \cup K_2$. Let $K$ denote $K_1 \cup K_2$ and $L$ denote $K_1 \cap K_2$. The Mayer-Vietoris sequence has the following form (see Eilenberg and Steenrod [1]).

$$\cdots \rightarrow H_{i+1}(M, M-L) \xrightarrow{c} H_i(M, M-K)$$
$$\xrightarrow{u} H_i(M, M-K_1) \oplus H_i(M, M-K_2) \xrightarrow{v} \cdots$$

Recall that $u(a) = (r_1(a), r_2(a))$, and $v(a, b) = r'_1(a) - r'_2(b)$. Then, clearly, we have $H_i(M, M-K) = 0$ for $i > n$. For the next statement, if each $r(a) = 0$ in $H_n(M, M-x)$, we have $u(a) = 0$. Since $H_{n+1}(M, M-L) = 0$, we have $a = 0$. Finally, the existence of $\omega_K$ follows from the fact that $v(\omega_{K_1}, \omega_{K_2}) = 0$, and the uniqueness of $\omega_K$ follows from the previous statement.

Next we suppose that $K \subset U$, where $(U, \phi)$ is a coordinate chart with $\phi(K)$ a convex set in $\phi(U) \subset \mathbf{R}^n$. Since $\phi(U) - \phi(K) \rightarrow \phi(U) - \phi(x)$ is a homotopy equivalence, the induced homomorphisms $H_i(M, M-K) \rightarrow H_i(M, M-x)$ are isomorphisms. For these $K$ the theorem follows. Using the result of the first paragraph, the theorem holds for compact sets $K \subset U$, where $(U, \phi
