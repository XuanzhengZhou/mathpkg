---
role: proof
locale: en
of_concept: product-of-complete-spaces
source_book: gtm027
source_chapter: "6"
source_section: "Completeness"
---

# Proof that the Product of Complete Spaces is Complete (Theorem 6.25)

**Theorem 6.25.** The product of uniform spaces is complete if and only if each coordinate space is complete.

A net in the product is a Cauchy net if and only if its projection into each coordinate space is a Cauchy net.

**Proof.** ($\Rightarrow$) If the product $\prod_{a \in A} X_a$ is complete, then each coordinate space $X_a$ is the image of the product under the projection $P_a$, which is uniformly continuous. The image of a Cauchy net under a uniformly continuous map is Cauchy, and every Cauchy net in $X_a$ is the projection of a Cauchy net in the product (by taking constant sequences in the other coordinates). Since the product is complete, the image net converges, making the original net in $X_a$ converge. Thus each $X_a$ is complete.

($\Leftarrow$) Suppose each $(X_a, \mathcal{U}_a)$ is complete. Let $\{x^n : n \in D\}$ be a Cauchy net in the product. For each $a \in A$, the projection $\{x^n_a : n \in D\}$ is a Cauchy net in $X_a$ (since projections are uniformly continuous by Theorem 6.10). Since $X_a$ is complete, $\{x^n_a\}$ converges to some point $y_a \in X_a$. Let $y = (y_a)_{a \in A}$. Then the net $\{x^n\}$ converges to $y$ in the product topology (equivalently, the product uniformity topology), because each coordinate converges. Thus the product is complete.

For the characterization: by Theorem 6.10, a map into a product is uniformly continuous if and only if each projection is uniformly continuous. Applying this to the map $(m,n) \mapsto (x^m, x^n)$ from $D \times D$ into the product $X \times X$ shows that the net $\{x^n\}$ is Cauchy in the product if and only if each projection $\{x^n_a\}$ is Cauchy in $X_a$.
