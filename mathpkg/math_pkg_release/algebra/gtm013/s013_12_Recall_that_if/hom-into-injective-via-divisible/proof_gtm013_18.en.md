---
role: proof
locale: en
of_concept: hom-into-injective-via-divisible
source_book: gtm013
source_chapter: "5"
source_section: "18"
---

Let $I \leq {}_R R$ and suppose $h: I \to \operatorname{Hom}_{\mathbb{Z}}(R_R, Q)$ is an $R$-homomorphism. Define $\gamma: \mathbb{Z}I \to \mathbb{Z}Q$ by $\gamma(a) = [h(a)](1)$. This is an abelian group homomorphism. Since $\mathbb{Z}Q$ is injective (divisible), there exists $\bar{\gamma} \in \operatorname{Hom}_{\mathbb{Z}}(R, Q)$ such that $(\bar{\gamma} \mid I) = \gamma$.

Now for all $a \in I$ and $r \in R$:
$$(a\bar{\gamma})(r) = \bar{\gamma}(ra) = \gamma(ra) = [h(ra)](1) = [r \cdot h(a)](1) = [h(a)](r).$$
Thus $h(a) = a\bar{\gamma}$ for all $a \in I$. By the Injective Test Lemma (18.3), $\operatorname{Hom}_{\mathbb{Z}}(R_R, Q)$ is injective.
