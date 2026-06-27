---
role: proof
locale: en
of_concept: mono-epi-iso-abelian
source_book: gtm004
source_chapter: "II"
source_section: "9"
---

# Proof of Monomorphism + Epimorphism = Isomorphism in an Abelian Category

Let $\alpha: A \to B$ be a morphism in the abelian category $\mathfrak{A}$ that is both a monomorphism and an epimorphism.

Since $\alpha$ is a monomorphism, its kernel is the zero morphism $0 \to A$. Form the image factorization (Proposition 9.6):

$$0 \to A \xrightarrow{\eta} I \xrightarrow{\nu} B \xrightarrow{\varepsilon} C,$$

where $\alpha = \nu \circ \eta$, $\eta = \operatorname{coker}(\ker \alpha) = \operatorname{coker}(0) = 1_A$ (the cokernel of $0: 0 \to A$ is the identity $1_A: A \to A$), so $\eta = 1_A$ and $I \cong A$. Thus $\nu = \alpha$.

On the other hand, since $\alpha$ is an epimorphism, its cokernel is the zero morphism $B \to 0$. Then $\varepsilon = 0: B \to 0$, and $\alpha = \ker(\varepsilon) = \ker(0) = 1_B$, so $\alpha$ is an isomorphism.

More directly: by axiom (ii) of abelian categories, every monomorphism is the kernel of its cokernel. Since $\alpha$ is both monic and epic, $\alpha = \ker(\operatorname{coker} \alpha)$. But $\operatorname{coker} \alpha = 0$ (the zero morphism from $B$ to $0$) because $\alpha$ is epic. And $\ker(0: B \to 0) = 1_B$, so $\alpha: A \to B$ must be the kernel, i.e., there exists an isomorphism $\varphi: B \to A$ such that $\alpha \circ \varphi = 1_B$ and a morphism $\psi: A \to B$ with $\varphi \circ \alpha = \psi$. By the kernel property, $\alpha$ is the equalizer of $0$ and the zero morphism, which means $\alpha$ is an isomorphism.

Equivalently, in the factorization $\alpha = \nu \circ \eta$ with $\eta$ epic and $\nu$ monic, the fact that $\alpha$ is already epic forces $\nu$ to be epic (and monic), hence an isomorphism; similarly $\eta$ must be monic (and epic), hence an isomorphism. Thus $\alpha = \nu \circ \eta$ is a composition of isomorphisms, hence an isomorphism.

This property is characteristic of abelian categories; it fails in general categories (e.g., a continuous bijection between topological spaces need not be a homeomorphism).
