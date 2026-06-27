---
role: proof
locale: en
of_concept: finite-cyclic-group-order
source_book: gtm030
source_chapter: "1"
source_section: "11"
---

Since the mapping is not 1-1, $a^m = a^n$ for $m \neq n$. Assume $n > m$. Then
$$a^{n-m} = a^n a^{-m} = a^m a^{-m} = 1.$$
Hence there exist positive integers $p$ such that $a^p = 1$. Let $r$ be the smallest such positive integer.

To prove distinctness: if $a^k = a^l$ for $k \neq l$ with $k, l \in \{0, 1, \ldots, r-1\}$, assume $k > l$. Then $a^{k-l} = 1$ with $0 < k-l < r$, contradicting the minimality of $r$.

To prove every element is in this set: let $a^n$ be arbitrary. Write $n = qr + s$ with $0 \leq s < r$ (division algorithm). Then
$$a^n = a^{qr+s} = a^{qr} a^s = (a^r)^q a^s = 1^q a^s = a^s.$$
Thus $\mathfrak{Z} = \{1, a, \ldots, a^{r-1}\}$ has order $r$.
