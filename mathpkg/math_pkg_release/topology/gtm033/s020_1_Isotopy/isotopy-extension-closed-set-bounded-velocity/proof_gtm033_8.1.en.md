---
role: proof
locale: en
of_concept: isotopy-extension-closed-set-bounded-velocity
source_book: gtm033
source_chapter: "8"
source_section: "1. Isotopy"
---

# Proof of Isotopy Extension Theorem for Closed Sets with Bounded Velocity

**Theorem 1.7.** Let $A \subset M$ be a closed set and $U \subset M$ an open neighborhood of $A$. Let $F: U \times I \to M$ be an isotopy of $U$ having bounded velocity, such that $\hat{F}(U \times I)$ is open in $M \times I$. Then there is a diffeotopy $G$ of $M$ having bounded velocity, which agrees with $F$ on a neighborhood of $A \times I$; and $\operatorname{Supp} G \subset \overline{F(U \times I)}$.

*Proof.* (The proof is left to the reader in the source text.) The argument parallels that of Theorem 1.4, with the compactness hypothesis replaced by bounded velocity. The tangent vectors to the curves $\hat{F}(x \times I)$ for $x \in U$ define a vector field $X$ on $\hat{F}(U \times I)$ of the form $X(y,t) = (H(y,t), 1)$. Since $F$ has bounded velocity, $H$ is bounded.

By means of a partition of unity subordinate to a suitable cover, one extends $H$ to a time-dependent vector field $G$ on $M \times I$ that has bounded velocity, agrees with $H$ on a neighborhood of $A \times I$, and satisfies $\operatorname{Supp} G \subset \overline{F(U \times I)}$. The openness of $\hat{F}(U \times I)$ ensures the smooth extension is possible. By Theorem 1.1, $G$ generates a diffeotopy of $M$ having bounded velocity, which is the desired extension. $\square$
