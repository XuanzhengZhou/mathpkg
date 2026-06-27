---
role: proof
locale: en
of_concept: degree-of-sum-inequality
source_book: gtm030
source_chapter: "3"
source_section: "5"
---

Let $n = \deg f$ and $m = \deg g$. Write $f(x) = \sum_{i=0}^n a_i x^i$ and $g(x) = \sum_{i=0}^m b_i x^i$. The sum $f+g$ has terms of degree at most $\max(n,m)$. The coefficient of $x^{\max(n,m)}$ in the sum is $a_{\max(n,m)} + b_{\max(n,m)}$ (where $a_i = 0$ for $i > n$ and $b_i = 0$ for $i > m$). Hence the degree of the sum is at most $\max(n,m)$, with strict inequality occurring exactly when the leading coefficients cancel: $a_n = -b_n$ if $n = m$, or one polynomial dominates in degree.
