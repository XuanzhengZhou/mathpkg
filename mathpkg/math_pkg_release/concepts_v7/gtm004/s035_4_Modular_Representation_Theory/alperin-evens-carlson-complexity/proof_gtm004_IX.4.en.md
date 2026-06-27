---
role: proof
locale: en
of_concept: alperin-evens-carlson-complexity
source_book: gtm004
source_chapter: "IX. Relative Homological Algebra"
source_section: "4. Modular Representation Theory"
---

# Proof of the Alperin-Evens-Carlson Complexity Theorem

Let $G$ be a finite group, $k$ a field of characteristic $p$, and $M$ an indecomposable $kG$-module. The complexity $c_G(M)$ is a numerical invariant associated with $M$, defined via the rate of growth of the Ext-groups $\operatorname{Ext}_{kG}^n(M, M)$.

**Theorem 4.3 (Alperin, Evens; Carlson).** The complexity $c_G(M)$ of a module $M$ is the maximum of the complexities $c_E(M_E)$ of the restrictions $M_E$ of $M$ to the elementary abelian $p$-subgroups $E$ of $G$.

*Proof (outline).* The theorem is a module-theoretic generalization of Quillen's Theorem 4.2, which identifies the Krull dimension $c_G(k)$ of the cohomology ring with the $p$-rank of $G$.

Recall the definition: $c_G(M)$ is the growth of the integer sequence

$$e_n = \dim_k \operatorname{Ext}_{kG}^n(M, M), \qquad n = 0, 1, 2, \ldots$$

That is, $c_G(M)$ is the least integer $c \geq 0$ for which there exists a constant $C > 0$ such that $e_n \leq C n^{c-1}$ for all $n$.

The proof rests on two pillars. The first is the Lyndon–Hochschild–Serre spectral sequence (Theorem 9.5, Chapter VIII), which for a group extension $N \hookrightarrow G \twoheadrightarrow G/N$ provides a spectral sequence

$$E_2^{p,q} = H^p(G/N, H^q(N, M)) \implies H^{p+q}(G, M).$$

This spectral sequence is the principal technical tool for comparing cohomological invariants of $G$ with those of its subgroups and quotient groups.

The second pillar is the generalization of Quillen's nilpotence result to the module setting. For each elementary abelian $p$-subgroup $E \leq G$, restriction yields a map between Ext-groups. Collectively, these restriction maps detect complexity: one proves that

$$c_G(M) = \sup_{E \in \mathcal{E}} c_E(M_E),$$

where $\mathcal{E}$ denotes the set of elementary abelian $p$-subgroups of $G$. The inequality $c_E(M_E) \leq c_G(M)$ follows from standard restriction properties. The reverse inequality relies on the fact that the kernel of the cohomological restriction to all $E \in \mathcal{E}$ lies in the nilradical of the cohomology ring, and complexity is invariant modulo nilpotent elements.

Combining these ingredients yields the claimed equality. $\square$

In the framework of relative homological algebra (Chapter IX), this theorem shows that the complexity invariant, like relative projectivity and the theory of vertices and sources, is controlled by the $p$-local subgroup structure of $G$.
