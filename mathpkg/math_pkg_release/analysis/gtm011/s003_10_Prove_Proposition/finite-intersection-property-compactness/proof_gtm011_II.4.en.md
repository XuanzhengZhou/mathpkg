---
role: proof
locale: en
of_concept: finite-intersection-property-compactness
source_book: gtm011
source_chapter: "II"
source_section: "4"
---

Suppose $K$ is compact and $\mathcal{F}$ is a collection of closed subsets of $K$ having the f.i.p. Assume that $\bigcap \{F: F \in \mathcal{F}\} = \varnothing$. Then $\{K - F: F \in \mathcal{F}\}$ is an open cover of $K$. By compactness, there exists a finite subcollection $F_1, \ldots, F_n$ such that $K = \bigcup_{i=1}^n (K - F_i) = K - \bigcap_{i=1}^n F_i$, which implies $\bigcap_{i=1}^n F_i = \varnothing$, contradicting the f.i.p.

Conversely, suppose every collection of closed subsets with f.i.p. has non-empty intersection, and let $\mathcal{G}$ be an open cover of $K$. Then $\mathcal{F} = \{K - G: G \in \mathcal{G}\}$ is a collection of closed subsets of $K$ with $\bigcap \mathcal{F} = \varnothing$. Thus $\mathcal{F}$ cannot have the f.i.p., so there exist $G_1, \ldots, G_n \in \mathcal{G}$ with $\bigcap_{i=1}^n (K - G_i) = \varnothing$, i.e., $K \subset \bigcup_{i=1}^n G_i$.
