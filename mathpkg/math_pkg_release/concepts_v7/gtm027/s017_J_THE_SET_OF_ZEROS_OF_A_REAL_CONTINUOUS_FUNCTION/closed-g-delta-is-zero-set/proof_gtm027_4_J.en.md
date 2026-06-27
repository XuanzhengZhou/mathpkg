---
role: proof
locale: en
of_concept: closed-g-delta-is-zero-set
source_book: gtm027
source_chapter: "4"
source_section: "J"
---

# Proof of Theorem J(b): Every closed $G_\delta$ in a normal space is a zero set

**Theorem.** If $A$ is a closed $G_\delta$ set in a normal topological space $X$, then there exists a continuous real-valued function $f: X \to \mathbb{R}$ such that $A = f^{-1}[\{0\}]$.

**Proof.** Since $A$ is a $G_\delta$ set, there exists a countable family $\{U_n\}_{n=1}^{\infty}$ of open sets such that

$$A = \bigcap_{n=1}^{\infty} U_n.$$

Without loss of generality, we may assume the sequence is decreasing: replace $U_n$ by $V_n = \bigcap_{i=1}^{n} U_i$, each $V_n$ is still open, and $A = \bigcap_{n=1}^{\infty} V_n$ with $V_1 \supset V_2 \supset \cdots$.

For each $n$, $A$ is closed and $A \subset V_n$. Since $X$ is normal, by Urysohn's Lemma there exists a continuous function $f_n: X \to [0,1]$ such that

$$f_n(x) = 0 \quad \text{for all } x \in A, \qquad f_n(x) = 1 \quad \text{for all } x \notin V_n.$$

Now define $f: X \to \mathbb{R}$ by

$$f(x) = \sum_{n=1}^{\infty} 2^{-n} f_n(x).$$

Since $0 \leq f_n(x) \leq 1$ for all $x$, the $n$-th term is bounded by $2^{-n}$, and the series $\sum_{n=1}^{\infty} 2^{-n} = 1$ converges. By the Weierstrass $M$-test, the series converges uniformly on $X$. Each partial sum is continuous, so the uniform limit $f$ is continuous.

Now we verify that $A = f^{-1}[\{0\}]$:

* If $x \in A$, then $f_n(x) = 0$ for all $n$, so $f(x) = 0$. Hence $A \subset f^{-1}[\{0\}]$.

* If $x \notin A$, then since $A = \bigcap_{n=1}^{\infty} V_n$, there exists some $m$ such that $x \notin V_m$. Then $f_m(x) = 1$, and since all $f_n(x) \geq 0$,

$$f(x) = \sum_{n=1}^{\infty} 2^{-n} f_n(x) \geq 2^{-m} f_m(x) = 2^{-m} > 0.$$

Thus $f(x) \neq 0$, so $x \notin f^{-1}[\{0\}]$. Therefore $f^{-1}[\{0\}] \subset A$.

Combining both inclusions, $A = f^{-1}[\{0\}]$. $\square$
