---
role: proof
locale: en
of_concept: bounded-nonzero-regular-function-absorbing-chain
source_book: gtm040
source_chapter: "8"
source_section: "4"
---

**Proof 1:** Suppose $Ph = h$ with $|h| \leq c\mathbf{1}$. Since $h_i = \sum_j P_{ij} h_j$, we have $|h_i| \leq \sum_j P_{ij} |h_j|$ or $|h| \leq P|h|$. Therefore, $|h| \leq P^n|h| \leq P^n(c\mathbf{1})$. But $P^n\mathbf{1}$ is the probability that the process continues at least until time $n$, which tends to zero as $n$ tends to infinity because $\bar{P}$ is absorbing. Hence $h = 0$.

**Proof 2:** Let $a$ be any state and set $h'_i = M_a[|h(x_n(\omega))|]$, where $M_a$ denotes expectation starting from state $a$. Then $h'(x_n(\omega))$ in the $\bar{P}$-process forms a bounded martingale. By the martingale convergence theorem (or equivalently, by Corollary 3-16 to the second martingale systems theorem),

$$0 = h'_a = M[h'(x_\infty(\omega))] = M[h'(x_0(\omega))].$$

But $x_0(\omega)$ is arbitrary, so that $h' = 0$ and consequently $h = 0$.
