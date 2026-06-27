---
role: proof
locale: en
of_concept: induced-maps-in-group-cohomology
source_book: gtm004
source_chapter: "VI"
source_section: "2"
---

# Proof: Natural Homomorphisms Induced by Group Homomorphisms

Let $f: G \to G'$ be a group homomorphism. This induces a ring homomorphism $\mathbb{Z}f: \mathbb{Z}G \to \mathbb{Z}G'$ (which we also denote by $f$). By the general machinery of change of rings (Section IV.12), we obtain an adjoint triple.

**Step 1: The restriction functor.** The ring homomorphism $f$ defines, via (IV.12.3), a restriction-of-scalars functor

$$Uf: \mathbb{M}_{\mathbb{Z}G'} \longrightarrow \mathbb{M}_{\mathbb{Z}G},$$

where a $G'$-module $A'$ is regarded as a $G$-module by $x \circ a' = f(x) \circ a'$ for $x \in G$, $a' \in A'$.

**Step 2: The left adjoint.** By (IV.12.4), $Uf$ admits a left adjoint

$$F: \mathbb{M}_{\mathbb{Z}G} \longrightarrow \mathbb{M}_{\mathbb{Z}G'}, \qquad FA = \mathbb{Z}G' \otimes_G A,$$

where the tensor product is taken over $\mathbb{Z}G$ via the homomorphism $f$.

**Step 3: Natural homomorphisms in cohomology.** Consider the $G$-module $\mathbb{Z}$ (with trivial action). Then $F\mathbb{Z} = \mathbb{Z}G' \otimes_G \mathbb{Z} \cong \mathbb{Z}$ as a $G'$-module (with trivial action). The adjunction $(F, Uf)$ together with Theorem IV.12.5 yields, for each $n \geq 0$, a natural homomorphism

$$\theta: H^n(G', A') = \operatorname{Ext}_{\mathbb{Z}G'}^n(\mathbb{Z}, A') \longrightarrow \operatorname{Ext}_{\mathbb{Z}G}^n(\mathbb{Z}, Uf A') = H^n(G, Uf A').$$

**Step 4: Natural homomorphisms in homology.** For right modules, we proceed analogously. The ring homomorphism $\mathbb{Z}f^{\text{op}}: (\mathbb{Z}G)^{\text{op}} \to (\mathbb{Z}G')^{\text{op}}$ induces a restriction functor on right modules. Its left adjoint is again given by $B \mapsto B \otimes_G \mathbb{Z}G'$. By the Tor-analogue of Theorem IV.12.5, we obtain for each $n \geq 0$ a natural homomorphism

$$\theta: H_n(G, Uf B') = \operatorname{Tor}_n^{\mathbb{Z}G}(Uf B', \mathbb{Z}) \longrightarrow \operatorname{Tor}_n^{\mathbb{Z}G'}(B', \mathbb{Z}) = H_n(G', B').$$

**Step 5: Functoriality.** In practice, one often omits the functor $Uf$ from the notation, understanding that $G'$-modules are regarded as $G$-modules via $f$. With this convention, the pair $(G, A) \mapsto H^n(G, A)$ becomes a functor on the category $\mathfrak{G}^*$ whose objects are pairs (group, module over that group) and whose morphisms are compatible pairs of group and module homomorphisms.
