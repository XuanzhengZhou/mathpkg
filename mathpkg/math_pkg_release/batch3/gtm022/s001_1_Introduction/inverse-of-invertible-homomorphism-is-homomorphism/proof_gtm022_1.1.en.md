---
role: proof
locale: en
of_concept: inverse-of-invertible-homomorphism-is-homomorphism
source_book: gtm022
source_chapter: "I"
source_section: "§1 Introduction"
---

Let $\varphi: A \rightarrow B$ be an invertible homomorphism of $T$-algebras. Take any $n \in \mathbb{N}$, any $t \in T_n$, and any $b_1, \ldots, b_n \in B$. Let $a_i = \varphi^{-1}(b_i)$ for $i = 1, \ldots, n$, so $\varphi(a_i) = b_i$. Since $\varphi$ is a homomorphism,
$$\varphi(t_A(a_1, \ldots, a_n)) = t_B(\varphi(a_1), \ldots, \varphi(a_n)) = t_B(b_1, \ldots, b_n).$$
Applying $\varphi^{-1}$ to both sides,
$$t_A(a_1, \ldots, a_n) = \varphi^{-1}(t_B(b_1, \ldots, b_n)).$$
But $a_i = \varphi^{-1}(b_i)$, so
$$t_A(\varphi^{-1}(b_1), \ldots, \varphi^{-1}(b_n)) = \varphi^{-1}(t_B(b_1, \ldots, b_n)).$$
Thus $\varphi^{-1}$ preserves the operations and is a homomorphism.
