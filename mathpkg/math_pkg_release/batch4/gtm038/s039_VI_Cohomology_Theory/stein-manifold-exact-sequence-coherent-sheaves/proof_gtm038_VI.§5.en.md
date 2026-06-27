---
role: proof
locale: en
of_concept: stein-manifold-exact-sequence-coherent-sheaves
source_book: gtm038
source_chapter: "VI"
source_section: "§5"
---

The long exact cohomology sequence associated to the short exact sequence

$$0 \to \mathcal{S}^* \to \mathcal{S} \to \mathcal{S}^{**} \to 0$$

reads

$$0 \to \Gamma(X, \mathcal{S}^*) \to \Gamma(X, \mathcal{S}) \to \Gamma(X, \mathcal{S}^{**}) \to H^1(X, \mathcal{S}^*) \to \cdots$$

By Theorem B (Cartan's Theorem B), $H^1(X, \mathcal{S}^*) = 0$ for every coherent analytic sheaf $\mathcal{S}^*$ on a Stein manifold $X$. Therefore the sequence of global sections terminates at $\Gamma(X, \mathcal{S}^{**})$, yielding the exact sequence

$$0 \to \Gamma(X, \mathcal{S}^*) \to \Gamma(X, \mathcal{S}) \to \Gamma(X, \mathcal{S}^{**}) \to 0.$$

The isomorphism $\Gamma(X, \mathcal{S}^{**}) \simeq \Gamma(X, \mathcal{S}) / \Gamma(X, \mathcal{S}^{*})$ follows from the exactness of this sequence.
