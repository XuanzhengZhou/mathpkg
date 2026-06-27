---
role: proof
locale: en
of_concept: c-op-closure-lemma
source_book: gtm037
source_chapter: "3"
source_section: "Decidable and Undecidable Theories"
---

Assume that $\mathbf{C} x$, $y$ is arbitrary, $z = \mathbf{Op}(x, y)$, and $w$ is arbitrary; we want to show that $z \sim w$ has its usual sense. If $y \in w$, then $\forall u(u \in (x \sim w) \leftrightarrow u \in z \land u \notin w)$, since $\mathbf{C} x$. If $y \notin w$, then $\forall u(u \in \mathbf{Op}(x \sim w, y) \leftrightarrow u \in z \land u \notin w)$.
