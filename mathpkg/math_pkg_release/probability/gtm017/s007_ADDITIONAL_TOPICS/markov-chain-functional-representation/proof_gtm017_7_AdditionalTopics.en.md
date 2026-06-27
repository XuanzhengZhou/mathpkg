---
role: proof
locale: en
of_concept: markov-chain-functional-representation
source_book: gtm017
source_chapter: "7"
source_section: "Additional Topics"
---

Introduce a continuous-state Markov process $Y_n = X_n - U_n$ whose instantaneous density is $p(y) = p_j$ for $j-1 \leq y < j$. Then $X_n = [Y_n] + 1$. Define the conditional distribution function $F(y \mid y')$ of $Y_n$ given $Y_{n-1}=y'$:
$$F(y \mid y') = \sum_{k=1}^{j-1} p_{i,k} + p_{i,j}(y - j + 1)$$
for $i-1 \leq y' < i$ and $j-1 \leq y < j$. Set $\xi_n = F(Y_n \mid Y_{n-1})$.

The random variable $\xi_n$ is uniformly distributed on $[0,1]$ and independent of $Y_{n-1}$ (by Problem IV.5). By the Markov property, $\xi_n$ is independent of all preceding $Y_{n-2}, Y_{n-3}, \ldots$, so the $\xi_n$ are i.i.d. Uniform$[0,1]$.

Let $\delta = \min_i p_{i,1} > 0$. Define inverse mappings recursively: $G_1(z,y) = F^{-1}(z \mid y)$, $G_2(z_1,z_2,y) = F^{-1}(z_1 \mid G_1(z_2,y))$, and generally $G_k(z_1,\ldots,z_k,y) = F^{-1}(z_1 \mid G_{k-1}(z_2,\ldots,z_k,y))$.

Consider events $A_{n-2k}$ with equal positive probability. Since $\sum P(A_{n-2k})$ diverges, by the zero-one law almost every realization falls into some $A_{n-2k}$. Let $j$ be the smallest such index. Then with probability one,
$$Y_n = G_{3j}(\xi_n, \ldots, \xi_{n-2j+1}, \xi_{n-2j}/p_{1,1}).$$
Since $X_n = [Y_n] + 1$, we obtain $X_n = f(\xi_n, \xi_{n-1}, \ldots)$.
