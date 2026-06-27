---
role: proof
locale: en
of_concept: n-sphere-hull-property
source_book: gtm035
source_chapter: "18"
source_section: "18.2"
---
# Proof of Hull of an n-Sphere in C^n

Let $S$ be a set in $\mathbb{C}^n$ homeomorphic to the $n$-sphere. Then $h(S) \neq S$.

**Proof.** Recall that $h(S) = \mathcal{M}(P(S))$, where $\mathcal{M}(P(S))$ denotes the maximal ideal space of the algebra $P(S)$. The algebra $P(S)$ has $n$ generators (namely the coordinate functions $z_1, \dots, z_n$ restricted to $S$). By Theorem 15.8, the $n$-th cohomology group of $\mathcal{M}(P(S))$ with complex coefficients vanishes:

$$H^n(\mathcal{M}(P(S)), \mathbb{C}) = 0.$$

However, $H^n(S, \mathbb{C}) \neq 0$ since $S$ is homeomorphic to the $n$-sphere. If $h(S) = S$, then $\mathcal{M}(P(S)) = S$, which would imply $H^n(\mathcal{M}(P(S)), \mathbb{C}) = H^n(S, \mathbb{C}) \neq 0$, contradicting the vanishing result from Theorem 15.8. Hence $S \neq h(S)$. ∎

**Remark.** This lemma is used in the proof of Lemma 18.1 ($P(X) \neq C(X)$) which establishes that on a $k$-dimensional submanifold $\Sigma$ of $\mathbb{C}^n$ with $n < k < 2n$, polynomials cannot approximate all continuous functions.
