---
role: proof
locale: en
of_concept: corollary-5-17
source_book: gtm040
source_chapter: "5"
source_section: "17"
---

**Proof:** It is the unique minimum non-negative solution by Proposition 5-16 and Proposition 5-11.

4. Finite drunkard's walk

The finite drunkard's walk is a Markov chain defined on the integers $\{0, 1, \ldots, n\}$ with states 0

We shall use the second martingale systems theorem (Theorem 3-15) to compute the entries of $B, H, N$, and $a$ for the case $r = 1$.

To compute the entries of the $B$ matrix when $r = 1$, we note that $B1 = 1$ by Proposition 5-14; therefore $B_{i0} = 1 - B_{in}$ for each transient state $i$. Since $\{x_n\}$ is a bounded martingale, Corollary 3-16 applies with the time taken as the time of absorption (which is a stopping time because $P$ is absorbing if and only if $a$ is finite a.e.). Then

$$i = 0B_{i0} + nB_{in}$$

so that

$$B_{in} = i/n$$

and

$$B_{i0} = 1 - i/n.$$

To find the entry $H_{ij}$ of the $H$-matrix, we make state $j$ absorbing and consider the resulting process. If $i \leq j$, the modified process is the drunkard's walk on the integers $\{0, \ldots, j\}$ with $j$ absorbing. Hence $H_{ij} = i/j$. If $i \geq j$, the modified process is the drunkard's walk on $\{j, \ldots, n\}$. Renumbering the states, we can consider the process as starting at $i - j$ and taking place on the states $\{0, \ldots, n - j\}$. Thus,

$$H_{ij} = 1 - \frac{i - j}{n - j} = \frac{n - i}{n - j}.$$

To get $\bar{H}_{ii}$, where $i$ is transient, we use the fact that $\bar{H} = PH$, so that

$$\bar{H}_{ii} = pH_{i+1,i} + qH_{i-1,i}$$

$$= 1 - \frac{n}{2i(n - i)} \text{ since } p = q = \frac{1}{2}.$$

The $N$-matrix is determined as a function of $\bar{H}$ and $H$

The case $r \neq 1$ proceeds in the same way. By the systems theorem

$$r^i = r^0 B_{i0} + r^n B_{in}.$$

From this equation one easily deduces that

$$B_{i0} = \frac{r^i - r^n}{1 - r^n}.$$

After first computing $H$ and $N$, we find

$$a_i = M_i[a] = \frac{1}{q - p} \left[ i - n \frac{1 - r^i}{1 - r^n} \right].$$

When $r > 1$, this process is sometimes known as "gambler's ruin" because of the following interpretation. A gambler walks into a gambling house with $i$ dollars in his pocket, and the house has $n - i$ dollars to bet against him. In a given game the gambler has probability $p$ of winning. Since the house fixes the odds, we have $p < \frac{1}{2}$ and therefore $r > 1$. If the game is played repeatedly, $x_k$ in the above Markov chain represents the gambler's cash after $k$ games, and $B_{i0}$ is the probability of his eventual ruin. Since $r > 1$,

$$B_{i0} = \frac{1 - r^{-(n-i)}}{1 - r^{-n}} > 1 - r^{-(n-i)}$$

is nearly 1 when $n - i$ (the house's capital) is large. Thus the gambler is nearly sure to be ruined, no matter how rich he is. However, $a_i$ is approximately $i/(q - p)$, which is very large if $i$ is substantial and $p$ is near to $\frac{1}{2}$. Thus the gambler is likely to have a long run for his money.

5. Infinite drunkard's walk

Extending the finite drunkard's walk to a process $P$ defined on all of the non-negative integers, we set

$$P_{0i} = \delta_{0i}$$

$$P_{i,i+1} = p \quad \text{for } 0 < i < \infty$$

with the infinite drunkard's walk the random variable $n_j$ to be the number of times the process is in state $j$ up to the first time it is in state $k$. Let $p$ be the statement that the process is not absorbed at state 0, and let $p_k$ be the statement that the process is not absorbed at state 0 at any time up to the time it reaches state $k$.
