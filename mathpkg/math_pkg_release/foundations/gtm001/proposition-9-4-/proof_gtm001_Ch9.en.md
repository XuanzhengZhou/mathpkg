---
role: proof
locale: en
of_concept: proposition-9-4-
source_book: gtm001
source_chapter: "9"
source_section: ""
---

** Let $a \in B$. By Proposition 9.3 there exists a set $b$ such that

$$\{a\} \subseteq b \subseteq A \wedge (\forall x \in A)(\forall y)[x R y \wedge y \in b \rightarrow x \in b]$$.

Then $b \cap B$ is a nonempty subset of $A$. Therefore

$(\exists x \in b \cap B)[(b \cap B) \cap (R^{-1})"\{x\} = 0]$.

If $y \in B \cap (R^{-1})"\{x\}$, then $y \in B$ and $y R x$. But $x \in b$ and hence $y \in b$. Thus

$$y \in [b \cap B \cap (R^{-1})"\{x\}]$$.

Therefore $B \cap (R^{-1})"\{x\} = 0$.

**Remark.** Note in Proposition 9.4 that the set $b$ has the property that $(R^{-1})"\{b\}$ is a subset of $b$. We say that $b$ is closed with respect to (w.r.t) the binary relation $R^{-1}$.
