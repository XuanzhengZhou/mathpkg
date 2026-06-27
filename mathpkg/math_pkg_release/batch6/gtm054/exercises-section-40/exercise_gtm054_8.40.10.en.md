---
role: exercise
locale: en
chapter: "8"
section: "40"
exercise_number: 10
---

Prove Theorem B9.

We shall presently see that no restrictions such as in Theorem B9 can be put on the design-types of one-sided designs

nondegenerate cases differ only in the initial stages. In order to construct a nondegenerate design, let $E_0$ denote a $(v_{t_p})$-set and let $f_0: E_0 \rightarrow \mathcal{P}_{t_p}(V)$ be a bijection. In order to construct a degenerate design in the case $t_p = v - 1$, let $E_0$ denote a $v$-set and let $f_0(e) = V$ for all $e \in E_0$. In order to construct a degenerate design when $t_p < v - 1$, let $E_0$ denote a $(v_{t_p}) - (v_{t_p} + 2)$-set and let $f_0: E_0 \rightarrow (\mathcal{P}_{t_p}(V) + \mathcal{P}_{t_p}(V')) \cup \{V, V'\}$ be a bijection where $V'$ is a $(v - 1)$-subset of $V$.

In all cases, let $\Lambda_0 = (V, f_0, E_0)$. We observe that $\Lambda_0$ is a $(t_p);)$-design but is not a $(t);)$-design for $t_p < t < v$. (We emphasize that this property will be unaffected by the adjoining to $E_0$ of blocks of size less than $t_p$.) This has been the initial step, $j = 0$, for a proof by induction. Now let $0 \leq j \leq t_p - 1$, and let the following be our induction hypothesis: There exists a system $\Lambda_j = (V, f_j, E_j)$ such that for all $t \geq t_p - j$, $\Lambda_j$ is a $(t);)$-design if and only if $t \in \{t_1, \ldots, t_p\}$. We shall adjoin blocks to $E_j$ and extend $f_j$ appropriately in order to form a design $\Lambda_{j+1}$ which satisfies the condition of the induction hypothesis for all $t \geq t_p - (j + 1)$.

Case 1: $t_p - (j + 1) \in \{

We may thus assume that $\Lambda$ is a $(; a)$-design with $a \geq 2$. By B6, $v \geq b$. But $v \leq |E_0| \leq b$, with $|E_0| = b$ only if $t_i = i$ for all $i = 1, \ldots, p$, while $v = |E_0|$ only if $t_p = v - 1$. But if both equalities hold simultaneously, then $b \geq 2v$ by our construction, giving a contradiction. Hence $\Lambda$ has design-type $(t_1, \ldots, t_p);$.

The degenerate design constructed in the above theorem has the property that $\bar{s}(V) > 0$. Due to Corollary B2, however, it generally will not have the property that $\bar{s}^*(E) > 0$.

A careful reading of the above proof also reveals that the design $\Lambda$ constructed therein will be a set system when the design is nondegenerate and the integers $t_1, \ldots, t_p$ are consecutive. Otherwise $\Lambda$ will in general not be a set system. Actually, set systems of type $(t_1, \ldots, t_p;)$ are also constructible under a slightly more general hypothesis than this.
