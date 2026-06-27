---
role: proof
locale: en
of_concept: generalized-distributive-law
source_book: gtm030
source_chapter: "2"
source_section: "1"
---

The generalized distributive law follows by induction on $m$ and $n$. For the base case $m = n = 1$, this is the ordinary distributive law. Assume the formula holds for some $m$ and $n$. Then for $m+1$:
\begin{align*}
(a_1 + \cdots + a_m + a_{m+1})(b_1 + \cdots + b_n) &= (a_1 + \cdots + a_m)(b_1 + \cdots + b_n) + a_{m+1}(b_1 + \cdots + b_n) \\
&= \sum_{i=1}^{m}\sum_{j=1}^{n} a_i b_j + \sum_{j=1}^{n} a_{m+1} b_j \\
&= \sum_{i=1}^{m+1}\sum_{j=1}^{n} a_i b_j.
\end{align*}
A symmetric induction on $n$ completes the proof, yielding:
$$(a_1 + a_2 + \cdots + a_m)(b_1 + b_2 + \cdots + b_n) = \sum_{i=1}^{m} \sum_{j=1}^{n} a_i b_j.$$
