---
role: proof
locale: en
of_concept: bott-periodicity-k-theory-spheres
source_book: gtm020
source_chapter: "9"
source_section: "5.1"
---

For the principal $U_F(n)$-bundle $V_n(F^{2n}) \rightarrow G_n(F^{2n})$, we have the homotopy exact sequence

$$0 = \pi_i(V_n(F^{2n})) \rightarrow \pi_i(G_n(F^{2n})) \xrightarrow{\partial} \pi_{i-1}(U_F(n)) \rightarrow \pi_{i-1}(V_n(F^{2n})) = 0$$

This holds by 7(5.1) for $i < (n+1)c-2$, since $V_n(F^{2n})$ is highly connected. The exactness yields the isomorphism $\partial: \pi_i(G_n(F^{2n})) \rightarrow \pi_{i-1}(U_F(n))$.

By 7(4.1), for $i-1 < c(n+1)-3$, the inclusion $U_F(n) \rightarrow U_F$ induces an isomorphism $\pi_{i-1}(U_F(n)) \rightarrow \pi_{i-1}(U_F)$. 

Combining these with the corepresentation isomorphism $\tilde{K}_F(S^i) \xrightarrow{\theta^{-1}} \pi_i(B_{(F)})$ and the bijection $\pi_i(B_{(F)}) \rightarrow \pi_i(G_n(F^{2n}))$ from Proposition 4.4, we obtain the sequence of isomorphisms:

$$\tilde{K}_F(S^i) \xrightarrow{\theta^{-1}} \pi_i(B_{(F)}) \xrightarrow{\cong} \pi_i(G_n(F^{2n})) \xrightarrow{\partial} \pi_{i-1}(U_F(n)) \rightarrow \pi_{i-1}(U_F)$$

The composition is an isomorphism $\tilde{K}_F(S^i) \rightarrow \pi_{i-1}(U_F)$.
