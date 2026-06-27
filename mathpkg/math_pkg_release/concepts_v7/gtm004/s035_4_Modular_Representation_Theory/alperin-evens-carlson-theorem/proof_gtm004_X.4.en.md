---
role: proof
locale: en
of_concept: alperin-evens-carlson-theorem
source_book: gtm004
source_chapter: "X. Survey of Some Applications"
source_section: "4. Modular Representation Theory"
---

# Proof of Theorem 4.3 (Alperin, Evens; Carlson) — Complexity Detection

Let $G$ be a finite group, $k$ a field of characteristic $p$, and $M$ an indecomposable $kG$-module. Denote by $c_G(M)$ the complexity of $M$, a numerical invariant generalizing the Krull dimension $c_G(k)$ of the cohomology ring (see Quillen's Theorem 4.2).

**Theorem 4.3 (Alperin, Evens; Carlson).** The complexity $c_G(M)$ of a module $M$ is the maximum of the complexities $c_E(M_E)$ of the restrictions $M_E$ of $M$ to the elementary abelian $p$-subgroups $E$ of $G$.

*Proof (sketch).* The theorem generalizes Quillen's result from the trivial module $k$ to an arbitrary indecomposable $kG$-module $M$.

The complexity $c_G(M)$ is defined through the rate of growth of the sequence

$$e_n = \dim_k \operatorname{Ext}_{kG}^n(M, M), \quad n = 0, 1, 2, \ldots$$

More precisely, $c_G(M)$ is the growth of $\{e_n\}$, i.e., the least integer $c \geq 0$ for which there exists $C > 0$ with $e_n \leq C n^{c-1}$ for all $n \geq 0$.

A crucial role in the proof is played by the Lyndon–Hochschild–Serre spectral sequence associated with a group extension (see Theorem 9.5 in Chapter VIII). This spectral sequence relates the cohomology of $G$ to that of a normal subgroup and the quotient group. Combined with restriction and induction techniques, one establishes that the complexity $c_G(M)$ is detected by the elementary abelian $p$-subgroups.

Specifically, for each elementary abelian $p$-subgroup $E \leq G$, the restriction map induces an inequality

$$c_E(M_E) \leq c_G(M).$$

The reverse direction — that $c_G(M)$ does not exceed the maximum of the $c_E(M_E)$ — is the deeper part and relies on the nilpotence of the kernel of the restriction to all elementary abelian $p$-subgroups acting on the cohomological support of $M$. This is the module-theoretic analogue of Quillen's nilpotence result for the cohomology ring itself.

Thus

$$c_G(M) = \max_{E \in \mathcal{E}} c_E(M_E),$$

where $\mathcal{E}$ is the set of elementary abelian $p$-subgroups of $G$. $\square$

The theorem shows that the complexity of a module, like the Krull dimension of the cohomology ring, is controlled by the $p$-local structure of $G$ and can be computed by examining restrictions to elementary abelian $p$-subgroups.
