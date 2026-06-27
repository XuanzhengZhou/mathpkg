---
role: proof
locale: en
of_concept: germ-maps-lattice-anti-isomorphism
source_book: gtm044
source_chapter: "III"
source_section: "1"
---

# Proof of Lattice Anti-Isomorphism Between $G^*$ and $J^*$ on Germs

**Theorem 3.16.** Let $a^*, b^*$ be any two ideals in $\mathcal{J}(R_{\mathfrak{p}})$, and $X_W, Y_W$ any two elements of $\mathcal{G}(R_{\mathfrak{p}})$. Then

(3.16.1) $G^*(a^* \cap b^*) = G^*(a^*) \cup G^*(b^*)$  
(3.16.2) $G^*(a^* + b^*) = G^*(a^*) \cap G^*(b^*)$  
(3.16.3) $J^*(X_W \cup Y_W) = J^*(X_W) \cap J^*(Y_W)$  
(3.16.4) $J^*(X_W \cap Y_W) = J^*(X_W) + J^*(Y_W)$

*Proof of (3.16.1).* Recall that $G^* = (\cdot)_W \circ V \circ (\cdot)^c$. Since contraction $(\cdot)^c$ preserves intersections (it is simply intersection with $R$ because $R \to R_{\mathfrak{p}}$ is an embedding, and intersection of ideals preserves $\cap$), the map $V$ (which sends ideals to varieties) is lattice-reversing (i.e., $V(a \cap b) = V(a) \cup V(b)$), and the germ map $(\cdot)_W$ preserves unions, we obtain:

$$G^*(a^* \cap b^*) = (V((a^* \cap b^*)^c))_W = (V(a^{*c} \cap b^{*c}))_W = (V(a^{*c}) \cup V(b^{*c}))_W = V(a^{*c})_W \cup V(b^{*c})_W = G^*(a^*) \cup G^*(b^*).$$

Note that $V(a^{*c})_W$ is defined as $(V(a^{*c})_{(W)}, W)$ where $V(a^{*c})_{(W)}$ is the union of irreducible components of $V(a^{*c})$ containing $W$.

*Proof of (3.16.3).* Recall that $J^* = (\cdot)^e \circ J \circ i$. The map $i$ simply strips the reference to the center $W$: $i(X_W) = X_{(W)}$, and it preserves unions. The map $J$ sends varieties to their ideals and is lattice-reversing. The extension map $(\cdot)^e$ preserves intersections (by Proposition 3.12). Thus:

$$J^*(X_W \cup Y_W) = (J(i(X_W \cup Y_W)))^e = (J(i(X_W) \cup i(Y_W)))^e = (J(i(X_W)) \cap J(i(Y_W)))^e = (J(i(X_W)))^e \cap (J(i(Y_W)))^e = J^*(X_W) \cap J^*(Y_W).$$

*Proof of (3.16.4).* We want to show $J^*(X_W \cap Y_W) = J^*(X_W) + J^*(Y_W)$. First, note that $i(X_W) \cap i(Y_W)$ and $i(X_W \cap Y_W)$ may differ. By the definition of the germ intersection,

$$X_W \cap Y_W = (X \cap Y)_W = ((X \cap Y)_{(W)}, W).$$

Now,

$$i(X_W) \cap i(Y_W) = X_{(W)} \cap Y_{(W)}.$$

On the other hand, $i(X_W \cap Y_W) = i((X \cap Y)_W) = (X \cap Y)_{(W)}$. These differ by varieties not containing $W$: from the definition of the germ, we have

$$i(X_W) \cap i(Y_W) = i(X_W \cap Y_W) \cup Z,$$

where $Z \subset V$ is a variety which does not contain $W$. Applying $J$ (which reverses inclusions),

$$J(i(X_W) \cap i(Y_W)) = J(i(X_W \cap Y_W)) \cap \mathfrak{c},$$

where $\mathfrak{c} = J(Z) \in \mathcal{I}(R)$ is an ideal not contained in $\mathfrak{p}$ (since $Z$ does not contain $W = V(\mathfrak{p})$). Now apply the extension map $(\cdot)^e$:

$$J^*(X_W \cap Y_W) = (J(i(X_W \cap Y_W)))^e.$$

Meanwhile,

$$J^*(X_W) + J^*(Y_W) = (J(i(X_W)))^e + (J(i(Y_W)))^e = (J(i(X_W)) + J(i(Y_W)))^e = (J(i(X_W) \cap i(Y_W)))^e,$$

using that $J$ reverses intersections to sums. Continuing,

$$(J(i(X_W) \cap i(Y_W)))^e = (J(i(X_W \cap Y_W)) \cap \mathfrak{c})^e.$$

By Proposition 3.12, extension preserves intersections of closed ideals, and since $\mathfrak{c} \not\subset \mathfrak{p}$, we have $\mathfrak{c}^e = R_{\mathfrak{p}}$ by (9). Therefore

$$(J(i(X_W \cap Y_W)) \cap \mathfrak{c})^e = (J(i(X_W \cap Y_W)))^e \cap \mathfrak{c}^e = (J(i(X_W \cap Y_W)))^e \cap R_{\mathfrak{p}} = (J(i(X_W \cap Y_W)))^e = J^*(X_W \cap Y_W).$$

Thus $J^*(X_W) + J^*(Y_W) = J^*(X_W \cap Y_W)$, establishing (3.16.4).

*Proof of (3.16.2).* This follows from (3.16.3) and (3.16.4) together with the fact that $G^*$ and $J^*$ are mutually inverse lattice-reversing isomorphisms. Alternatively, one may prove it directly using the same techniques as above, noting that $(\cdot)^c$ preserves sums as well as intersections. $\square$
