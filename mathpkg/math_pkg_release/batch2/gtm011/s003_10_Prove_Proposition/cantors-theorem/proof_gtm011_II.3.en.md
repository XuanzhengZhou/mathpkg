---
role: proof
locale: en
of_concept: cantors-theorem
source_book: gtm011
source_chapter: "II"
source_section: "3"
---

Suppose $(X, d)$ is complete and let $\{F_n\}$ be a sequence of closed sets having the properties: (i) $F_1 \supset F_2 \supset \ldots$ and (ii) $\lim \operatorname{diam} F_n = 0$. For each $n$, let $x_n$ be an arbitrary point in $F_n$; if $n, m \geq N$ then $x_n, x_m$ are in $F_N$ so that, by definition, $d(x_n, x_m) \leq \operatorname{diam} F_N$. By the hypothesis $N$ can be chosen sufficiently large that $\operatorname{diam} F_N < \epsilon$; this shows that $\{x_n\}$ is a Cauchy sequence. Since $X$ is complete, $x_0 = \lim x_n$ exists. Also, $x_n$ is in $F_N$ for all $n \geq N$ since $F_n \subset F_N$; hence, $x_0$ is in $F_N$ for every $N$ and this gives $x_0 \in \bigcap_{n=1}^{\infty} F_n = F$. So $F$ contains at least one point; if, also, $y$ is in $F$ then both $x_0$ and $y$ are in $F$ and $d(x_0, y) \leq \operatorname{diam} F_n$ for each $n$, so $d(x_0, y) = 0$ and $x_0 = y$.
