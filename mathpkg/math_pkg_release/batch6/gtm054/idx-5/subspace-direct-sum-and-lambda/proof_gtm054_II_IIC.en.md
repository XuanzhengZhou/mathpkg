---
role: proof
locale: en
of_concept: subspace-direct-sum-and-lambda
source_book: gtm054
source_chapter: "II"
source_section: "IIC"
---

**Proof of C6 Proposition.**

(a) This follows at once from Lemmas C3 and C5 and the definitions.

(b) Let $\mathcal{B}_i = \mathcal{A} \cap \mathcal{P}(V_i)$ for $i = 1, \ldots, k$. Clearly $\operatorname{Fnd}(\mathcal{B}_i) \subseteq V_i$. Hence $\bigoplus_{i=1}^{k} \mathcal{B}_i$ is a well-defined subspace of $\mathcal{A}$. Now let $A \in \mathcal{A}$. By Lemma C1, $A = \sum_{i=1}^{k} B_i$, where $B_i$ is a sum of sets in $\mathcal{E}_i \cap \mathcal{M}(\mathcal{A})$. Since for $i = 1, \ldots, k$, $B_i \in \mathcal{A}$ and $B_i \subseteq V_i$, we have $B_i \in \mathcal{B}_i$. Thus $A \in \bigoplus_{i=1}^{k} \mathcal{B}_i$, and we conclude that $\mathcal{A} = \bigoplus_{i=1}^{k} \mathcal{B}_i$.

By part (a) above, $\Lambda(\mathcal{A}) = \bigoplus_{i=1}^{k} \Lambda(\mathcal{B}_i)$. Since $\operatorname{Fnd}(\mathcal{B}_i) \subseteq V_i$, and $\Lambda(\mathcal{A}) = \bigoplus_{i=1}^{k} \Lambda_i$ with $\Lambda_i = (V_i, \mathcal{E}_i)$, it follows that $\Lambda_i = \Lambda(\mathcal{B}_i)$.
