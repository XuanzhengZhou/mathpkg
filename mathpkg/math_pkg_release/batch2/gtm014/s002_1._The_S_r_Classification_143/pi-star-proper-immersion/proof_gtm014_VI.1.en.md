---
role: proof
locale: en
of_concept: pi-star-proper-immersion
source_book: gtm014
source_chapter: "Chapter VI: Classification of Singularities, Part I: The Thom-Boardman Invariants"
source_section: "§1. The S_r Classification"
---

The proof is straightforward but a little tedious. We will not include it here. (See exercises.) 

The main idea is as follows. For each $p \in G(s, V)$ corresponding to a subspace $K$, the map $\pi^*: \operatorname{Hom}(V/K, W) \to \operatorname{Hom}(V, W)$ is the transpose of the projection $V \to V/K$. This map is clearly linear and injective on each fiber, and its image consists of maps whose kernel contains $K$. Restricted to $L^0(V/K, W)$ — the injective linear maps from $V/K$ to $W$ — the image consists precisely of maps of corank exactly $r$ with kernel exactly $K$. Varying $p$ over $G(s, V)$ gives a fiber bundle description of $L^r(V, W)$; the properness follows from the compactness of the Grassmannian and the fact that the map is a bijection onto its image.

Given Proposition 1.4, the assertion that $S_r(f)$ is generically a submanifold follows by applying the same construction to vector bundles and using the Thom Transversality Theorem.
