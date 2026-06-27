---
role: proof
locale: en
of_concept: induced-map-composition-property
source_book: gtm027
source_chapter: "7"
source_section: "S"
---

# Proof of Functoriality of the Induced Map

Let $F : X \to Y$ and $G : Y \to Z$ be continuous maps between compact Hausdorff spaces. We prove $(G \circ F)^* = F^* \circ G^*$.

The induced maps are $F^* : C(Y) \to C(X)$, $G^* : C(Z) \to C(Y)$, and $(G \circ F)^* : C(Z) \to C(X)$.

For any $h \in C(Z)$ and $x \in X$:

$$(G \circ F)^*(h)(x) = h((G \circ F)(x)) = h(G(F(x))).$$

On the other hand,

$$(F^* \circ G^*)(h)(x) = F^*(G^*(h))(x) = G^*(h)(F(x)) = h(G(F(x))).$$

Thus $(G \circ F)^* = F^* \circ G^*$, establishing functoriality.
