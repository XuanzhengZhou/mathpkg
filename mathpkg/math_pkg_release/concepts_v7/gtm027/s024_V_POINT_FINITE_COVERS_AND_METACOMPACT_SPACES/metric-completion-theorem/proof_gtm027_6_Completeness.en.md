---
role: proof
locale: en
of_concept: metric-completion-theorem
source_book: gtm027
source_chapter: "6"
source_section: "Completeness"
---

# Proof of the Metric Completion Theorem (Theorem 6.27)

**Theorem 6.27.** Each metric (or pseudo-metric) space can be mapped by a one-to-one isometry onto a dense subset of a complete metric (respectively pseudo-metric) space.

**Proof.** It suffices to prove the theorem for a pseudo-metric space $(X,d)$, since the corresponding result for metric spaces then follows from Theorem 4.15 (identifying points at distance zero to obtain a metric space).

Let $X^*$ be the class of all Cauchy sequences in $X$. For members $S = \{S_n\}$ and $T = \{T_n\}$ of $X^*$, define

$$d^*(S,T) = \lim_{n \to \infty} d(S_n, T_n).$$

This limit exists because $\{d(S_n, T_n)\}$ is a Cauchy sequence of real numbers (by the triangle inequality: $|d(S_n, T_n) - d(S_m, T_m)| \leq d(S_n, S_m) + d(T_n, T_m) \to 0$). It is straightforward to verify that $d^*$ is a pseudo-metric for $X^*$.

Define $F : X \to X^*$ by letting $F(x)$ be the constant sequence $F(x)_n = x$ for all $n$. Clearly $F$ is an isometry because $d^*(F(x), F(y)) = \lim_n d(x,y) = d(x,y)$, and $F$ is one-to-one modulo identification of points at distance zero.

**$F[X]$ is dense in $X^*$:** If $S \in X^*$, then for any $\epsilon > 0$ there exists $N$ such that $d(S_n, S_m) < \epsilon$ for all $n,m \geq N$. Then $F(S_N)$ (the constant sequence at $S_N$) satisfies $d^*(S, F(S_N)) = \lim_n d(S_n, S_N) \leq \epsilon$ (actually $\leq \epsilon$ since for large $n$, $d(S_n, S_N) < \epsilon$). Thus $F[X]$ is dense.

**$X^*$ is complete:** First observe that it suffices to show each Cauchy sequence in $F[X]$ converges in $X^*$ (since $F[X]$ is dense). A Cauchy sequence in $F[X]$ has the form $\{F(S_n) : n \in \omega\}$ where $S = \{S_n\}$ is a Cauchy sequence in $X$. Then $F(S_n)$ converges to $S$ in $X^*$ because

$$d^*(F(S_n), S) = \lim_{m \to \infty} d(S_n, S_m) \to 0 \quad \text{as } n \to \infty$$

since $S$ is a Cauchy sequence. Thus each Cauchy sequence in $F[X]$ converges in $X^*$, and by density, $X^*$ is complete.

For metric spaces: if $d$ is a metric (not just pseudo-metric), then $d^*$ is a pseudo-metric. By Theorem 4.15, the quotient of $X^*$ by the equivalence relation $d^*(S,T) = 0$ is a complete metric space, and the composition of $F$ with this quotient map yields the metric completion.
