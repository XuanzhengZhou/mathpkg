---
role: proof
locale: en
of_concept: inductive-characterization-of-sigma-relations
source_book: gtm037
source_chapter: "Part 1: Recursive Function Theory"
source_section: "5. Arithmetic Hierarchy"
---

The assertions for $\Delta_m$ follow from those for $\Sigma_m$ and $\Pi_m$. The assertions for $\Sigma_m$ and $\Pi_m$ are proved simultaneously by induction on $m$. The case $m = 0$ is trivial. Now assume the assertions for $m$. We take just one typical assertion for $m + 1$:

Assume $R, S \in \Sigma_{m+1}$; we show that $R \cap S \in \Sigma_{m+1}$. By 5.25, choose $(n + 1)$-ary $\Pi_m$-relations $R', S'$ such that for all $x_0, \ldots, x_{n-1} \in \omega$,

$$(x_0, \ldots, x_{n-1}) \in R \quad \text{iff} \quad \exists y \in \omega[(x_0, \ldots, x_{n-1}, y) \in R'],$$
$$(x_0, \ldots, x_{n-1}) \in S \quad \text{iff} \quad \exists y \in \omega[(x_0, \ldots, x_{n-1}, y) \in S'].$$

Then for any $x_0, \ldots, x_{n-1} \in \omega$,

$$(x_0, \ldots, x_{n-1}) \in R \cap S \quad \text{iff} \quad \exists y \in \omega \exists z \in \omega[(x_0, \ldots, x_{n-1}, y) \in R' \text{ and } (x_0, \ldots, x_{n-1}, z) \in S'].$$

Now let $R'' = \{(x_0, \ldots, x_{n+1}): (x_0, \ldots, x_n) \in R'\}$ and $S'' = \{(x_0, \ldots, x_{n+1}): (x_0, \ldots, x_{n-1}, x_{n+1}) \in S'\}$. Using 5.26 and 5.27 it is easy to see that $R \cap S \in \Sigma_{m+1}$.
