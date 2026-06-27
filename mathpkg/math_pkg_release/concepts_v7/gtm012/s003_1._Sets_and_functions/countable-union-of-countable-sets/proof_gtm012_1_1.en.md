---
role: proof
locale: en
of_concept: countable-union-of-countable-sets
source_book: gtm012
source_chapter: "1"
source_section: "1. Sets and functions"
---

# Proof of Countable Union of Countable Sets

**Proposition 1.3.** If $A_1, A_2, A_3, \ldots$ are finite or countable sets, then the sets

$$\bigcup_{j=1}^{n} A_j \quad \text{and} \quad \bigcup_{j=1}^{\infty} A_j$$

are finite or countable.

*Proof.* We prove only the second statement (the finite union case follows immediately by taking $A_j = \varnothing$ for $j > n$). If any of the $A_j$ are empty, we may exclude them and renumber without affecting the union. Thus we may assume each $A_j$ is nonempty.

For each $A_j$, since $A_j$ is finite or countable, there exists a surjective function $f_j: \mathbb{Z}_+ \to A_j$. Define a function

$$f: \mathbb{Z}_+ \to \bigcup_{j=1}^{\infty} A_j$$

by the following scheme:

$$\begin{aligned}
f(1) &= f_1(1), & f(3) &= f_1(2), & f(5) &= f_1(3), & \ldots \\
f(2) &= f_2(1), & f(6) &= f_2(2), & f(10) &= f_2(3), & \ldots \\
f(4) &= f_3(1), & f(12) &= f_3(2), & f(20) &= f_3(3), & \ldots
\end{aligned}$$

In general, for $j, k = 1, 2, 3, \ldots$,

$$f\big(2^{j}(2k-1)\big) = f_j(k).$$

The mapping $n \mapsto (j, k)$ determined by the formula $n = 2^j(2k-1)$ is a bijection from $\mathbb{Z}_+$ onto $\mathbb{Z}_+ \times \mathbb{Z}_+$, since every positive integer can be uniquely expressed as an odd number $(2k-1)$ multiplied by a power of $2$ $(2^j)$.

Now let $x \in \bigcup_{j=1}^{\infty} A_j$. Then $x \in A_j$ for some $j \in \mathbb{Z}_+$. Since $f_j$ is surjective, there exists $k \in \mathbb{Z}_+$ such that $f_j(k) = x$. Taking $n = 2^j(2k-1)$, we have

$$f(n) = f\big(2^j(2k-1)\big) = f_j(k) = x.$$

Thus $f$ is surjective. By Proposition 1.1 (which states that if there exists a surjection from $\mathbb{Z}_+$ onto a set, then that set is finite or countable), the union $\bigcup_{j=1}^{\infty} A_j$ is finite or countable. $\square$
