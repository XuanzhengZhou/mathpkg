---
role: proof
locale: en
of_concept: upper-bound-of-locally-convex-topologies
source_book: gtm003
source_chapter: "II"
source_section: "5"
---

Let $\{\mathfrak{T}_\alpha : \alpha \in \mathbf{A}\}$ be a family of locally convex topologies on $E$. Their least upper bound $\mathfrak{T}$ in the lattice of all topologies on $E$ is the coarsest topology on $E$ that is finer than each $\mathfrak{T}_\alpha$. This is equivalent to requiring that the identity map $e: E \to (E, \mathfrak{T}_\alpha)$ be continuous for each $\alpha \in \mathbf{A}$. By the definition of the projective topology (Section 5), $\mathfrak{T}$ is precisely the projective topology on $E$ with respect to the family $\{(E, \mathfrak{T}_\alpha, e) : \alpha \in \mathbf{A}\}$, where $e$ is the identity map of $E$. A 0-neighborhood base for $\mathfrak{T}$ is given by finite intersections $\bigcap_{\alpha \in H} U_\alpha$ where $H$ is finite and $U_\alpha$ is a $\mathfrak{T}_\alpha$-neighborhood of 0. Since each $\mathfrak{T}_\alpha$ is locally convex, each $U_\alpha$ can be chosen convex and circled, and the intersection of finitely many such sets remains convex and circled. Moreover, these intersections form a filter base satisfying conditions (a) and (b) of (I, 1.2), hence $\mathfrak{T}$ is a locally convex topology. Thus the upper bound of locally convex topologies is a locally convex projective topology.
