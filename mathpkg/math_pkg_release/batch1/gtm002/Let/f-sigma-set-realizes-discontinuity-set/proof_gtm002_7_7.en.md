---
role: proof
locale: en
of_concept: f-sigma-set-realizes-discontinuity-set
source_book: gtm002
source_chapter: "7"
source_section: "7"
---

Let $E = \bigcup F_n$, where each $F_n$ is closed. We may assume that $F_n \subset F_{n+1}$ for all $n$. Let $A_n$ denote the set of rational points in $F_n$, together with all isolated points of $F_n$. Each $A_n$ is countable, so we may enumerate $A_n$ as $\{a_{n1}, a_{n2}, \ldots\}$. For each pair $(n,k)$ define a continuous function $f_{nk}$ on $\mathbb{R}$ such that $f_{nk}(a_{nk}) = 1$, $0 \leq f_{nk}(x) \leq 1$ for all $x$, and $f_{nk}$ vanishes outside an interval of length $1/n$ centered at $a_{nk}$. Let $f_n(x) = \sup_k f_{nk}(x)$; then $f_n$ is lower semi-continuous and its set of points of discontinuity is exactly $F_n$.

Let $\{a_n\}$ be a sequence of positive numbers such that $a_n > \sum_{i>n} a_i$ for every $n$ (for instance, $a_n = 1/n!$). Then the series $\sum_{n=1}^{\infty} a_n f_n(x)$ converges uniformly on $\mathbb{R}$ to a bounded function $f$. The function $f$ is continuous at any point where all of the terms are continuous, hence at each point of $\mathbb{R} - E$. On the other hand, at each point of $F_n - F_{n-1}$ the oscillation of $f$ is at least equal to $a_n - \sum_{i>n} a_i > 0$. Hence the set of points of discontinuity of $f$ is exactly $E$.
