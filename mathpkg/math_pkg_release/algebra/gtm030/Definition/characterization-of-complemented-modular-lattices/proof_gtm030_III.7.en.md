---
role: proof
locale: en
of_concept: characterization-of-complemented-modular-lattices
source_book: gtm030
source_chapter: "III"
source_section: "7"
---

**Forward direction:** Let $L$ be a complemented modular lattice satisfying both chain conditions. Pick a point $p_1$ (if $1 = 0$ the result is trivial). Let $p_1'$ be a complement of $p_1$. If $p_1' \neq 0$, it contains a point $p_2 \leq p_1'$. Since $p_1 \cap p_2 = 0$, we have $p_1 \cup p_2 > p_1$. The element $p_1 \cup p_2$ has a complement which, if non-zero, contains a point $p_3$ with $(p_1 \cup p_2) \cap p_3 = 0$ and $p_1 \cup p_2 \cup p_3 > p_1 \cup p_2$. Continuing in this way yields a strictly ascending chain
$$p_1 < p_1 \cup p_2 < p_1 \cup p_2 \cup p_3 < \cdots$$
By the ascending chain condition this breaks off after $n < \infty$ steps, at which point $p_1 \cup \cdots \cup p_n$ has $0$ as complement, so $1 = p_1 \cup \cdots \cup p_n$. Thus $1$ is a l.u.b. of finitely many points. Moreover,
$$(p_1 \cup \cdots \cup p_i) \cap p_{i+1} = 0 \quad (i = 1, \ldots, n-1),$$
so by modularity the $p_i$ are independent.

**Converse:** Suppose $L$ is a modular lattice with $0$ and $1$ such that $1 = p_1 \cup \cdots \cup p_n$ where the $p_i$ are points. We may assume $\{p_1, \ldots, p_m\}$ is a maximal independent subset.

To prove $L$ is complemented, let $a \in L$, $a \neq 1$. Choose $p_{i_1} \not\leq a$; then $a \cap p_{i_1} = 0$ and $a_1 = a \cup p_{i_1} > a$. If $a_1 \neq 1$, find $p_{i_2}$ with $a_1 \cap p_{i_2} = 0$. Continue to obtain $p_{i_1}, \ldots, p_{i_r}$ such that
$$a \cap p_{i_1} = 0, \quad (a \cup p_{i_1}) \cap p_{i_2} = 0, \quad \ldots, \quad (a \cup p_{i_1} \cup \cdots \cup p_{i_{r-1}}) \cap p_{i_r} = 0,$$
$$a \cup p_{i_1} \cup \cdots \cup p_{i_r} = 1.$$
The first set of equations shows that $\{a, p_{i_1}, \ldots, p_{i_r}\}$ is independent, so $a \cap (p_{i_1} \cup \cdots \cup p_{i_r}) = 0$. Hence $p_{i_1} \cup \cdots \cup p_{i_r}$ is a complement of $a$. This proves $L$ is complemented. The chain conditions follow from the finiteness of the generating set of points.
