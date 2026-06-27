---
role: introduce
locale: en
content_hash: ""
written_against: ""
---

**Theorem 4.8 (Serre's Five Lemma for Sheaves)** is a coherence criterion for the middle term of a five-term exact sequence. If the four outer sheaves $\mathcal{S}', \mathcal{S}'', \mathcal{S}^*, \mathcal{S}^{**}$ are coherent, then the middle sheaf $\mathcal{S}$ is also coherent.

The proof uses the factorization of the sequence through intermediate quotients. By exactness, $\operatorname{Im}j_1 = \operatorname{Ker}j_2$, and the sequence $0 \to \mathcal{S}''/\operatorname{Im}j_1 \to \mathcal{S} \to \operatorname{Ker}p_2 \to 0$ is exact. One then applies Theorem 4.3 (coherence of middle term) to this short exact sequence.

This lemma is essential for establishing coherence properties in longer exact sequences and is the sheaf-theoretic analog of the classical Five Lemma in homological algebra.
