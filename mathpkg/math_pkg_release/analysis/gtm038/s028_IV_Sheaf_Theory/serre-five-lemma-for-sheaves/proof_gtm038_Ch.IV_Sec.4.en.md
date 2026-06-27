---
role: proof
locale: en
of_concept: serre-five-lemma-for-sheaves
source_book: gtm038
source_chapter: "IV"
source_section: "4. Coherent Sheaves"
---

**Proof.** By exactness at $\mathcal{S}''$, we have $\operatorname{Im}j_1 = \operatorname{Ker}j_2$. Consider the short exact sequence
$$
0 \longrightarrow \mathcal{S}''/\operatorname{Im}j_1 \longrightarrow \mathcal{S} \longrightarrow \operatorname{Ker}p_2 \longrightarrow 0.
$$

Now $\mathcal{S}''/\operatorname{Im}j_1$ is coherent: since $\mathcal{S}''$ and $\mathcal{S}'$ are coherent, $\operatorname{Im}j_1 \simeq \mathcal{S}'/\operatorname{Ker}j_1$ is coherent by Theorem 4.7, and then $\mathcal{S}''/\operatorname{Im}j_1$ is coherent by Theorem 4.6(1).

Similarly, $\operatorname{Ker}p_2$ is coherent: the exact sequence $0 \to \operatorname{Ker}p_2 \to \mathcal{S}^* \to \mathcal{S}^{**}$ with $\mathcal{S}^*$ and $\mathcal{S}^{**}$ coherent implies $\operatorname{Ker}p_2$ is coherent (by the same argument as in Theorem 4.7 for kernels).

Since the outer terms $\mathcal{S}''/\operatorname{Im}j_1$ and $\operatorname{Ker}p_2$ are coherent, Theorem 4.3 implies that $\mathcal{S}$ is coherent. $\square$
