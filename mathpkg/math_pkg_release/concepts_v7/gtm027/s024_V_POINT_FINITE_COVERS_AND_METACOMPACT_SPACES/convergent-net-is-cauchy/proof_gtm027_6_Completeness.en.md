---
role: proof
locale: en
of_concept: convergent-net-is-cauchy
source_book: gtm027
source_chapter: "6"
source_section: "Completeness"
---

# Proof that Convergent Nets are Cauchy Nets (Theorem 6.21)

**Theorem 6.21.** Each net which converges to a point relative to the uniform topology is a Cauchy net. A Cauchy net converges to each of its cluster points.

**Proof.** Let $\{S_n : n \in D\}$ be a net in $(X, \mathcal{U})$ converging to $x$. Let $U \in \mathcal{U}$ be given. Choose a symmetric $V \in \mathcal{U}$ such that $V \circ V \subset U$. Since $S_n \to x$, the net is eventually in $V[x]$, i.e., there exists $n_0 \in D$ such that $(x, S_n) \in V$ for all $n \geq n_0$. Then for any $m, n \geq n_0$, we have $(S_m, x) \in V$ (by symmetry) and $(x, S_n) \in V$, so $(S_m, S_n) \in V \circ V \subset U$. Thus $\{(S_m, S_n)\} \to \Delta$ in the product uniformity, meaning the net is Cauchy.

For the second statement: suppose $\{S_n\}$ is a Cauchy net and $x$ is a cluster point. Let $U \in \mathcal{U}$ and choose symmetric $V$ with $V \circ V \subset U$. Since the net is Cauchy, there exists $n_0$ such that $(S_m, S_n) \in V$ for all $m, n \geq n_0$. Since $x$ is a cluster point, there exists $n \geq n_0$ with $S_n \in V[x]$, i.e., $(x, S_n) \in V$. Then for any $m \geq n_0$, $(x, S_m) \in V \circ V \subset U$ (since $(x, S_n) \in V$ and $(S_n, S_m) \in V$). Hence the net converges to $x$.
