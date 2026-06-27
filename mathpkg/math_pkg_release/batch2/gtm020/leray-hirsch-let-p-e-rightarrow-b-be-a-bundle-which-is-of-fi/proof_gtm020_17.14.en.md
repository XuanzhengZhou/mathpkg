---
locale: en
of_concept: leray-hirsch-let-p-e-rightarrow-b-be-a-bundle-which-is-of-fi
role: proof
source_book: gtm020
source_chapter: 17. Chern Classes and Stiefel-Whitney Classes
source_section: '14'
---

For an open subset $U$ of $B$, let $E_U$ denote $p^{-1}(U)$, let $j_U: E_U \rightarrow E$ be the natural inclusion, and let $p_U: E_U \rightarrow

directly from the Künneth formula. Consequently, the theorem is true over such an open set $U$.

Finally, it suffices to prove that if the theorem is true over open sets $U$, $V$, and $U \cap V$ it is true over $U \cap V$. To do this, we define two functors $K^n(U)$ and $L^n(U)$ on the open subsets $U$ of $B$. Let $n(i)$ denote the degree of $a_i$, and let $x_i$ denote an indeterminant of degree $n(i)$. Let $K^n(U)$ be the direct sum $\sum_{1 \leq i \leq r} H^{n-i}(U)x_i$, let $L^n(U)$ denote $H^n(E_U, E_U \cap E_0)$, and the $\theta_U: K^n(U) \rightarrow L^n(U)$ be the morphism defined by the relation $\theta_U \left( \sum_i c_i x_i \right) = \sum_i p^*(c_i)a_i$, where $c_i \in H^{n-i}(U)$. Observe that the theorem is true over $U$ if and only if $\theta_U$ is an isomorphism.

Since $L^n(U)$ is constructed from a functor for which the Mayer-Vietoris sequence exists and is exact, and since $K^n(U)$ is a direct sum of functors for which the Mayer-Vietoris sequence exists and is exact, we have the following commutative diagram with exact rows.

$$\begin{array}{ccc}
\cdots & K^n(U \cap V) & K^n(U) \oplus K^n(V) \\
\theta_1 & \theta_2 = \theta \oplus \theta \\
L^n(U \cap V) & L^n(U) \oplus L^n(V) \\
K^n(U \cup V) & K^{n-1}(U \cap V) & K^{n-1}(U) \oplus K^{n-1}(V) \\
\theta_3 & \theta_4 & \theta_5 \\
L^n(U \cup V) & L^{n-1}(U \cap V) &
