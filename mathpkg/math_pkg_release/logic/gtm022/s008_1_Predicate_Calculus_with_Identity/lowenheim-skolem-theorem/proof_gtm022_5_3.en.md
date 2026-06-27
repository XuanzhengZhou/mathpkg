---
role: proof
locale: en
of_concept: lowenheim-skolem-theorem
source_book: gtm022
source_chapter: "V"
source_section: "3"
---

\textbf{Proof.} Suppose $\mathcal{T} = (\mathcal{R}, A, C)$. Choose some set $V_0 \supset C$ such that $|V_0 - C| = \aleph$. Then $|P(V_0, \mathcal{R})| = \aleph$. Put

\[
A'_0 = I \cup A \cup \{\sim \mathcal{I}(x, y) \mid x, y \in V_0 - C, x \neq y\}.
\]

The set $A'_0$ asserts that all the new variables in $V_0 - C$ denote distinct elements. One then shows that every finite subset of $A'_0$ is satisfiable in some model of $\mathcal{T}$ (using the infinite model to accommodate finitely many distinctness requirements). By compactness, $A'_0$ has a model $M$. In $M$, the elements interpreting the variables in $V_0 - C$ are all distinct, so $|M| \geqslant \aleph$. On the other hand, since $|P(V_0, \mathcal{R})| = \aleph$, a suitable downward Löwenheim-Skolem argument yields a submodel of cardinality exactly $\aleph$, which remains a model of $\mathcal{T}$.
