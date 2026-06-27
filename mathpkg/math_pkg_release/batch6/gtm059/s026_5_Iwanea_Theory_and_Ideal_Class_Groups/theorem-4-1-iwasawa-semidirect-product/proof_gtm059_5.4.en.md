---
role: proof
locale: en
of_concept: theorem-4-1-iwasawa-semidirect-product
source_book: gtm059
source_chapter: "5"
source_section: "4"
---

*Proof.* We have an exact sequence
$$1 \to G_1 \to G \to \operatorname{Gal}(K_\infty / K) \cong \mathbb{Z}_p \to 1$$
where the map $G \to \operatorname{Gal}(K_\infty/K)$ is given by restriction. 

Let $I$ be the inertia group of the unique ramified prime $\mathfrak{p}$ in $G$. The restriction of $I$ to $K_\infty$ gives a homomorphism $I \to \operatorname{Gal}(K_\infty/K)$. We claim this is surjective: since $K_\infty/K$ is totally ramified at $\mathfrak{p}$, the image of the inertia group must map onto the full Galois group of the totally ramified extension.

Moreover, $I \cap G_1 = \{1\}$ because $G_1 = \operatorname{Gal}(M_\infty/K_1)$ and $K_1/K$ is totally ramified at $\mathfrak{p}$, so the extension $M_\infty/K_1$ is unramified (it is the maximal unramified $p$-extension). The inertia at $\mathfrak{p}$ in $G_1$ is trivial since $K_1$ already captures the ramification. Thus the intersection of the inertia group $I$ (which only has non-trivial inertia at $\mathfrak{p}$) with $G_1$ is trivial. This shows $G = G_1 \rtimes I$.

For (ii): Since $I \cong \mathbb{Z}_p$ is abelian and operates on $G_1$ by conjugation, and $G_1$ is pro-$p$ abelian, the semidirect product structure implies $[G, G] \subseteq G_1$. The maximal abelian quotient of $G$ is $G/[G,G] \cong G_1/[G,G] \times I$, and since the extension $M_\infty/K$ is the maximal $p$-abelian unramified extension, $G$ is pro-$p$. Using class field theory, one shows $G_1 = [G, G]$.

For (iii): This follows directly from (i) since the semidirect product $G_1 \rtimes I$ with $I \cong \mathbb{Z}_p$ gives the split exact sequence as stated.
