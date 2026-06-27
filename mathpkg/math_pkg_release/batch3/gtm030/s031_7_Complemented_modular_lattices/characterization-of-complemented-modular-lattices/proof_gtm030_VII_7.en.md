---
role: proof
locale: en
of_concept: characterization-of-complemented-modular-lattices
source_book: gtm030
source_chapter: "VII"
source_section: "7. Complemented modular lattices"
---

**($\Rightarrow$)** Let $L$ be a complemented modular lattice satisfying both chain conditions. Since $L$ has $0$ and $1$, $L$ is not empty. If $1 = 0$, then $1$ is trivially a l.u.b. of independent points. Assume $1 \neq 0$. Then $L$ contains points (atoms). Choose a point $p_1 \in L$. Since $L$ is complemented, there exists $p_1'$ such that $p_1 \cup p_1' = 1$, $p_1 \cap p_1' = 0$. If $p_1' \neq 0$, then $p_1'$ contains a point $p_2 \leq p_1'$. Since $p_1 \cap p_2 = 0$, we have $p_1 \cup p_2 > p_1$. Also $p_1 \cup p_2$ has a complement which, if nonzero, contains a point $p_3$. Then $(p_1 \cup p_2) \cap p_3 = 0$ and $p_1 \cup p_2 \cup p_3 > p_1 \cup p_2$. Continuing in this way we obtain a sequence of points $p_1, p_2, p_3, \ldots$ such that
$$p_1 < p_1 \cup p_2 < p_1 \cup p_2 \cup p_3 < \cdots.$$
By the ascending chain condition this breaks off after, say, $n < \infty$ steps. When this occurs, we know that $p_1 \cup p_2 \cup \cdots \cup p_n$ has $0$ as a complement. This means $1 = p_1 \cup p_2 \cup \cdots \cup p_n$. Thus $1$ is a l.u.b. of a finite number of points. Also we have chosen the $p_i$ so that
$$(p_1 \cup p_2 \cup \cdots \cup p_i) \cap p_{i+1} = 0, \quad i = 1, 2, \ldots, n-1.$$
Hence, if $L$ is modular, the $p_i$ are independent.

**($\Leftarrow$)** Conversely, suppose $L$ is any modular lattice with $0$ and $1$ that has the property that $1$ is a l.u.b. of a finite number of points. We show $L$ satisfies the chain conditions and is complemented. Let $1 = p_1 \cup p_2 \cup \cdots \cup p_n$ where the $p_i$ are points. Choose notation so that $p_1, \ldots, p_m$ is a maximal independent subset of $\{p_1, \ldots, p_n\}$.

We prove next that $L$ is complemented. Let $1 = p_1 \cup p_2 \cup \cdots \cup p_n$ where the $p_i$ are points. If $a$ is any element of $L$ and $a \neq 1$, we can choose a $p_{i_1} \not\leq a$. Then $a \cap p_{i_1} = 0$ and $a_1 = a \cup p_{i_1} > a$. If $a_1 \neq 1$, we can find a $p_{i_2}$ such that $a_1 \cap p_{i_2} = 0$. This process leads to a subset $p_{i_1}, p_{i_2}, \ldots, p_{i_r}$ of the $p_j$ such that
$$a \cap p_{i_1} = 0,$$
$$(a \cup p_{i_1}) \cap p_{i_2} = 0, \quad \ldots, \quad (a \cup p_{i_1} \cup \cdots \cup p_{i_{r-1}}) \cap p_{i_r} = 0,$$
$$a \cup p_{i_1} \cup \cdots \cup p_{i_r} = 1.$$
The first set of equations shows that the set $\{a, p_{i_1}, \ldots, p_{i_r}\}$ is independent. Hence $a \cap (p_{i_1} \cup \cdots \cup p_{i_r}) = 0$ so that by the last equation above, $p_{i_1} \cup \cdots \cup p_{i_r}$ is a complement of $a$. Thus $L$ is complemented.
