---
role: proof
locale: en
of_concept: local-triviality-of-stiefel-grassmann-bundle
source_book: gtm020
source_chapter: "3"
source_section: "3.6"
---

**Proof.** For each $W \in G_k(F^n)$, let $O(W)$ denote the open set of all subspaces $W'$ that are graph-related to $W$, i.e., those $W'$ for which the orthogonal projection $\pi_{W'}|_W: W \to W'$ is an isomorphism. For $W = \langle v_1, \ldots, v_k \rangle$, we define a map

$$f_{(v_1, \ldots, v_k), W'}: W \to F^n$$

that is linear, inner-product preserving, continuous in the frame $(v_1, \ldots, v_k) \in V_k(F^n)$ and $W' \in O(W)$, and satisfies $f_{(v_1, \ldots, v_k), W'}(W) = W'$. This is done by requiring

$$f_{(v_1, \ldots, v_k), W'}(v_i) = v_i'$$

where $(v_1', \ldots, v_k') = GS(\pi_{W'}(v_1), \ldots, \pi_{W'}(v_k))$ is obtained by applying the Gram-Schmidt map to the projection of the frame vectors. The well-definedness of this construction follows from Proposition 3.1.

A local trivialization over $O(W)$ is then given by the map

$$g: O(W) \times U_F(k) \to p^{-1}(O(W))$$

defined by $g(W', a) = (v_1, \ldots, v_k)a$ where $(v_1, \ldots, v_k)$ is the frame constructed above. This shows that $p$ is locally trivial with fibre $U_F(k)$. Moreover, for the case $k+1$, one obtains the local product structure

$$O_H^* \times V_1(F^{n-k}) \cong q^{-1}(O_H^*) \subset V_{k+1}(F^n)$$

where $g(v_1, \ldots, v_k, x) = (v_1, \ldots, v_k, v_{k+1})$ with $v_{k+1} = f_{(v_1, \ldots, v_k), W^*}(x)$. Observe that the fibre $V_1(F^{n-k})$ is $S^{n-k-1}$ for $F = \mathbf{R}$, $S^{2n-2k-1}$ for $F = \mathbf{C}$, and $S^{4n-4k-1}$ for $F = \mathbf{H}$.
