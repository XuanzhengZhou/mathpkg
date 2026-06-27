---
role: proof
locale: en
of_concept: connected-subspace-duality
source_book: gtm054
source_chapter: "II"
source_section: "IIC"
---

**Proof of C11 Lemma.**

By duality it suffices to prove this lemma in just one direction. Suppose $\operatorname{Fnd}(\mathcal{A}) = U$ and that $\mathcal{A}$ is connected, and let $x \in U \setminus \operatorname{Fnd}(\mathcal{A}^{\perp})$. By Exercise C10(c), $\mathcal{P}(\{x\})$ is a component of $\mathcal{A}$. Since $|U| \geq 2$, this implies $\mathcal{A}$ has a nontrivial component distinct from $\mathcal{A}$ itself, so $\mathcal{A}$ is not connected, contrary to assumption. Hence $\operatorname{Fnd}(\mathcal{A}^{\perp}) = U$.

Now suppose $\mathcal{A}^{\perp} = \mathcal{B}_1 \oplus \mathcal{B}_2$ with both $\mathcal{B}_1, \mathcal{B}_2$ nontrivial. Let $\mathcal{A}_i$ be the orthogonal complement of $\mathcal{B}_i$ in $\mathcal{P}(\operatorname{Fnd}(\mathcal{B}_i))$ for $i = 1, 2$. Then by the duality of orthogonal complements, $\mathcal{A} = \mathcal{A}_1 \oplus \mathcal{A}_2$, and both $\mathcal{A}_i$ are nontrivial, contradicting the connectedness of $\mathcal{A}$. Hence $\mathcal{A}^{\perp}$ is connected.
