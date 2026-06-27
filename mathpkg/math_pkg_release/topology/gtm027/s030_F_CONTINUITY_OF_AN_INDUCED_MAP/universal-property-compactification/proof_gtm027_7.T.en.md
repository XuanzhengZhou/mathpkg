---
role: proof
locale: en
of_concept: universal-property-compactification
source_book: gtm027
source_chapter: "7"
source_section: "T"
---

# Proof of Universal Property of the Almost Periodic Compactification

If $\phi : G \to H$ is a continuous homomorphism of $G$ into a compact topological group $H$, then there exists a continuous homomorphism $\theta : \alpha[G] \to H$ such that $\phi = \theta \circ L$.

**Proof.** Define $\theta$ on the dense subset $\{L_x : x \in G\}$ of $\alpha[G]$ by $\theta(L_x) = \phi(x)$. This is well-defined because if $L_x = L_y$, then for all $f \in A$, $L_x(f) = L_y(f)$. In particular, for any continuous function $h$ on $H$, $h \circ \phi \in A$ (since $\phi$ is a continuous homomorphism into a compact group, left translates of $h \circ \phi$ are totally bounded). Then

$$h(\phi(xy)) = (L_y(h \circ \phi))(x),$$

and the condition $L_x = L_y$ forces $\phi(x) = \phi(y)$ (otherwise continuous functions on $H$ would separate them, contradicting the equality of left translations on $A$).

$\theta$ is a homomorphism: $\theta(L_x \circ L_y) = \theta(L_{xy}) = \phi(xy) = \phi(x)\phi(y) = \theta(L_x)\theta(L_y)$.

The map $\theta$ is uniformly continuous on the dense subset (since $L$ has the property that each $f \in A$ is left uniformly continuous, and the uniformity on $\alpha[G]$ is the weakest making all $\tilde{f}$ continuous). It extends uniquely to a continuous homomorphism $\theta : \alpha[G] \to H$ satisfying $\phi = \theta \circ L$.

More generally, for $\phi : G \to H$ with $H$ arbitrary, $\phi$ induces a natural homomorphism $\theta : \alpha[G] \to \alpha[H]$ such that $\theta \circ L_G = L_H \circ \phi$, by defining $\theta(R)(f) = R(f \circ \phi)$ for $R \in \alpha[G]$ and $f$ left almost periodic on $H$.
