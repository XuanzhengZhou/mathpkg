---
role: proof
locale: en
of_concept: omega-u-equivalence-lemma
source_book: gtm037
source_chapter: "3"
source_section: "Decidable and Undecidable Theories"
---

First assume $\Omega x$; thus $\mathbf{B} x$, $\operatorname{Trans} x$, $\forall y \in x(\operatorname{Trans} y)$, and $\mathbf{W} x$. Hence $\mathbf{B}\,\mathbf{U} x$ and $\mathbf{W}\,\mathbf{U} x$ by 16.15 and 16.19. Suppose $z \in y \in \mathbf{U} x$. Then $z \in y \in x$ or $z \in y = x$, so $z \in x$ since $\operatorname{Trans} x$. Thus $\operatorname{Trans}\,\mathbf{U} x$. If $y \in \mathbf{U} x$, then $y \in x$ or $y = x$, so $\operatorname{Trans} y$ is clear. Thus $\Omega\,\mathbf{U} x$.

Now assume $\Omega\,\mathbf{U} x$, which means that $\mathbf{B}\,\mathbf{U} x$, $\operatorname{Trans}\,\mathbf{U} x$, $\forall y \in \mathbf{U} x(\operatorname{Trans} y)$, and $\mathbf{W}\,\mathbf{U} x$. The condition $\forall y \in \mathbf{U} x(\operatorname{Trans} y)$ means that $\operatorname{Trans} x$ and $\forall y \in x(\operatorname{Trans} y)$. And we have $\mathbf{B} x$ and $\mathbf{W} x$ by 16.13 and 16.18.
