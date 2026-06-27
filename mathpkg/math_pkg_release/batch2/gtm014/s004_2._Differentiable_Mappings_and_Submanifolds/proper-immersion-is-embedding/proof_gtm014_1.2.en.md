---
role: proof
locale: en
of_concept: proper-immersion-is-embedding
source_book: gtm014
source_chapter: "I"
source_section: "2"
---

Using Corollary 2.11 (2) we see that $\phi(X)$ is a submanifold if and only if $\phi: X \to \phi(X)$ is a homeomorphism where $\phi(X)$ is given the topology induced from $Y$. Clearly $\phi: X \to \phi(X)$ is continuous and bijective, so we need only show that $\phi^{-1}$ is continuous.

Let $y_1, y_2, \ldots$ be a sequence in $\phi(X)$ converging to $y$ in $\phi(X)$. Let $x_i = \phi^{-1}(y_i)$ and $x = \phi^{-1}(y)$. We need to show $x_i \to x$ in $X$.

Consider the set $K = \{y, y_1, y_2, \ldots\}$. Since $y_i \to y$, $K$ is compact in $\phi(X)$ and hence compact in $Y$. By properness of $\phi$, the preimage $\phi^{-1}(K)$ is compact in $X$. Now $\{x_i\}$ is a sequence in the compact set $\phi^{-1}(K)$, so it has a convergent subsequence.

Let $x_{i_j} \to x'$ be a convergent subsequence. By continuity of $\phi$, $\phi(x_{i_j}) = y_{i_j} \to \phi(x')$. But $y_{i_j} \to y = \phi(x)$. By uniqueness of limits, $\phi(x') = \phi(x)$, and since $\phi$ is 1-1, $x' = x$.

Thus every convergent subsequence of $\{x_i\}$ converges to $x$. Since $\{x_i\}$ lies in a compact set, this implies $x_i \to x$. Therefore $\phi^{-1}$ is continuous, and $\phi(X)$ is a submanifold of $Y$.
