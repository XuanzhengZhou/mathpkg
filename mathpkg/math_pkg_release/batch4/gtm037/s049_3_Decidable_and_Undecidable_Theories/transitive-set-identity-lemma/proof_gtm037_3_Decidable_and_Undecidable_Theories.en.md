---
role: proof
locale: en
of_concept: transitive-set-identity-lemma
source_book: gtm037
source_chapter: "3"
source_section: "Decidable and Undecidable Theories"
---

Assume that $\operatorname{Trans} x$, $x \notin x$, and $\mathbf{U} x = \mathbf{U} y$. Take any $z \in x$. Then $z \in \mathbf{U} x = \mathbf{U} y$, so $z \in y$ or $z = y$; we shall show that $z = y$ is impossible. Assume $z = y$; thus $y \in x$. Since $x \in \mathbf{U} x$, we have $x \in \mathbf{U} y$ and hence $x \in y$ or $x = y$. Both cases lead to a contradiction with transitivity and $x \notin x$.
