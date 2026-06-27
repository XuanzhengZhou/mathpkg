---
role: proof
locale: en
of_concept: density-of-gs-maps-in-strong-cr-topology
source_book: gtm033
source_chapter: "2"
source_section: "2"
---

# Proof of Theorem 2.7 (Density of $G^s$ maps in the strong $C^r$ topology)

This follows from Theorem 2.6 and the openness theorems of Section 2.1.

Recall that $G^k(M,N) \subset C^k(M,N)$, $k \geqslant 1$, denotes any one of the following subsets: diffeomorphisms, embeddings, closed embeddings, immersions, submersions, proper maps. For each of these classes, Section 2.1 established that $G^k(M,N)$ is open in $C^k_S(M,N)$. 

Let $f \in G^r(M,N) \subset C^r_S(M,N)$. By Theorem 2.6, $C^s(M,N)$ is dense in $C^r_S(M,N)$, so there exists a $C^s$ map $g: M \to N$ arbitrarily $C^r$-close to $f$. Since $G^r(M,N)$ is open in $C^r_S(M,N)$, any map sufficiently $C^r$-close to $f$ also belongs to $G^r(M,N)$. In particular, $g$ can be chosen so that $g \in G^r(M,N)$. But $g$ is $C^s$, hence $g \in G^s(M,N)$.

Therefore $G^s(M,N)$ is dense in $G^r(M,N)$ in the strong $C^r$ topology, $1 \leqslant r < s$.

In particular, $M$ and $N$ are $C^s$ diffeomorphic if and only if they are $C^r$ diffeomorphic.

QED
