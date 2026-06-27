---
role: proof
locale: en
of_concept: j-op-closure-lemma
source_book: gtm037
source_chapter: "3"
source_section: "Decidable and Undecidable Theories"
---

Assume that $\mathbf{J} x$, $y$ is arbitrary, $z = \mathbf{Op}(x, y)$, $w \subseteq z$, and $v$ is arbitrary. We want to show that $w \cap z$ has its usual meaning, i.e., that $\exists u \forall s (s \in u \leftrightarrow s \in w \land s \in v)$. Since $\mathbf{J} x$, both $x \cap x$ and $(x \cap x) \cap (w \cap x v)$ have their usual meanings. If $y \notin w$ or $y \notin v$, then the intersection reduces to the $x$-case which is already covered by $\mathbf{J} x$.
