---
locale: en
of_concept: for-each-numerable-principal-g-bundle-xi-over-a-space-b-ther
role: proof
source_book: gtm020
source_chapter: 4. General Fibre Bundles
source_section: '2'
---

It suffices to define a $G$-morphism $(g, f): \xi \rightarrow \omega_G$, for then, by (4.2), $\xi$ and $f^*(\omega_G)$ are isomorphic. By (12.1) we can assume that there is a countable partition of unity $\{u_n\}_{0 \leq n}$ on $B$ such that $\xi|u_n^{-1}(0, 1]$ is trivial for $n \geq 0$. Let $U_n$ denote $u_n^{-1}(0, 1)$, and let $h_n: U_n \times G \rightarrow E(\xi|U_n) \subset E(\xi)$ be an isomorphism defining the locally trivial character of $\xi$.

We define $g: E(\xi) \rightarrow E_G$ by the relation

$$g(z) = (u_0 p(z)(q_0 h_0^{-1}(z)), \ldots, u_n p(z)(q_n h_n^{-1}(z)), \ldots)$$

where $q_n: U_n \times G \rightarrow G$ is the projection on the second factor. Since for $z$, where $h_n^{-1}(z)$ is undefined, we have $u_n(p(z)) = 0$, the map $g$ is well defined and the relation $g(zs) = g(z)s$ holds for each $s \in G$ since $h_n(zs) = h_n(z)s$. The map $g$ induces $f: B \rightarrow B_G$ and $(g, f): \xi \rightarrow \omega_G$ is a bundle morphism. This proves the theorem.

We consider various maps $B_G \rightarrow B_G$ determined by maps $E_G \right
