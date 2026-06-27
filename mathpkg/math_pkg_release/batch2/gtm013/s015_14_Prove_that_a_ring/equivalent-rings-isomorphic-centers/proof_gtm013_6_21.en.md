---
role: proof
locale: en
of_concept: equivalent-rings-isomorphic-centers
source_book: gtm013
source_chapter: "6"
source_section: "21"
---

Adopt the notation of (21.1). For each ideal $I$ of $R$, define

$$\Phi(I) = \operatorname{Ann}_S(F(R/I)).$$

That is, $\Phi(I)$ is the annihilator in $S$ of the $S$-module $F(R/I)$. Each such $\Phi(I)$ is an ideal of $S$. Similarly, if $K$ is an ideal of $S$, define

$$\Gamma(K) = l_R(G(S/K)) = \operatorname{Ann}_R(G(S/K)),$$

which is an ideal of $R$.

We claim that $\Phi$ and $\Gamma$ define inverse mappings of the ideal lattices. By viewing $F(R/I)$ first as a faithful $S/\Phi(I)$-module, it is clear that as $S$-modules, $F(R/I)$ cogenerates $S/\Phi(I)$ and $S/\Phi(I)$ generates $F(R/I)$. Thus, by (21.6), $R/I$ cogenerates $G(S/\Phi(I))$ and $G(S/\Phi(I))$ generates $R/I$ as $R$-modules. In particular, these two $R$-modules must have the same annihilator (Exercise 8.2). That is,

$$\Gamma\Phi(I) = I.$$

Similarly, for each ideal $K$ of $S$, $\Phi\Gamma(K) = K$.

If $I \subseteq I'$ are ideals of $R$, then there is a natural $R$-epimorphism $R/I \to R/I' \to 0$. By (21.2), there is an $S$-epimorphism $F(R/I) \to F(R/I') \to 0$, whence $\Phi(I) \subseteq \Phi(I')$. Thus $\Phi$ is order-preserving, and similarly so is $\Gamma$. Therefore $\Phi$ is a lattice isomorphism from the ideal lattice of $R$ to that of $S$.

The center isomorphism follows from the fact that the center of $R$ is isomorphic to the endomorphism ring of the identity functor on ${}_R \mathbf{M}$, and equivalence preserves this endomorphism ring.
