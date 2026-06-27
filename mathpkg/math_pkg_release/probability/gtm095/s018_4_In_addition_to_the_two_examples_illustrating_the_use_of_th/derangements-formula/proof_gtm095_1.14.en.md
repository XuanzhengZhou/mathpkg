---
role: proof
locale: en
of_concept: derangements-formula
source_book: gtm095
source_chapter: "1"
source_section: "14. Inclusion–Exclusion Principle"
---

# Proof of Number of Derangements

Let $\Omega$ consist of $n!$ permutations of $(1, 2, \ldots, n)$:

$$\begin{pmatrix} 1 & 2 & \cdots & n \\ a_1 & a_2 & \cdots & a_n \end{pmatrix}.$$

A derangement is a permutation with no fixed points, i.e., $a_i \neq i$ for all $i$. Let $D_n$ denote the number of derangements of $n$ elements (with $D_0 = 1$).

Let $A_i$ be the event that $a_i = i$ (the $i$-th element is a fixed point). We seek

$$D_n = N(\overline{A}_1 \cap \overline{A}_2 \cap \cdots \cap \overline{A}_n),$$

where $N(\cdot)$ counts the number of permutations in the corresponding event.

Clearly,

$$N(A_i) = (n-1)!$$

since fixing one position leaves $(n-1)!$ ways to arrange the remaining elements. Similarly, for $i \neq j$,

$$N(A_i A_j) = (n-2)!,$$

and in general, for any $k$-tuple of distinct indices,

$$N(A_{i_1} A_{i_2} \cdots A_{i_k}) = (n-k)!.$$

By the inclusion–exclusion principle,

$$D_n = N(\Omega) - S_1 + S_2 - \cdots + (-1)^m S_m + \cdots + (-1)^n S_n,$$

where

$$S_m = \sum_{1 \leq i_1 < i_2 < \cdots < i_m \leq n} N(A_{i_1} A_{i_2} \cdots A_{i_m}).$$

The number of terms in $S_m$ is $\binom{n}{m}$, and each term equals $(n-m)!$. Hence

$$S_m = \binom{n}{m} (n-m)!.$$

Substituting into the inclusion–exclusion expansion:

$$D_n = \sum_{m=0}^{n} (-1)^m \binom{n}{m} (n-m)!.$$

Since $\binom{n}{m} (n-m)! = \frac{n!}{m!}$, we obtain

$$D_n = n! \sum_{m=0}^{n} \frac{(-1)^m}{m!}.$$

Thus the probability of a complete derangement is

$$P(\overline{A}_1 \cdots \overline{A}_n) = \frac{D_n}{n!} = \sum_{m=0}^{n} \frac{(-1)^m}{m!} = 1 - 1 + \frac{1}{2!} - \frac{1}{3!} + \cdots + \frac{(-1)^n}{n!}.$$

Since $\sum_{m=0}^{\infty} \frac{(-1)^m}{m!} = \frac{1}{e}$, we have the asymptotic estimate

$$D_n \sim \frac{n!}{e} \qquad (n \to \infty).$$

More precisely,

$$P(\overline{A}_1 \cdots \overline{A}_n) = \frac{1}{e} + O\left(\frac{1}{(n+1)!}\right).$$

$\square$
