---
role: proof
locale: en
of_concept: hyperplane-linear-form-characterization
source_book: gtm003
source_chapter: "2"
source_section: "4"
---

If $f \in L^*$ is non-zero, then $M = f^{-1}(0)$ is a maximal proper subspace of $L$ (since $\dim L/M = 1$). Given any $x_0 \in L$ with $f(x_0) = \alpha$, the set $H = \{x : f(x) = \alpha\} = x_0 + M$ is a translate of $M$, hence a hyperplane.

Conversely, let $H$ be a hyperplane with corresponding subspace $M$ of codimension $1$. Choose $x_0 \in H$ so that $H = x_0 + M$. Since $L/M$ is one-dimensional, we can define a linear form $f$ by $f(x_0 + m) = f(x_0)$ for all $m \in M$. Setting $\alpha = f(x_0)$, we obtain $H = \{x : f(x) = \alpha\}$. The non-uniqueness of $f$ and $\alpha$ follows from the fact that if $H = \{x : g(x) = \beta\}$ for another pair $(g, \beta)$, then $g = \beta f / \alpha$, so $f$ and $g$ differ by the common factor $\beta/\alpha$.
