---
role: proof
locale: en
of_concept: hom-functors-additive
source_book: gtm013
source_chapter: "1"
source_section: "§16. The Hom Functors and Exactness—Projectivity and Injectivity"
---

We show that $Hom_R(-, U)$ reverses composition and preserves addition. Suppose that $g: M \to M'$ and $f: M' \to M''$ are morphisms in ${}_R\mathcal{M}$. If $\gamma \in Hom_R(M'', U)$, then

$$(f \circ g)^*(\gamma) = \gamma \circ f \circ g = g^*(f^*(\gamma)) = (g^* \circ f^*)(\gamma).$$

Next suppose that $f: M \to N$ and $g: M \to N$ are morphisms in ${}_R\mathcal{M}$. If $\gamma \in Hom(N, U)$, then

$$(f + g)^*(\gamma) = \gamma \circ (f + g) = (\gamma \circ f) + (\gamma \circ g) = f^*(\gamma) + g^*(\gamma).$$

Thus $Hom_R(-, U)$ is an additive contravariant functor. The proof for $Hom_R(U, -)$ is similarly routine.
