---
locale: en
of_concept: if-xi-is-a-vector-bundle-over-b-there-exists-a-splitting-map
role: proof
source_book: gtm020
source_chapter: 17. Chern Classes and Stiefel-Whitney Classes
source_section: '1'
---

We prove this by induction on the dimension of $\xi$. For a line bundle, the identity on the base space is a splitting map. In general, let $q: E(P\xi) \rightarrow B$ be the associated projective bundle. Then $q^*: H^*(B, K_c) \rightarrow H^*(E(P\xi), K_c)$ is a monomorphism, and $q^*(\xi) = \lambda_\xi \oplus \sigma_\xi$. By inductive hypothesis there exists a splitting map $g: B_1 \rightarrow E(P\xi)$ for $\sigma_\xi$. Then $f = qg$ from $B_1$ to $B$ is a splitting map for $\xi$.
