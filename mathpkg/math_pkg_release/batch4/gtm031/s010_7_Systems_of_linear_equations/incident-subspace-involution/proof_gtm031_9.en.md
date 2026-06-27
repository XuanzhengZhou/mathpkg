---
role: proof
locale: en
of_concept: incident-subspace-involution
source_book: gtm031
source_chapter: "II"
source_section: "9"
---

The mapping $\mathfrak{S} \mapsto j(\mathfrak{S})$ is clearly order-reversing: $\mathfrak{S}_1 \supseteq \mathfrak{S}_2$ implies $j(\mathfrak{S}_1) \subseteq j(\mathfrak{S}_2)$. To show it is $1$-$1$, suppose $j(\mathfrak{S}_1) = j(\mathfrak{S}_2)$. Then applying $j$ again gives $j(j(\mathfrak{S}_1)) = j(j(\mathfrak{S}_2))$. Using the complementary basis theorem, one proves $j(j(\mathfrak{S})) = \mathfrak{S}$ for all subspaces $\mathfrak{S}$, which yields $\mathfrak{S}_1 = \mathfrak{S}_2$. The surjectivity follows since for any $\mathfrak{S}^* \subseteq \mathfrak{R}^*$, taking $\mathfrak{S} = j(\mathfrak{S}^*)$ gives $\mathfrak{S}^* = j(j(\mathfrak{S}^*)) = j(\mathfrak{S})$.
