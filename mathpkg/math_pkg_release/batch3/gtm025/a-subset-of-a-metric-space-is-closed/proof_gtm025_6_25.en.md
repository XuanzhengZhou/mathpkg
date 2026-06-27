---
role: proof
locale: en
of_concept: "a-subset-of-a-metric-space-is-closed"
source_book: gtm025
source_chapter: "Topology"
source_section: "6.25"
---

Suppose that $A$ is closed and let $(x_n)$ be a sequence with values in $A$ for which a limit $x$ in $X$ exists. If $x$ were in $A'$, then $A'$ would be a neighborhood of $x$, and so all but a finite number of the values $x_n$ would lie in $A'$ — a contradiction.

Conversely, suppose that $A$ is not closed. Then by (6.7.v), $A$ has a limit point $x$ such that $x \notin A$. For each $n \in N$, choose $x_n \in A \cap B_{\frac{1}{n}}(x)$. Then $(x_n) \subset A$, $x_n \to x$, and $x \notin A$.
