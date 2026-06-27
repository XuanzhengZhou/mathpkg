---
role: proof
locale: en
of_concept: lebesgue-covering-lemma-compact-metric
source_book: gtm043
source_chapter: "16"
source_section: "21"
---
Let $\mathcal{U} = \{U_k\}_{k \leq s}$. For each $k \leq s$, write
$$f_k(x) = d(x, X - U_k) \quad (x \in X),$$
$d$ denoting the metric; this defines $f_k$ as a continuous function on $X$, and we have $f_k(x) > 0$ for all $x \in U_k$. Since $\mathcal{U}$ is a cover, the continuous function $f_1 \vee \cdots \vee f_s$ is everywhere positive on $X$; since $X$ is compact, this function has a positive lower bound $\epsilon$. Hence, for each point $x$, there exists $k$ for which $f_k(x) \geq \epsilon$. It follows that the cell $\{y : d(x, y) < \epsilon\}$ is contained in $U_k$.
