---
role: introduce
locale: en
content_hash: ""
written_against: ""
---

Order statistics are the sorted values of a random sample and form the backbone of nonparametric statistics. The density of the $k$-th order statistic has a natural interpretation: for $X^{(k)}$ to be near $x$, one observation must be near $x$, $k-1$ must be below it, and $n-k$ above it — hence the factors $f(x)$, $F(x)^{k-1}$, and $(1-F(x))^{n-k}$ with the multinomial coefficient $n!/((k-1)!1!(n-k)!)$. Order statistics are essential for quantile estimation, robust statistics (median), and extreme value theory (minima and maxima).
