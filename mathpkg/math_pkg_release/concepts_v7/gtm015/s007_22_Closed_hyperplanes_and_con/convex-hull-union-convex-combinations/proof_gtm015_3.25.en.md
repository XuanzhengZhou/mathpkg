---
role: proof
locale: en
of_concept: convex-hull-union-convex-combinations
source_book: gtm015
source_chapter: "3"
source_section: "25"
---

# Proof of Convex hull of a union expressed as convex combinations

Let $(A_i)_{i \in I}$ be a family of convex subsets of $E$ and let $S = \bigcup_{i \in I} A_i$. Let $A$ be the set of all convex combinations

$$x = \sum_{i \in I} \lambda_i x_i,$$

where $\lambda_i = 0$ for all but finitely many $i$, $\lambda_i \ge 0$ for all $i$, $\sum_{i \in I} \lambda_i = 1$, and $x_i \in A_i$ whenever $\lambda_i > 0$.

Clearly $A \supset S$ (take $\lambda_i = 1$ for one index) and $A$ is convex: if $x = \sum \lambda_i x_i$ and $y = \sum \mu_i y_i$ are in $A$, then for $0 \le \alpha \le 1$,

$$\alpha x + (1 - \alpha) y = \sum_i [\alpha \lambda_i x_i + (1 - \alpha) \mu_i y_i] = \sum_i \gamma_i z_i$$

where $\gamma_i = \alpha \lambda_i + (1 - \alpha) \mu_i$ and $z_i$ is a convex combination of $x_i$ and $y_i$ in $A_i$. Thus $A$ is a convex set containing $S$, so $A \supset \operatorname{conv} S$.

Conversely, every convex combination of elements from $S$ belongs to $\operatorname{conv} S$, so $A \subset \operatorname{conv} S$.
