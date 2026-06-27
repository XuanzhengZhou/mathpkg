---
role: proof
locale: en
of_concept: cofinal-sequence-in-countable-ordered-set
source_book: gtm043
source_chapter: "13"
source_section: "13.6"
---
Let $(x_n)_{n \in \mathbb{N}}$ enumerate $E$. Define
$$S = \{x_n : x_k < x_n \text{ for all } k < n\}.$$
The elements of $S$ form an increasing sequence.

For cofinality: given $x \in E$, let $x_n$ be the element with smallest index $n$ such that $x \leq x_n$. Then for all $k < n$, $x_k < x \leq x_n$, so $x_n \in S$ and $x \leq x_n$. Thus $S$ is cofinal.

The coinitial case follows by reversing the order of $E$.