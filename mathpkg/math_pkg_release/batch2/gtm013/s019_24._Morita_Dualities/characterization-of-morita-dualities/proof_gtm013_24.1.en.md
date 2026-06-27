---
role: proof
locale: en
of_concept: characterization-of-morita-dualities
source_book: gtm013
source_chapter: "7"
source_section: "24. Morita Dualities"
---

(a) $\Rightarrow$ (b). Since ${}_R R$ and $S_S$ are $U$-reflexive by definition and ${}_R U \cong (S_S)^*$, $U_S \cong ({}_R R)^*$, condition (b) follows from the definition of Morita duality (property (2)).

(b) $\Rightarrow$ (c). By hypothesis every factor module of ${}_R U$ and $U_S$ is $U$-reflexive. In particular, ${}_R U$ and $U_S$ are $U$-reflexive. The canonical map $\sigma_U: {}_R U \to U^{**}$ is an isomorphism, which implies ${}_R U_S$ is balanced (see (20.14)). Moreover, since every factor module of ${}_R R$ is $U$-reflexive, for every left ideal $I \leq {}_R R$ the factor ${}_R R/I$ is $U$-reflexive, hence $U$-torsionless. This means $U$ cogenerates every cyclic module, so ${}_R U$ is a cogenerator. The injectivity of ${}_R U$ follows from Baer's criterion: if every factor of ${}_R R$ is $U$-reflexive, then every homomorphism from a left ideal into $U$ extends to $R$, which is equivalent to $U$ being injective by (3.11) and (20.12). The symmetric argument applies to $U_S$.

(c) $\Rightarrow$ (a). Assume ${}_R U_S$ is balanced with ${}_R U$ and $U_S$ injective cogenerators. Then $U$ cogenerates $R/I$ for every left ideal $I$, so by (20.12), $\operatorname{Rej}_{R/I}(U) = 0$. Since ${}_R U$ is injective, the functor $(\cdot)^* = \operatorname{Hom}_R(-, U)$ is exact on short exact sequences of left $R$-modules. We must verify that ${}_R R$ and $S_S$ are $U$-reflexive and that submodules and factor modules of $U$-reflexive modules are $U$-reflexive.

First, since $U$ is a cogenerator, the evaluation maps $\sigma_R: {}_R R \to R^{**}$ and $\sigma_S: S_S \to S^{**}$ are monic. Exactness of $(\cdot)^*$ together with the fact that $U$ is balanced yields that these maps are isomorphisms; thus ${}_R R$ and $S_S$ are $U$-reflexive.

Now suppose $M$ is $U$-reflexive and $K \leq M$. Consider the exact sequence $0 \to K \to M \to M/K \to 0$. Applying the exact functor $(\cdot)^*$ twice yields a commutative diagram with exact rows. Since $\sigma_M$ is an isomorphism, it follows that $\sigma_{M/K}$ is monic and $\sigma_K$ is monic. Because $U$ is an injective cogenerator, the map $\sigma_{M/K}$ is in fact an isomorphism (see Exercise (3.11)), so $M/K$ is $U$-reflexive. Similarly $\sigma_K$ is an isomorphism, so $K$ is $U$-reflexive. Thus every submodule and factor module of a $U$-reflexive module is $U$-reflexive, and ${}_R U_S$ defines a Morita duality.
