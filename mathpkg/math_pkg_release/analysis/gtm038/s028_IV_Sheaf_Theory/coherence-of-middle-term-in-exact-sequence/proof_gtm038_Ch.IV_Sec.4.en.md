---
role: proof
locale: en
of_concept: coherence-of-middle-term-in-exact-sequence
source_book: gtm038
source_chapter: "IV"
source_section: "4. Coherent Sheaves"
---

**Proof.** 

1. **Finite generation:** Since $\mathcal{S}^{**}$ is coherent (hence finitely generated), for each $\mathfrak{z}_0 \in B$ there exist $W(\mathfrak{z}_0) \subset B$, $q^{**} \in \mathbb{N}$, and a sheaf epimorphism $\varepsilon^{**}: q^{**}\mathcal{O}|W \twoheadrightarrow \mathcal{S}^{**}|W$. Since $p$ is an epimorphism, $\varepsilon^{**}$ lifts to a homomorphism $\varepsilon: q^{**}\mathcal{O}|W \to \mathcal{S}|W$ with $p \circ \varepsilon = \varepsilon^{**}$.

Similarly, since $\mathcal{S}^*$ is coherent, there exists a sheaf epimorphism $\varepsilon^*: q^*\mathcal{O}|W \twoheadrightarrow \mathcal{S}^*|W$. Then $j \circ \varepsilon^*: q^*\mathcal{O}|W \to \mathcal{S}|W$.

Define $\varphi: (q^* + q^{**})\mathcal{O}|W \to \mathcal{S}|W$ by $\varphi(a^*, a^{**}) = j \circ \varepsilon^*(a^*) + \varepsilon(a^{**})$. By exactness and diagram chasing, $\varphi$ is surjective, so $\mathcal{S}$ is finitely generated.

2. **Kernel finite generation:** Given an arbitrary sheaf homomorphism $\varphi: q\mathcal{O}|U \to \mathcal{S}|U$, consider $p \circ \varphi: q\mathcal{O}|U \to \mathcal{S}^{**}|U$. Since $\mathcal{S}^{**}$ is coherent, $\operatorname{Ker}(p \circ \varphi)$ is finitely generated. Using coherence of $\mathcal{S}^*$ and exactness, one shows that $\operatorname{Ker}\varphi$ is also finitely generated.

Thus $\mathcal{S}$ satisfies both conditions for coherence. $\square$
