---
role: proof
locale: en
of_concept: corollary-2-3-diffeomorphism-from-split-boundary
source_book: gtm033
source_chapter: "6"
source_section: "2"
---

# Proof of Diffeomorphism from Split Boundary

This is a direct application of the Regular Interval Theorem (Theorem 2.2). 

Let $M$ be a compact manifold with $\partial M = A \cup B$, where $A$ and $B$ are disjoint closed sets. Suppose there exists a $C^2$ map $f: M \to \mathbb{R}$ without critical points such that $f(A) = 0$, $f(B) = 1$.

Since $\partial M = A \cup B$ and $f$ maps $A$ to $0$ and $B$ to $1$, and $f$ has no critical points, the image $f(M)$ is contained in $[0, 1]$. In fact, by compactness and the absence of critical points, $f(M) = [0, 1]$. Moreover, $f^{-1}(0) = A$ and $f^{-1}(1) = B$, because any point mapping to $0$ would have to be a critical point or lie in $A$ (and similarly for $1$), and by assumption there are no critical points.

Now apply Theorem 2.2 with $a = 0$, $b = 1$. The theorem gives a $C^r$ diffeomorphism

$$F: f^{-1}(0) \times [0, 1] \rightarrow M,$$

i.e., $F: A \times I \rightarrow M$, where $I = [0, 1]$.

For the symmetric statement with $B$, simply apply the same argument to the function $g = 1 - f$, which satisfies $g(B) = 0$ and $g(A) = 1$, and has the same critical points as $f$ (namely, none). Theorem 2.2 then yields a diffeomorphism $B \times I \cong M$.

Thus $M$ is diffeomorphic to both $A \times I$ and $B \times I$.
