---
role: proof
locale: en
of_concept: whitney-embedding-theorem
source_book: gtm033
source_chapter: "2"
source_section: "2"
---

# Proof of Theorem 2.14 (Whitney embedding theorem)

This follows from Theorem 2.13 as soon as a proper map $f: M \to \mathbb{R}$ has been found.

If $M$ is compact, take $f$ constant. Then $f$ is a proper $C^\infty$ map $M \to \mathbb{R} \subset \mathbb{R}^{2n+1}$. By Theorem 2.13 with $N = \mathbb{R}^{2n+1}$ (since $\dim \mathbb{R}^{2n+1} = 2n+1 \geqslant 2 \dim M + 1$), embeddings are dense in $C_S^r(M, \mathbb{R}^{2n+1})$. In particular, there exists an embedding $g: M \to \mathbb{R}^{2n+1}$ arbitrarily $C^r$-close to $f$. Since $M$ is compact, any such embedding is a closed embedding (the image of a compact set under a continuous map is compact, hence closed).

If $M$ is not compact, there exists a proper $C^\infty$ map $f: M \to \mathbb{R}$ (for instance, a map that tends to infinity at the ends of $M$, constructed via a partition of unity). Then $f$ is proper and belongs to $\operatorname{Prop}_S^r(M, \mathbb{R}^{2n+1})$ when composed with the inclusion $\mathbb{R} \hookrightarrow \mathbb{R}^{2n+1}$. By Theorem 2.13, embeddings are dense in $\operatorname{Prop}_S^r(M, \mathbb{R}^{2n+1})$, so there exists an embedding $g: M \to \mathbb{R}^{2n+1}$ arbitrarily $C^r$-close to (the inclusion of) $f$. Since $g$ is proper (being close to a proper map in the strong topology) and an embedding, its image is a closed submanifold of $\mathbb{R}^{2n+1}$.

Thus every $C^r$ $n$-dimensional manifold is $C^r$ diffeomorphic to a closed submanifold of $\mathbb{R}^{2n+1}$.

QED
