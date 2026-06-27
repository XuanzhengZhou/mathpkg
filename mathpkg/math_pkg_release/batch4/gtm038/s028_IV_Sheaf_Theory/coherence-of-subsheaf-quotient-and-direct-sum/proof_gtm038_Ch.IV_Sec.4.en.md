---
role: proof
locale: en
of_concept: coherence-of-subsheaf-quotient-and-direct-sum
source_book: gtm038
source_chapter: "IV"
source_section: "4. Coherent Sheaves"
---

**Proof.**

1. There is a canonical short exact sequence
$$
0 \longrightarrow \mathcal{S}^* \longrightarrow \mathcal{S} \longrightarrow \mathcal{S}/\mathcal{S}^* \longrightarrow 0.
$$
Since $\mathcal{S}^*$ and $\mathcal{S}$ are coherent, Theorem 4.4 implies that $\mathcal{S}/\mathcal{S}^*$ is coherent.

2. For $\ell = 2$, consider the exact sequence
$$
0 \longrightarrow \mathcal{S}_1 \xrightarrow{j_1} \mathcal{S}_1 \oplus \mathcal{S}_2 \xrightarrow{p_2} \mathcal{S}_2 \longrightarrow 0.
$$
Since $\mathcal{S}_1$ and $\mathcal{S}_2$ are coherent, Theorem 4.3 implies $\mathcal{S}_1 \oplus \mathcal{S}_2$ is coherent. For $\ell > 2$, use induction and the isomorphism
$$
\mathcal{S}_1 \oplus \cdots \oplus \mathcal{S}_\ell \simeq (\mathcal{S}_1 \oplus \cdots \oplus \mathcal{S}_{\ell-1}) \oplus \mathcal{S}_\ell.
$$
$\square$
