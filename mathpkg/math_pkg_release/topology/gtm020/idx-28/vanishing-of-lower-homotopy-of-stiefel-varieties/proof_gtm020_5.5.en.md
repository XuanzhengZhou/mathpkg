---
role: proof
locale: en
of_concept: vanishing-of-lower-homotopy-of-stiefel-varieties
source_book: gtm020
source_chapter: "5"
source_section: "5"
---

Applying the homotopy sequence 1(5.3) of a fibre map, we have the following exact sequence:

$$\cdots \rightarrow \pi_i(U_F(m)) \xrightarrow{\alpha} \pi_i(U_F(m + k)) \rightarrow \pi_i(V_k(F^{k+m})) \rightarrow \pi_{i-1}(U_F(m)) \xrightarrow{} \cdots$$

The map $\alpha$ is induced by the inclusion $U_F(m) \hookrightarrow U_F(m+k)$. From the stability results for unitary groups (Section 4), $\alpha$ is an epimorphism when $i < mc$ and an isomorphism when $i < mc - 1$. More precisely, for $i \leq (m+1)c - 2$, we have $i \leq mc + c - 2$, so $\alpha$ is an epimorphism and $\pi_{i-1}(U_F(m)) \to \pi_{i-1}(U_F(m+k))$ is a monomorphism. By exactness, the middle term $\pi_i(V_k(F^{k+m}))$ must vanish for $i \leq (m+1)c - 2$.
