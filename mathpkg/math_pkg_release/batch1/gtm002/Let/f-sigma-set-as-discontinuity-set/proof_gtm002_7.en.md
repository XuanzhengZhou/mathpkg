---
role: proof
locale: en
of_concept: f-sigma-set-as-discontinuity-set
source_book: gtm002
source_chapter: "7"
source_section: "7. Functions of First Class"
---

Let $E = \bigcup F_n$, where $F_n$ is closed. We may assume that $F_n \subset F_{n+1}$ for all $n$. Let $A_n$ denote the set of rational numbers such that $a_n > \sum_{i>n} a_i$ for every $n$ (for instance, let $a_n = 1/n!$). Define $f_n$ to be the indicator function of $F_n$ with appropriate modifications, and consider the series $\sum_{n=1}^{\infty} a_n f_n(x)$. This series converges uniformly on $\mathbb{R}$ to a bounded function $f$.

$f$ is continuous at any point where all of the terms are continuous, hence at each point of $\mathbb{R} - E$. On the other hand, at each point of $F_n - F_{n-1}$ the oscillation of $f$ is at least equal to $a_n - \sum_{i>n} a_i$. Hence the set of points of discontinuity of $f$ is exactly $E$.
