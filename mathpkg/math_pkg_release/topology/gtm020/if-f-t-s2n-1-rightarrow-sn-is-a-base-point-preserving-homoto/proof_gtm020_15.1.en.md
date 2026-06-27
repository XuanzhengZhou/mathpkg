---
locale: en
of_concept: if-f-t-s2n-1-rightarrow-sn-is-a-base-point-preserving-homoto
role: proof
source_book: gtm020
source_chapter: 15. The Hopf Invariant
source_section: '1'
---

We view $f_t$ as a map $f: (S^{2n-1} \times I)_* \rightarrow S^n$, and then we have the following commutative diagram of spaces and maps for each $t \in I$:

$$\begin{array}{cccccccc}
(S^{2n-1} \times I)_* & f & S^n & C_f & S(S^{2n-1} \times I)_* & SS^n \\
\uparrow j_t & \uparrow 1 & \uparrow k_t & \uparrow S_j_t & \uparrow 1 \\
S^{2n-1} & f_t & S^n & C_f

is the map pinching the equator to a point. Let $q_i: S^{2n-1} \rightarrow S^{2n-1} \vee S^{2n-1}$ denote the inclusion maps into the coproduct, let $g$ denote the map $(f_1 \vee f_2)\theta$, and let $r_i: C_{f_i} \rightarrow C_g$ denote the inclusion map induced by $q_i$. We have the following commutative diagrams of $K$-groups for $i = 1$ and 2:

$$\tilde{K}(C_g) \leftarrow \tilde{K}(S^{2n}) \leftarrow 0$$
$$\tilde{K}(S^n) \leftarrow \tilde{K}(C_{f_1 \vee f_2}) \leftarrow \tilde{K}(S^{2n}) \oplus \tilde{K}(S^{2n}) \leftarrow 0$$
$$\tilde{K}(C_{f_i}) \leftarrow \tilde{K}(S^{2n}) \leftarrow 0$$

As a group, $\tilde{K}(C_{f_1 \vee f_2})$ has three free generators $a, b_1$, and $b_2$, where $r_1^!(a) = a(f_1)$, $r_2^!(a) = a(f_2)$, $r_1^!(b_1) = b(f_1)$, $r_2^!(b_2) = b(f_2)$, and $r_1^!(b_2) = r_2^!(b_1) = 0$. The ring structure is given by $ab_1 = ab_2 = b_1^2 = b_2^2 = 0$ and $a^2 = h_1b_1 + h_2b_2$, where $h_1, h_2 \in \mathbb{Z}$. By commutativity of the lower square, $a(f_i)^2 = r_i^!(a)^2 = h_i r_i^!(b_i) = h(f_i)b(f_i)$ or $h_i = h(f_i)$ for $i = 1, 2$. Finally,
