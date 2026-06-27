---
locale: en
of_concept: for-each-finite-connected-cw-complex-x-there-exists-a-k-such
role: proof
source_book: gtm020
source_chapter: 9. Stability Properties of Vector Bundles
source_section: '3'
---

By (2.7), for $k$ such that $\dim X \leq c(k + 1) - 2$, the following bijections are induced by inclusions:

$$[X, G_k(F^{2k})] \rightarrow \cdots \rightarrow [X, G_q(F^{2q})] \rightarrow \cdots$$

Since $X$ is compact, every map $f: X \rightarrow B_{(F)}$ has the image $f(X) \subset G_n(F^{2n})$ for some $n$ for $k \leq n$, and the function $[X, G_q(F^{2q})] \rightarrow [X, B_{(F)}]$ is surjective. Since the image of a homotopy of maps $X \rightarrow B_{(F)}$ lies in some $G_n(F^{2n}) \subset B_{(F)}$ for some $n$ for $k \leq n$,

In this way we see that there exists a unique map $\psi: B_{(F)} \times B_{(F)} \rightarrow B_{(F)}$ such that the following diagram is commutative where the vertical maps are inclusions.

$$G_n(F^{2n}) \times G_n(F^{2n}) \xrightarrow{\psi_n} G_{2n}(F^{4n})$$
$$G_{n+k}(F^{2(n+k)}) \times G_{n+k}(F^{2(n+k)}) \xrightarrow{\psi_{n+k}} G_{2(n+k)}F^{4(n+k)}$$

For $[f], [g] \in [X, B_{(F)}]$, there exists an integer $n$ such that we can view $f$, $g: X \rightarrow G_n(F^{2n})$. Then $\theta([f]) = f^*(\gamma_n^{2n}) - n$ and $\theta([g]) = g^*(\gamma_n^{2n}) - n$. Moreover, $(\psi_n(f \times g)\Delta)^*(\gamma_n^{4n}) = \Delta^*(f^*(\gamma_n^{2n}) \times g^*(\gamma_n^{2n})) = f^*(\gamma_n^{2n}) \oplus g^*(\gamma_n^{2n})$. Therefore, in $\tilde{K}_F(X)$ we have $\theta([\psi_n(f \times g)\Delta]) = f^*(\gamma_n^{2n}) \oplus g^*(\gamma_n^{2n}) - 2n = (f^*(\gamma_n^{2n}) - n) + (g^*(\gamma_n^{2n}) - n) = \theta([f]) + \theta([g])$. This proves the theorem.

4.6 Remark. In view of the natural splitting $K_F(X) = \tilde{K}_F(X) \oplus Z$, there is an isomorphism $\theta: [-, B_{(F)} \times Z] \rightarrow K_F(-)$ for connected finite CW-complexes.

4.7 Remark. For a connected space $X$ we can replace $[X, B_{(F)}]$ by $[

For the principal $U_F(n)$-bundle $V_n(F^{2n}) \rightarrow G_n(F^{2n})$, we have the homotopy exact sequence

$$0 = \pi_i(V_n(F^{2n})) \rightarrow \pi_i(G_n(F^{2n})) \xrightarrow{\hat{c}} \pi_{i-1}(U_F(n)) \rightarrow \pi_{i-1}(V_n(F^{2n})) = 0$$

This holds by 7(5.1) for $i < (n+1)c-2$. This yields the isomorphism $\partial: \pi_i(G_n(F^{2n})) \rightarrow \pi_{i-1}(U_F(n))$. By 7(4.1) for $i-1 < c(n+1)-3$, the inclusion $U_F(n) \rightarrow U_F$ induces an isomorphism $\pi_{i-1}(U_F(n)) \rightarrow \pi_{i-1}(U_F)$. We have the following sequence of isomorphisms:

$$\tilde{K}_F(S^i) \xrightarrow{\theta-1} \pi_i(B_{(F)}) \xrightarrow{\alpha} \pi_i(G_n(F^{2n})) \xrightarrow{\hat{c}} \pi_{i-1}(U_F(n)) \rightarrow \pi_{i-1}(U_F)$$

The composition is an isomorphism $\tilde{K}_F(S^i) \rightarrow \pi_{i-1}(U_F)$. This proves the theorem.
