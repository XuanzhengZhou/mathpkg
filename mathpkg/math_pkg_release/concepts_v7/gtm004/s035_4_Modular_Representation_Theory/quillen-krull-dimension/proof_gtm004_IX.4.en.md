---
role: proof
locale: en
of_concept: quillen-krull-dimension
source_book: gtm004
source_chapter: "IX. Relative Homological Algebra"
source_section: "4. Modular Representation Theory"
---

# Proof of Quillen's Theorem on Krull Dimension of Cohomology

Let $G$ be a finite group, $k$ a field of characteristic $p$, and $H^*(G, k)$ the cohomology ring of $G$.

**Theorem 4.2 (Quillen).** The Krull dimension $c(G)$ of $H^*(G, k)$ equals the $p$-rank of $G$, i.e., the maximal rank of the elementary abelian $p$-subgroups $E$ of $G$.

*Proof (outline).* Define the Krull dimension $c(G)$ via the growth rate of the Betti numbers $d_n = \dim_k H^n(G, k)$:

$$c(G) = \inf\left\{c \geq 0 \;\middle|\; \exists C > 0,\; d_n \leq C n^{c-1} \text{ for all } n \geq 0\right\}.$$

Observe that $c(G) = 1$ precisely when the sequence $\{d_n\}$ is uniformly bounded. Using the restriction map to a $p$-Sylow subgroup, one checks that this boundedness occurs exactly when the $p$-Sylow subgroup is cyclic, or, if $p = 2$, either cyclic or generalized quaternion.

Now let $\mathcal{E}$ denote the set of elementary abelian $p$-subgroups of $G$. For each $E \in \mathcal{E}$, the restriction $\operatorname{res}_{G,E}: H^*(G, k) \to H^*(E, k)$ is a ring homomorphism. The fundamental insight of Quillen [Q] is that the kernel of the product map

$$\Phi: H^*(G, k) \longrightarrow \prod_{E \in \mathcal{E}} H^*(E, k)$$

consists entirely of nilpotent elements. Therefore, modulo nilpotent elements, $H^*(G, k)$ embeds into a finite product of the cohomology rings $H^*(E, k)$. Since Krull dimension is unaffected by nilpotent elements, we obtain

$$c(G) = \max_{E \in \mathcal{E}} c(E).$$

For an elementary abelian $p$-group $E$ of order $p^n$, the cohomology ring $H^*(E, k)$ is well understood: for $p \neq 2$, its even part $H^{2*}(E, k)$ is a polynomial ring $\operatorname{Sym}^*(E^\vee)$ in $n$ generators, so $c(E) = n$; for $p = 2$, the full cohomology ring is polynomial in $n$ generators, also giving $c(E) = n$.

Thus

$$c(G) = \max_{E \in \mathcal{E}} \operatorname{rank}(E) = p\text{-rank}(G),$$

as claimed. $\square$

The result, previously conjectured by Atiyah and Swan, establishes a deep connection between the cohomological invariant $c(G)$ and the purely group-theoretic notion of $p$-rank. In the context of relative homological algebra (Chapter IX), this theorem serves as a foundation for the theory of cohomological varieties associated with $kG$-modules.
