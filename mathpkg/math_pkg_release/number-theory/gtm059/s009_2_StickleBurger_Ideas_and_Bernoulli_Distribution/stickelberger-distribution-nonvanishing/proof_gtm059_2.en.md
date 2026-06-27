---
role: proof
locale: en
of_concept: stickelberger-distribution-nonvanishing
source_book: gtm059
source_chapter: "2"
source_section: "2. Stickelberger Ideals and Bernoulli Distributions"
---

The proof proceeds by induction on the number of prime factors of the level $N$. For $N = p$ (prime case), one shows directly that the Bernoulli distribution generates the full space of odd distributions. The key computation uses the fact that the Bernoulli polynomials $B_k(X)$ have leading term $X^k$, which guarantees that the Stickelberger sums are non-zero for characters of exact conductor $p$.

For composite $N = p_1^{e_1} \cdots p_r^{e_r}$, one uses the partial fraction decomposition and the Chinese Remainder Theorem. An induction argument on the number of prime factors shows that the Stickelberger distribution at level $N$ has rank equal to the sum of the ranks at the prime power components, which is the maximal possible.

The inductive step uses the distribution relation to relate the values at level $N$ to values at levels $N/p_i$, and a careful analysis of the kernel of the restriction map shows that no new relations appear beyond those defining the universal distribution. The nonvanishing of the Stickelberger sums for primitive characters follows from the fact that $B_k(X)$ is not a polynomial in $X^p$ for any prime $p$ when $k \geq 1$.
