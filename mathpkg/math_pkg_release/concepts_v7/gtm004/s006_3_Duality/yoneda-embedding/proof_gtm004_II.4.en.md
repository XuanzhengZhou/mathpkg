---
role: proof
locale: en
of_concept: yoneda-embedding
source_book: gtm004
source_chapter: "II"
source_section: "4"
---

# Proof of the Yoneda Embedding

By choosing $F = \mathfrak{C}(A', -)$ in the Yoneda Lemma (Proposition 4.1), the set of natural transformations from $\mathfrak{C}(A, -)$ to $\mathfrak{C}(A', -)$ is in bijection with $\mathfrak{C}(A', A)$.

Explicitly, each morphism $f : A' \to A$ in $\mathfrak{C}$ gives rise to a natural transformation $f^* : \mathfrak{C}(A, -) \to \mathfrak{C}(A', -)$ defined by precomposition with $f$, i.e., $f^*_B(\varphi) = \varphi \circ f$ for $\varphi : A \to B$. The Yoneda Lemma shows that every natural transformation between these Hom-functors arises uniquely in this way.

If $\mathfrak{C}$ is a small category, we may formulate this in the functor category $\mathfrak{S}^{\mathfrak{C}}$. The assignment $A \mapsto \mathfrak{C}(A, -)$ defines a functor $\mathfrak{C}^{\mathrm{opp}} \to \mathfrak{S}^{\mathfrak{C}}$, called the **Yoneda embedding**. Corollary 4.2 asserts that this embedding is **full and faithful** (a full embedding): the map

$$\mathfrak{C}(A', A) \to [\mathfrak{C}(A, -), \mathfrak{C}(A', -)]$$

given by $f \mapsto f^*$ is a bijection.
