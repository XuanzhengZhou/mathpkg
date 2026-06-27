---
role: proof
locale: en
of_concept: local-triviality-of-stiefel-projection
source_book: gtm020
source_chapter: "8"
source_section: "3"
---

For each $W \in G_k(F^n)$, let $O(W)$ denote the open set of all $W' \in G_k(F^n)$ such that the orthogonal projection $\pi_{W'}$ restricted to $W$ is an isomorphism. For $W = \langle v_1, \ldots, v_k \rangle$, we define a linear inner-product preserving map

$$f_{(v_1,\ldots,v_k),W'}: W \to F^n$$

with $f(W) = W'$, continuous in $(v_1,\ldots,v_k) \in V_k(F^n)$ and $W' \in O(W)$, by requiring

$$f_{(v_1,\ldots,v_k),W'}(v_i) = v'_i$$

where $(v'_1,\ldots,v'_k) = GS(\pi_{W'}(v_1),\ldots,\pi_{W'}(v_k))$ is the Gram-Schmidt orthonormalization of the projections. This is well-defined by Proposition 3.1.

Now define a map on the local product:

$$O(W) \times V_k(F^k) \to p^{-1}(O(W))$$

by sending $(W', (a_1,\ldots,a_k))$ to $(\sum_i a_{i1} v'_i,\ldots,\sum_i a_{ik} v'_i)$ where $(v'_i) = f_{(v_1,\ldots,v_k),W'}(v_i)$. Since $V_k(F^k) = U_F(k)$, this gives a homeomorphism

$$O(W) \times U_F(k) \xrightarrow{\cong} p^{-1}(O(W))$$

compatible with the right $U_F(k)$-action on fibres. The inverse map sends a frame $(w_1,\ldots,w_k) \in p^{-1}(W')$ to the pair $(W', a)$, where $a \in U_F(k)$ is the transition matrix between $(v'_1,\ldots,v'_k)$ and $(w_1,\ldots,w_k)$. This proves local triviality, and $(V_k(F^n), p, G_k(F^n))$ is a locally trivial principal $U_F(k)$-bundle.

As a corollary of the construction, there is also a fibre bundle

$$V_k(F^k) = U_F(k) \to V_{k+1}(F^n) \xrightarrow{q} V_k(F^n)$$

where $q(v_1,\ldots,v_{k+1}) = (v_1,\ldots,v_k)$ forgets the last vector. The fibre is $V_1(F^{n-k})$, which for $F = \mathbf{R}$ is $S^{n-k-1}$, for $F = \mathbf{C}$ is $S^{2n-2k-1}$, and for $F = \mathbf{H}$ is $S^{4n-4k-1}$.
