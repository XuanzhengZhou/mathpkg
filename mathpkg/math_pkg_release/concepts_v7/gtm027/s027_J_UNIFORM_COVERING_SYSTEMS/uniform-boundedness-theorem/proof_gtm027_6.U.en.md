---
role: proof
locale: en
of_concept: uniform-boundedness-theorem
source_book: gtm027
source_chapter: "6"
source_section: "U"
---

# Proof of the Uniform Boundedness Theorem

Let $F$ be a family of continuous linear functions on a non-meager linear topological space $X$ with values in a linear topological space $Y$. Assume that for each $x \in X$, the set $\{f(x) : f \in F\}$ is bounded in $Y$.

For each neighborhood $V$ of $0$ in $Y$, define

$$K_V = \{x \in X : f(x) \in \overline{V} \text{ for all } f \in F\}.$$

Each $K_V$ is closed (intersection of closed sets $f^{-1}[\overline{V}]$) and convex (intersection of convex sets). Since $F$ is pointwise bounded, for each $x$ there exists $t > 0$ such that $f(sx) \in V$ for all $f \in F$ and $0 \leq s \leq t$. Hence $K_V$ contains a line segment in each direction. Also $K_V = -K_V$ by linearity.

By part (a), $K_V$ is a neighborhood of $0$. This means there exists a neighborhood $U$ of $0$ in $X$ such that $f[U] \subset \overline{V}$ for all $f \in F$, i.e., $F$ is *equicontinuous* at $0$.

Thus, for a non-meager domain, pointwise boundedness of a family of continuous linear maps implies equicontinuity. This is the Uniform Boundedness Principle (Banach-Steinhaus theorem) for topological vector spaces.
