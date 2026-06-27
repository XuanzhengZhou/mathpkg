---
role: proof
locale: en
of_concept: sequentially-compact-implies-closed-and-bounded
source_book: gtm012
source_chapter: "1"
source_section: "6. Compactness"
---

# Proof of Proposition 6.3: Sequentially Compact Sets are Closed and Bounded

Suppose $(S, d)$ is a metric space, $S \neq \varnothing$, and suppose $A \subset S$ is sequentially compact.

**Closed.** Suppose $x$ is a limit point of $A$. Choose $x_n \in B_{1/n}(x) \cap A$, $n = 1, 2, 3, \ldots$. Any subsequence of $(x_n)_{n=1}^{\infty}$ converges to $x$, since $x_n \to x$. Since $A$ is sequentially compact, some subsequence converges to a point of $A$. But the limit of this subsequence must be $x$ (since the whole sequence converges to $x$). Thus $x \in A$, and $A$ is closed.

**Bounded.** Suppose $A$ were not bounded. Take $x \in S$ and choose $x_1 \in A$ such that $x \notin B_1(x)$. Let $r_1 = d(x, x_1) + 1$. By the triangle inequality, $B_1(x_1) \subset B_{r_1}(x)$. Since $A$ is not bounded, there is $x_2 \in A$ such that $x_2 \notin B_{r_1}(x)$. Thus also $d(x_1, x_2) \geq 1$. Let $r_2 = \max\{d(x, x_1), d(x, x_2)\} + 1$. Continuing inductively, we obtain a sequence $(x_n)_{n=1}^{\infty}$ in $A$ with $d(x_i, x_j) \geq 1$ for all $i \neq j$. Such a sequence has no convergent subsequence (any convergent subsequence would be Cauchy, which contradicts $d(x_i, x_j) \geq 1$ for $i \neq j$). This contradicts the sequential compactness of $A$. Hence $A$ is bounded. $\square$
