---
role: proof
locale: en
of_concept: characterization-of-complemented-modular-lattice
source_book: gtm030
source_chapter: "7"
source_section: "7"
---

**Forward direction:** Assume $L$ is a complemented modular lattice satisfying both chain conditions. If $1 = 0$, the statement is trivial. Otherwise, there exists a point $p_1$ (a minimal non-zero element). Since $L$ is complemented, $p_1$ has a complement $p_1'$. If $p_1' \neq 0$, $p_1'$ contains a point $p_2$ with $p_1 \cap p_2 = 0$ and $p_1 \cup p_2 > p_1$. Then $p_1 \cup p_2$ has a complement; if nonzero, it contains a point $p_3$ with $(p_1 \cup p_2) \cap p_3 = 0$ and $p_1 \cup p_2 \cup p_3 > p_1 \cup p_2$. Continuing, we obtain a strictly ascending chain $p_1 < p_1 \cup p_2 < p_1 \cup p_2 \cup p_3 < \cdots$. By the ascending chain condition, this terminates after $n < \infty$ steps, meaning $p_1 \cup \cdots \cup p_n$ has $0$ as complement, so $1 = p_1 \cup \cdots \cup p_n$. The construction ensures $(p_1 \cup \cdots \cup p_i) \cap p_{i+1} = 0$ for all $i$, so the $p_i$ are independent.

**Converse direction:** Suppose $L$ is a modular lattice with $0$ and $1$, and $1 = p_1 \cup \cdots \cup p_n$ where the $p_i$ are points. Let $\{p_1, \ldots, p_m\}$ be a maximal independent subset. Since $L$ is modular and $1$ is the join of finitely many points, $L$ satisfies both chain conditions. To prove $L$ is complemented, let $a \in L$, $a \neq 1$. Choose $p_{i_1} \nleq a$; then $a \cap p_{i_1} = 0$ and $a_1 = a \cup p_{i_1} > a$. If $a_1 \neq 1$, choose $p_{i_2}$ such that $a_1 \cap p_{i_2} = 0$. This process yields $p_{i_1}, \ldots, p_{i_r}$ such that $a \cap p_{i_1} = 0$, $(a \cup p_{i_1}) \cap p_{i_2} = 0$, $\ldots$, $(a \cup p_{i_1} \cup \cdots \cup p_{i_{r-1}}) \cap p_{i_r} = 0$, and $a \cup p_{i_1} \cup \cdots \cup p_{i_r} = 1$. By independence, $a \cap (p_{i_1} \cup \cdots \cup p_{i_r}) = 0$, so $p_{i_1} \cup \cdots \cup p_{i_r}$ is a complement of $a$.
