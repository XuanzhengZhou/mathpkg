---
role: proof
locale: en
of_concept: complete-quotient-theorem
source_book: gtm015
source_chapter: "9"
source_section: "Completeness of quotient groups"
---

# Proof of Quotient of a metrizable complete group by a closed normal subgroup is complete

Let $G$ be a metrizable complete topological group and let $N$ be a closed normal subgroup of $G$.

**Part 1: $N$ is complete.** Let $d$ be a left-invariant compatible metric on $G$ (6.3). Since $(G, d)$ is a complete metric space (7.8) and $N$ is a closed subset, $(N, d|_N)$ is a complete metric space. But $d|_N$ is a left-invariant metric compatible with the relative topology on $N$ (2.2), therefore $N$ is a complete topological group (7.8).

**Part 2: $G/N$ is complete and metrizable.** Let $\pi: G \to G/N$ be the canonical mapping. Define a value on $G$ by $|x| = d(e, x)$ (8.3). For $u \in G/N$, define

$$|u| = \inf \{|x| : x \in u\}.$$

By (8.13), $u \mapsto |u|$ is a value on $G/N$ whose left value topology coincides with the quotient topology. The corresponding left-invariant metric is $D(u, v) = |u^{-1}v|$ (8.3). Thus $G/N$ is metrizable.

To show $(G/N, D)$ is complete, let $(u_n)$ be a $D$-Cauchy sequence in $G/N$. Pass to a subsequence such that $D(u_n, u_{n+1}) < 2^{-n}$ for all $n$. By definition of $|u|$ as an infimum, choose $x_n \in G$ such that

(1) $\pi(x_n) = u_n$,
(2) $|x_n| < |u_n^{-1}u_{n+1}| + 2^{-(n+1)}$ for $n \geq 1$,
and $|x_1| < 2^{-1}$.

Set $y_n = x_1 x_2 \cdots x_n$ (a "partial product"). Then $y_1 = x_1$ and $y_{n+1} = y_n x_{n+1}$. Since $\pi(x_1) = u_1$ and $\pi(x_n) = u_{n-1}^{-1}u_n$ for $n > 1$, a telescoping product gives

(3) $\pi(y_n) = u_n \quad (n = 1, 2, 3, \ldots).$

The sequence $(y_n)$ is $d$-Cauchy. Indeed,
$$d(y_n, y_{n+1}) = |y_n^{-1}y_{n+1}| = |x_{n+1}| < |u_n^{-1}u_{n+1}| + 2^{-(n+1)} < 2^{-n} + 2^{-(n+1)} < 2^{-n+1},$$
and
$$d(y_n, y_{n+p}) \leq \sum_{k=n}^{n+p-1} d(y_k, y_{k+1}) < \sum_{k=n}^{n+p-1} 2^{-k+1} < 2^{-n+2} \to 0$$
as $n \to \infty$, uniformly in $p$. Since $(G, d)$ is complete, there exists $y \in G$ with $d(y_n, y) \to 0$. Setting $u = \pi(y)$, continuity of $\pi$ yields $u_n = \pi(y_n) \to \pi(y) = u$.

Thus every $D$-Cauchy sequence converges, so $(G/N, D)$ is a complete metric space. Since $D$ is a left-invariant compatible metric, $G/N$ is a complete topological group (7.8).

For the general case where $G$ is metrizable complete but not necessarily metric-complete (7.5), one uses the value structure (8.8) to reduce to the metric case treated above.
