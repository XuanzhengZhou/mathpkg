---
role: proof
locale: en
of_concept: open-iff-complement-closed
source_book: gtm012
source_chapter: "1"
source_section: "5. Metric spaces"
---

# Proof of Proposition 5.3: Open if and only if Complement is Closed

Let $(S, d)$ be a metric space and let $A \subset S$. Let $B$ be the complement of $A$ in $S$.

**($\Leftarrow$)** Suppose $B$ is closed and suppose $x \in A$. Then $x$ is not a limit point of $B$, so for some $r > 0$ we have $B_r(x) \cap B = \varnothing$. Thus $B_r(x) \subset A$, and $A$ is a neighborhood of $x$. Since $x$ was arbitrary, $A$ is open.

**($\Rightarrow$)** Conversely, suppose $A$ is open and suppose $x \notin B$. Then $x \in A$, so for some $r > 0$ we have $B_r(x) \subset A$. Then $B_r(x) \cap B = \varnothing$, and $x$ is not a limit point of $B$. It follows that every limit point of $B$ is in $B$; hence $B$ is closed. $\square$
