---
role: proof
locale: en
of_concept: f-sigma-set-as-discontinuity-set
source_book: gtm002
source_chapter: "7"
source_section: "Functions of First Class"
---

Let $E = \bigcup F_n$, where each $F_n$ is closed. We may assume that $F_n \subset F_{n+1}$ for all $n$. Let $A_n$ denote the set of rational numbers in the complement of $F_n$, and let $f_n$ be the characteristic function of $A_n$. Each $f_n$ is continuous at every point of $F_n$ (since $F_n$ is closed and $A_n$ consists of isolated rational points outside $F_n$) and discontinuous at every point of the complement of $F_n$.

Choose a sequence of positive numbers $a_n$ such that $a_n > \sum_{i>n} a_i$ for every $n$. (For instance, let $a_n = 1/n!$.) Then the series $\sum_{n=1}^{\infty} a_n f_n(x)$ converges uniformly on $\mathbb{R}$ to a bounded function $f$. The function $f$ is continuous at any point where all of the terms are continuous, hence at each point of $\mathbb{R} - E$. On the other hand, at each point of $F_n - F_{n-1}$, the oscillation of $f$ is at least equal to $a_n - \sum_{i>n} a_i > 0$. Hence the set of points of discontinuity of $f$ is exactly $E$.
