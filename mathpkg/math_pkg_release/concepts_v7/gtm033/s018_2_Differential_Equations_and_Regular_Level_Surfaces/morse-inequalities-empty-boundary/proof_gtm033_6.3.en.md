---
role: proof
locale: en
of_concept: morse-inequalities-empty-boundary
source_book: gtm033
source_chapter: "6"
source_section: "6.3"
---

# Proof of Morse Inequalities for Manifolds (Empty Lower Boundary)

The theorem follows immediately from Theorem 3.4 (the general Morse inequalities) by setting $f^{-1}(a) = \varnothing$.

When $f^{-1}(a) = \varnothing$, the relative homology group reduces to absolute homology:

$$H_k(M, f^{-1}(a); F) \cong H_k(M, \varnothing; F) \cong H_k(M; F).$$

Therefore the numbers $\beta_k$ in Theorem 3.4 become the absolute Betti numbers $\dim_F H_k(M; F)$. Substituting into the conclusions of Theorem 3.4:

**(a)** For $0 \leqslant m \leqslant n$,

$$\sum_{k=0}^{m} (-1)^{k+m} v_k \geqslant \sum_{k=0}^{m} (-1)^{k+m} \dim_F H_k(M; F).$$

**(b)** The alternating sum of type numbers equals the Euler characteristic:

$$\sum_{k=0}^{n} (-1)^k v_k = \sum_{k=0}^{n} (-1)^k \dim_F H_k(M; F) = \chi(M).$$

In particular, the alternating sum of the type numbers is independent of the choice of the admissible Morse function $f$, being equal to the homological Euler characteristic of $M$.
