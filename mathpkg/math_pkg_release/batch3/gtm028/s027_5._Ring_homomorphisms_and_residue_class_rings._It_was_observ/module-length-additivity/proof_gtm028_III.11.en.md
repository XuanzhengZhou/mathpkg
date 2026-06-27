---
role: proof
locale: en
of_concept: module-length-additivity
source_book: gtm028
source_chapter: "III"
source_section: "§11"
---

Let $N = N_0 > N_1 > \cdots > N_t = (0)$ be any normal series of $N$ without repetitions. Since by Theorem 4, §4 and its corollary every submodule of $M - N$ is of the form $L - N$, where $L$ is a submodule of $M$ containing $N$, it follows that any normal series of $M - N$ without repetitions has the form
$$M - N = L_0 - N > L_1 - N > \cdots > L_s - N = (0), \quad L_{j-1} > L_j.$$
We thus obtain for $M$ a normal series
$$M = L_0 > L_1 > \cdots > L_s > N_1 > \cdots > N_t = (0)$$
without repetitions and of length $s + t$. Hence if either $l(N)$ or $l(M - N)$ is infinite, then either $t$ or $s$ can be made arbitrarily large, hence $l(M) = \infty$. On the other hand if they are both finite, then we may assume the series to be composition series. It then follows that the combined series is a composition series of $M$, whence the theorem.

For the second formula, we use $(L + N) - N \cong L - (L \cap N)$ and the fact that $R$-isomorphic modules have the same length. If either $l(L)$ or $l(N)$ is infinite, so is $l(L + N)$, and the formula is trivial. If both are finite, then the right side has finite length, hence so does the left, hence so does $L + N$ by the first part. The formula follows from the first part.
