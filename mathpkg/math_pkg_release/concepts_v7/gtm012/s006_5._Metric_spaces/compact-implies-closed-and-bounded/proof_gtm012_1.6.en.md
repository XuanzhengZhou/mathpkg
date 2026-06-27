---
role: proof
locale: en
of_concept: compact-implies-closed-and-bounded
source_book: gtm012
source_chapter: "1"
source_section: "6. Compactness"
---

# Proof of Proposition 6.1: Compact Sets are Closed and Bounded

Suppose $(S, d)$ is a metric space, $S \neq \varnothing$, and suppose $A \subset S$ is compact.

**Closed.** Suppose $y \notin A$. We want to show that $y$ is not a limit point of $A$. For each $x \in A$, let $r_x = \frac{1}{2} d(x, y) > 0$, and set $N(x) = B_{r_x}(x)$. The collection $\{N(x) : x \in A\}$ is an open cover of $A$. Since $A$ is compact, there exist finitely many points $x_1, x_2, \ldots, x_n \in A$ such that $A \subset \bigcup_{j=1}^{n} N(x_j)$. Let $r = \min\{r_{x_1}, r_{x_2}, \ldots, r_{x_n}\}$. Then $r > 0$.

We claim $B_r(y) \cap A = \varnothing$. Indeed, if $z \in B_r(y) \cap A$, then $z \in N(x_j)$ for some $j$, so $d(z, x_j) < r_{x_j}$. But then by the triangle inequality,

$$d(y, x_j) \leq d(y, z) + d(z, x_j) < r + r_{x_j} \leq 2r_{x_j} = d(y, x_j),$$

a contradiction. Thus $B_r(y) \cap A = \varnothing$, so $y$ is not a limit point of $A$. Hence every limit point of $A$ belongs to $A$, and $A$ is closed.

**Bounded.** Pick any $x_0 \in S$. The collection $\{B_n(x_0) : n = 1, 2, 3, \ldots\}$ is an open cover of $S$, hence covers $A$. By compactness of $A$, there is a finite subcover; let $N$ be the maximum of the indices in this subcover. Then $A \subset B_N(x_0)$, so $A$ is bounded. $\square$
