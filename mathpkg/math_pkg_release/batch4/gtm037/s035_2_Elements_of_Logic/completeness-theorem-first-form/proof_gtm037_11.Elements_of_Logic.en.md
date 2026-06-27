---
role: proof
locale: en
of_concept: completeness-theorem-first-form
source_book: gtm037
source_chapter: "11"
source_section: "Elements of Logic"
---

Let $\Gamma$ be a consistent set of sentences in the language $\mathcal{L}$. Let $\mathcal{L}'$ be obtained from $\mathcal{L}$ by adjoining $|\operatorname{Fmla}_{\mathcal{L}}|$ new individual constants. By Lemma 11.18, let $\Delta$ be a consistent rich set of sentences in $\mathcal{L}'$ with $\Gamma \subseteq \Delta$.

By the Lindenbaum-type lemma (11.13), extend $\Delta$ to a complete consistent set $\Theta$ of sentences in $\mathcal{L}'$ such that $\Delta \subseteq \Theta$. Since $\Theta$ extends a rich set, it remains rich (adding sentences only adds more provable implications, not removing the witnessing constants).

Now $\Theta$ is complete, rich, and consistent. By Theorem 11.12 (Henkin Model Existence), $\Theta$ has a model $\mathfrak{A}$ with $|A| \leq |\{\sigma : \sigma \text{ is a closed term of } \mathcal{L}'\}| \leq |\operatorname{Fmla}_{\mathcal{L}}|$.

Taking the $\mathcal{L}$-reduct $\mathfrak{A} \upharpoonright \mathcal{L}$, we obtain an $\mathcal{L}$-structure that is a model of $\Gamma$ (since $\Gamma \subseteq \Theta$ and restricting to the smaller language does not affect the truth of $\mathcal{L}$-sentences). The cardinality bound is preserved.
