---
role: proof
locale: en
of_concept: cardinality-of-power-set
source_book: gtm030
source_chapter: "Chapter I: Basic Concepts"
source_section: "1-4"
---

By definition, $P(S)$ contains all subsets of $S$. For each $i = 0, 1, \ldots, n$, the number of subsets of $S$ having exactly $i$ elements is the binomial coefficient $\binom{n}{i} = \frac{n(n-1)\cdots(n-i+1)}{i!}$. Summing over all possible sizes $i$ gives
$$|P(S)| = \binom{n}{0} + \binom{n}{1} + \binom{n}{2} + \cdots + \binom{n}{n}.$$
By the binomial theorem, $(1+1)^n = \sum_{i=0}^n \binom{n}{i} 1^{n-i} 1^i = \sum_{i=0}^n \binom{n}{i}$. Since $\binom{n}{0}=1$ (the empty set), we obtain $|P(S)| = 2^n$.
