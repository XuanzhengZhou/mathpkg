---
role: proof
locale: en
of_concept: universal-property-projective-tensor-product
source_book: gtm003
source_chapter: "III"
source_section: "6"
---

**Proof.** The mapping $u \mapsto u \circ \chi$ is clearly linear and injective, since $\chi(E \times F)$ spans $E \otimes F$ algebraically; thus it suffices to show that $u$ is continuous if and only if $u \circ \chi$ is continuous.

If $u \in \mathcal{L}(E \otimes_\pi F, G)$ is continuous, then $u \circ \chi$ is continuous as the composition of continuous maps, since $\chi$ is continuous by definition of the projective topology.

Conversely, suppose $f = u \circ \chi \in \mathcal{B}(E, F; G)$ is a continuous bilinear map. Let $W$ be a convex, circled $0$-neighborhood in $G$. By continuity of $f$, there exist $0$-neighborhoods $U \subset E$ and $V \subset F$ such that $f(U \times V) \subset W$. Since $f = u \circ \chi$, this implies $u(\chi(U \times V)) = u(U \otimes V) \subset W$. By linearity of $u$, we obtain $u(\Gamma(U \otimes V)) \subset \Gamma(W) = W$, where the last equality holds because $W$ is convex and circled. Since the family $\{\Gamma(U \otimes V)\}$ forms a $0$-neighborhood base for the projective topology $\mathfrak{T}_p$, the linear map $u$ is continuous at $0$ and hence continuous everywhere. $\square$
