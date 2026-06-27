---
role: proof
locale: en
of_concept: equivalence-submodule-lattice-isomorphism
source_book: gtm013
source_chapter: "6"
source_section: "21"
---

Since $F$ is a functor, it is easy to see that $\Lambda_M$ is order-preserving. Adopting the notation of (21.1), for each $N \leq F(M)$ define

$$\Gamma_M(N) = \operatorname{Im} \phi(i_{N \leq F(M)})$$

where $\phi$ is the isomorphism from (21.3). Then $\Gamma_M$ is a function from the submodules of $F(M)$ to those of $M$, and it is also order-preserving by (21.3.1).

Now for $K \leq M$, let $N = \Lambda_M(K)$. Since $F(i_{K \leq M})$ is monic (21.2), there is an isomorphism $h: F(K) \to N$ making the inclusion diagram commute. By (21.3),

$$\phi(i_{N \leq F(M)}) \circ G(h) = \phi(i_{N \leq F(M)} \circ h) = \phi(F(i_{K \leq M}))$$

$$= i_{K \leq M} \circ \phi(1_{F(K)}).$$

Since $G(h)$ and $\phi(1_{F(K)})$ are isomorphisms (by (21.2) and (21.3)),

$$\Gamma_M \Lambda_M(K) = \operatorname{Im} \phi(i_{N \leq F(M)}) = \operatorname{Im} i_{K \leq M} = K.$$

Next, let $N \leq F(M)$ and let $K = \Gamma_M(N)$. There is an isomorphism $\gamma$ making the relevant diagram commute. Applying $\phi^{-1}$ and using (21.3),

$$i_{N \leq F(M)} = \phi^{-1}(i_{K \leq M} \circ \gamma) = F(i_{K \leq M}) \circ \phi^{-1}(\gamma).$$

Since $\phi^{-1}(\gamma)$ is an isomorphism (21.3),

$$\Lambda_M \Gamma_M(N) = \operatorname{Im} F(i_{K \leq M}) = \operatorname{Im} i_{N \leq F(M)} = N.$$

Thus $\Lambda_M$ and $\Gamma_M$ are mutual inverses, establishing the lattice isomorphism.
