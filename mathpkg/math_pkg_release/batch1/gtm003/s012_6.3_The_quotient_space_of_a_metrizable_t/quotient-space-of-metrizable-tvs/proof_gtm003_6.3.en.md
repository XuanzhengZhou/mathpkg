---
role: proof
locale: en
of_concept: quotient-space-of-metrizable-tvs
source_book: gtm003
source_chapter: "I"
source_section: "6.3"
---

We note first that $\hat{x} \rightarrow |\hat{x}|$ satisfies (i)-(iii) of (6.1). Clearly, $|\hat{0}| = 0$; if $|\hat{x}| = 0$, then $0 \in \hat{x}$, since $M$ is closed. For (ii), let $\varepsilon > 0$ be given; then $|x| < |\hat{x}| + \varepsilon$, $|y| < |\hat{y}| + \varepsilon$ for suitable $x \in \hat{x}$, $y \in \hat{y}$; now,

$$|\hat{x} + \hat{y}| \leq |x + y| \leq |x| + |y| \leq |\hat{x}| + |\hat{y}| + 2\varepsilon.$$

(i) follows from the corresponding property of $x \rightarrow |x|$ on $L$, since the quotient map $x \rightarrow \hat{x}$ is linear.

Let $V_n = \{x: |x| < n^{-1}\}$ for $n \in \mathbb{N}$. Then $\{V_n\}$ is a $0$-neighborhood base in $L$; hence $\{\phi(V_n)\}$ is a $0$-neighborhood base in $L/M$, since the natural map $x \rightarrow \hat{x} = \phi(x)$ is continuous and open. This shows that $\hat{x} \rightarrow |\hat{x}|$ generates the quotient topology.

For completeness: if $L$ is complete, let $(\hat{x}_n)$ be a Cauchy sequence in $L/M$. One can select a subsequence and representatives $x_n \in \hat{x}_n$ such that $(x_n)$ is Cauchy in $L$, hence converges; then $(\hat{x}_n)$ converges in $L/M$.
