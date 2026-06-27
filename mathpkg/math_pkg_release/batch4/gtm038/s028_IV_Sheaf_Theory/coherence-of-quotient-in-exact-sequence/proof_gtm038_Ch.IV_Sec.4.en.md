---
role: proof
locale: en
of_concept: coherence-of-quotient-in-exact-sequence
source_book: gtm038
source_chapter: "IV"
source_section: "4. Coherent Sheaves"
---

**Proof.**

1. **Finite generation:** Since $p$ is surjective, for any $\sigma^{**} \in \mathcal{S}^{**}_{\mathfrak{z}}$ there exists $\sigma \in \mathcal{S}_{\mathfrak{z}}$ with $p(\sigma) = \sigma^{**}$. Because $\mathcal{S}$ is finitely generated, for each $\mathfrak{z}_0 \in B$ there is a neighborhood $W(\mathfrak{z}_0)$ and an epimorphism $\varphi: q\mathcal{O}|W \twoheadrightarrow \mathcal{S}|W$. Then $p \circ \varphi: q\mathcal{O}|W \to \mathcal{S}^{**}|W$ is also an epimorphism, so $\mathcal{S}^{**}$ is finitely generated.

2. **Kernel finite generation:** Let $\varepsilon^{**}: q^{**}\mathcal{O}|U \to \mathcal{S}^{**}|U$ be an arbitrary sheaf homomorphism. Since $p$ is an epimorphism, there exists a lifting $\varepsilon: q^{**}\mathcal{O}|U \to \mathcal{S}|U$ with $p \circ \varepsilon = \varepsilon^{**}$.

For any $\mathfrak{z}_0 \in U$, since $\mathcal{S}^*$ is finitely generated, there exist a neighborhood $V(\mathfrak{z}_0) \subset U$, $q^* \in \mathbb{N}$, and an epimorphism $\varepsilon^*: q^*\mathcal{O}|V \twoheadrightarrow \mathcal{S}^*|V$.

Consider the homomorphism $\psi := j \circ \varepsilon^*: q^*\mathcal{O}|V \to \mathcal{S}|V$. By the coherence of $\mathcal{S}$, the sum $\psi \oplus \varepsilon: (q^* + q^{**})\mathcal{O}|V \to \mathcal{S}|V$ has finitely generated kernel. Through diagram chasing in the exact sequence, one deduces that $\operatorname{Ker}\varepsilon^{**}$ is also finitely generated.

Therefore $\mathcal{S}^{**}$ is coherent. $\square$
