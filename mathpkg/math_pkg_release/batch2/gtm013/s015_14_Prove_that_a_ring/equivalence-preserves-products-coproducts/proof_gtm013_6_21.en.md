---
role: proof
locale: en
of_concept: equivalence-preserves-products-coproducts
source_book: gtm013
source_chapter: "6"
source_section: "21"
---

Adopt the notation of (21.1). Each part is proved using the Fundamental Lemma (21.3).

**(1) Products**: Suppose $(M, (p_\alpha))$ is a product of $(M_\alpha)$ in ${}_R \mathbf{M}$. For any $S$-module $N$ and morphisms $g_\alpha: N \to F(M_\alpha)$, consider $\phi^{-1}(g_\alpha): G(N) \to M_\alpha$. By the universal property of $(M, (p_\alpha))$, there exists a unique $h: G(N) \to M$ with $p_\alpha h = \phi^{-1}(g_\alpha)$. Applying $\phi$ and using (21.3.3), we get $F(p_\alpha) \phi^{-1}(h) = g_\alpha$, and uniqueness follows from the bijectivity of $\phi$. The converse is symmetric using $G$.

**(2) Coproducts**: Dual to (1), using $\theta$ instead of $\phi$.

**(3) Generation**: $U$ generates $M$ means there is an epimorphism $U^{(A)} \to M \to 0$. By (2), $F$ preserves coproducts, and by (21.2) it preserves epimorphisms, so $F(U)^{(A)} \to F(M) \to 0$ is an epimorphism. Similarly for cogeneration, using monomorphisms and products.

**(4) Generator/Cogenerator/Faithful**: Follows directly from (3). For faithfulness, recall that $U$ is faithful iff it cogenerates a generator (Exercise 8.3).

**(5) Essential/Superfluous**: Suppose $g: F(M') \to N$ is such that $g F(f)$ is monic. Then by (21.3), $\phi(gF(f)) = \phi(g)f$ is monic. Since $f$ is essential, $\phi(g)$ must be monic, and by (21.3), $g$ is monic. Thus $F(f)$ is essential. The converse uses $G$.

**(6) Injective envelope/Projective cover**: An injective envelope is an essential monomorphism with injective domain. Both essential monomorphisms (by (5)) and injectivity (by (21.2) and the definition) are preserved. Similarly for projective covers.
