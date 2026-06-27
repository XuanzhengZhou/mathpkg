---
role: proof
locale: en
of_concept: completeness-of-hausdorff-metric
source_book: gtm036
source_chapter: "1"
source_section: "D"
---

Suppose that $\{A_n : n = 1, 2, \dots\}$ is a Cauchy sequence in $\mathcal{E}$. Let $A$ be the set of limits of all Cauchy sequences $\{x_n\}$ in $E$ with $x_n \in A_n$ for each $n$. One must show that $d(A, A_n) \to 0$ as $n \to \infty$.

Let $\varepsilon > 0$ be given. Since $\{A_n\}$ is Cauchy in $\mathcal{E}$, there exists $N$ such that for all $m, n \geq N$, we have $d(A_n, A_m) < \varepsilon/2$. 

Fix $n \geq N$. For any $a \in A$, by definition there exists a Cauchy sequence $\{x_k\}$ with $x_k \in A_k$ converging to $a$. Choose $k \geq N$ large enough so that $d(x_k, a) < \varepsilon/2$. Then
$$d(a, A_n) \leq d(a, x_k) + d(x_k, A_n) \leq d(a, x_k) + d(A_k, A_n) < \varepsilon/2 + \varepsilon/2 = \varepsilon.$$
Since $a \in A$ was arbitrary, $\sup_{a \in A} d(a, A_n) \leq \varepsilon$.

Conversely, for any $y \in A_n$ with $n \geq N$, choose a subsequence $\{n_k\}$ such that $n_1 = n$. Since $\{A_m\}$ is Cauchy, we can inductively select points $y_k \in A_{n_k}$ with $d(y_k, y_{k+1}) < \varepsilon/2^k$. The sequence $\{y_k\}$ is Cauchy in $E$, hence converges to some $y_0 \in A$. Moreover, $d(y, y_0) \leq \sum_{k=1}^\infty d(y_k, y_{k+1}) < \varepsilon$. Thus $\sup_{y \in A_n} d(y, A) \leq \varepsilon$.

Therefore $d(A, A_n) \leq \varepsilon$ for all $n \geq N$, proving $d(A, A_n) \to 0$. It remains to show that $A$ is closed and non-void. Non-voidness follows from selecting one point from each $A_n$ and taking a Cauchy subsequence. Closedness follows from the fact that limits of sequences in $A$ can be approximated by diagonal sequences from the $A_n$'s.
