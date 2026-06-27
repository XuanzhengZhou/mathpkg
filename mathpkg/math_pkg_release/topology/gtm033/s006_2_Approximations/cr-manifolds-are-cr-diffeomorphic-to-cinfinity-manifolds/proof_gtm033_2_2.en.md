---
role: proof
locale: en
of_concept: cr-manifolds-are-cr-diffeomorphic-to-cinfinity-manifolds
source_book: gtm033
source_chapter: "2"
source_section: "2"
---

# Proof of Theorem 2.10 (Every $C^r$ manifold is $C^r$ diffeomorphic to a $C^\infty$ manifold)

**(a)** Let $1 \leqslant r < \infty$ and let $M$ be a $C^r$ manifold. By Theorem 2.9, there exists a $C^\infty$ differential structure $\beta$ on $M$ compatible with the given $C^r$ structure $\alpha$ (taking $s = \infty$). Compatibility means precisely that the identity map $\operatorname{id}: M_\alpha \to M_\beta$ is a $C^r$ diffeomorphism. Thus $M_\alpha$ is $C^r$ diffeomorphic to the $C^\infty$ manifold $M_\beta$.

**(b)** Let $1 \leqslant r < s \leqslant \infty$ and suppose $M$ and $N$ are $C^s$ manifolds that are $C^r$ diffeomorphic. Let $f: M \to N$ be a $C^r$ diffeomorphism. By Theorem 2.7 applied to diffeomorphisms, $G^s(M,N)$ (the set of $C^s$ diffeomorphisms) is dense in $G^r(M,N)$ (the set of $C^r$ diffeomorphisms) in the strong $C^r$ topology. Since $f \in G^r(M,N)$, there exists a $C^s$ diffeomorphism $g: M \to N$ arbitrarily $C^r$-close to $f$. Thus $M$ and $N$ are $C^s$ diffeomorphic.

QED

In view of this there is no need to consider $C^r$ manifolds for $1 \leqslant r < \infty$; and for most purposes $C^\infty$ maps are sufficient. The $C^\infty$ category has several advantages over the $C^r$ categories with $r$ finite. An obvious one is its closure under derivatives. A more subtle advantage comes from the Morse–Sard theorem in the following chapter.
