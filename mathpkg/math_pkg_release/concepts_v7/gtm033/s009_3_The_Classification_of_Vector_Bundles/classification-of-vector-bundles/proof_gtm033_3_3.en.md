---
role: proof
locale: en
of_concept: classification-of-vector-bundles
source_book: gtm033
source_chapter: "3"
source_section: "3. The Classification of Vector Bundles"
---

# Proof of Classification Theorem for Vector Bundles (Theorem 3.4)

**Step 1: From a monomorphism to a classifying map.** Let $F: \xi \hookrightarrow M \times \mathbb{R}^s$ be a $C^r$ monomorphism over $1_M$ (such an $F$ exists by Theorem 3.1 whenever $s \geqslant k + n$, where $n = \dim M$). For each $y \in M$, the image $F(\xi_y) \subset \mathbb{R}^s$ is a $k$-dimensional linear subspace of $\mathbb{R}^s$. This assignment defines a map

$$f_\xi: M \to G_{s,k}$$

into the Grassmann manifold $G_{s,k}$ of $k$-planes in $\mathbb{R}^s$, sending $y$ to the point $F(\xi_y) \in G_{s,k}$. One checks that $f_\xi$ is $C^r$ (in local coordinates on the Grassmannian, the varying $k$-plane depends differentiably on $y$).

By the definition of the universal $k$-plane bundle $\gamma_{s,k}$ over $G_{s,k}$, the pullback $f_\xi^* \gamma_{s,k}$ has fiber over $y$ exactly $F(\xi_y)$, and the vector bundle isomorphism

$$\xi \cong_r f_\xi^* \gamma_{s,k}$$

is given by $F$ itself (regarded as a bundle map covering $f_\xi$). Thus $f_\xi$ is a classifying map for $\xi$.

**Step 2: Homotopic classifying maps imply isomorphic bundles.** Suppose $f_0, f_1: M \to G_{s,k}$ are $C^r$ maps with $f_0 \simeq f_1$ (homotopic in the $C^r$ sense). Let $H: M \times I \to G_{s,k}$ be a $C^r$ homotopy with $H(\cdot, 0) = f_0$ and $H(\cdot, 1) = f_1$. Then $H^* \gamma_{s,k}$ is a $k$-plane bundle over $M \times I$ whose restrictions to $M \times \{0\}$ and $M \times \{1\}$ are

$$(H^*\gamma_{s,k})|_{M \times \{0\}} \cong f_0^*\gamma_{s,k}, \qquad (H^*\gamma_{s,k})|_{M \times \{1\}} \cong f_1^*\gamma_{s,k}.$$

By the covering homotopy theorem for vector bundles, two bundles over $M$ that are restrictions of the same bundle over $M \times I$ to the two ends are isomorphic. Hence

$$f_0^*\gamma_{s,k} \cong_r f_1^*\gamma_{s,k}.$$

This shows that the map $\Theta: [M, G_{s,k}] \to K^k(M)$ given by $[f] \mapsto [f^*\gamma_{s,k}]$ is well-defined.

**Step 3: Isomorphic bundles have homotopic classifying maps.** Let $\xi$ and $\eta$ be $C^r$ isomorphic $k$-plane bundles over $M$. Choose monomorphisms $F: \xi \hookrightarrow M \times \mathbb{R}^s$ and $G: \eta \hookrightarrow M \times \mathbb{R}^s$ (using Theorem 3.1). These give classifying maps $f_\xi, f_\eta: M \to G_{s,k}$ as in Step 1. To show $f_\xi \simeq f_\eta$ when $s > k + n$, consider the bundle $\xi \oplus \varepsilon^1$ (or the same argument applied to both bundles). Alternatively, use Corollary 3.2: the two monomorphisms $F$ and $G \circ \phi$ (where $\phi: \xi \to \eta$ is the given isomorphism) are both monomorphisms of $\xi$ into $\mathbb{R}^s$. Define a bundle $\zeta = \xi \times I$ over $M \times I$; at the two ends we have monomorphisms $F$ (at $t = 0$) and $G \circ \phi$ (at $t = 1$). By Corollary 3.2 (applicable since $s > k + n$), these extend to a monomorphism of $\zeta$ into $(M \times I) \times \mathbb{R}^s$, which produces a homotopy between $f_\xi$ and $f_\eta$. Therefore $\Theta$ is injective.

**Step 4: Surjectivity.** Given any $C^r$ map $f: M \to G_{s,k}$, the pullback bundle $f^*\gamma_{s,k}$ is a $C^r$ $k$-plane bundle over $M$. Its classifying map (obtained from the tautological monomorphism $f^*\gamma_{s,k} \hookrightarrow M \times \mathbb{R}^s$) is precisely $f$, showing that $\Theta([f]) = [f^*\gamma_{s,k}]$ hits every isomorphism class. Thus $\Theta$ is surjective.

**Conclusion.** When $s > k + n$, the map

$$\Theta_M: K^k(M) \to [M, G_{s,k}], \qquad [\xi] \mapsto [f_\xi]$$

is a bijection, with inverse $[f] \mapsto [f^*\gamma_{s,k}]$. Equivalently, two $C^r$ $k$-plane bundles over $M$ are $C^r$ isomorphic if and only if their classifying maps into $G_{s,k}$ are homotopic. $\square$
