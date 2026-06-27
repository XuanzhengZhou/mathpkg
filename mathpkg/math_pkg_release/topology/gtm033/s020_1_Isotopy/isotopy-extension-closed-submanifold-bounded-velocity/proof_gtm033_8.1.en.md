---
role: proof
locale: en
of_concept: isotopy-extension-closed-submanifold-bounded-velocity
source_book: gtm033
source_chapter: "8"
source_section: "1. Isotopy"
---

# Proof of Isotopy Extension Theorem for Closed Submanifolds with Bounded Velocity

**Theorem 1.6.** Let $V \subset M$ be a closed submanifold and $F: V \times I \to M$ an isotopy of $V$ having bounded velocity. If either $F(V \times I) \subset \partial M$ or $F(V \times I) \subset M - \partial M$, then $F$ extends to a diffeotopy of $M$ which has bounded velocity.

*Proof.* (The proof is left to the reader in the source text.) The argument parallels that of Theorem 1.3, but uses the bounded velocity hypothesis instead of compactness. Consider the vector field $X$ on $\hat{F}(V \times I)$ tangent to the curves $\hat{F}(x \times I)$. Since $F$ has bounded velocity, the horizontal component $H$ of $X$ is bounded. One constructs a tubular neighborhood of the closed submanifold $\hat{F}(V \times I)$ in $M \times I$ and uses a partition of unity to extend $H$ to a time-dependent vector field $G$ on $M \times I$ with bounded velocity that agrees with $H$ on $\hat{F}(V \times I)$. By Theorem 1.1, $G$ generates a diffeotopy of $M$ having bounded velocity, which extends $F$. $\square$
