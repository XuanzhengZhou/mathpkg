---
role: proof
locale: en
of_concept: chinese-remainder-theorem
source_book: gtm077
source_chapter: "I"
source_section: "4"
---
# Proof of the Chinese Remainder Theorem for Simultaneous Congruences

**Theorem.** Let $n_1, n_2, \ldots, n_k$ be pairwise relatively prime positive integers, and let $a_1, a_2, \ldots, a_k$ be arbitrary integers. Then the system of congruences
$$x \equiv a_1 \pmod{n_1}, \quad x \equiv a_2 \pmod{n_2}, \quad \ldots, \quad x \equiv a_k \pmod{n_k}$$
has a unique solution modulo $n_1 n_2 \cdots n_k$.

*Proof.* **Uniqueness.** Suppose $x$ and $y$ are two solutions of the system. Then $x - y \equiv 0 \pmod{n_i}$ for each $i = 1, \ldots, k$, so each $n_i$ divides $x - y$. Since the $n_i$ are pairwise coprime, their product $N = n_1 n_2 \cdots n_k$ also divides $x - y$. Hence $x \equiv y \pmod{N}$, establishing uniqueness modulo $N$.

**Existence.** Set $N = n_1 n_2 \cdots n_k$. For each $i$, define
$$N_i = \frac{N}{n_i} = n_1 \cdots n_{i-1} \, n_{i+1} \cdots n_k.$$
Since the $n_j$ are pairwise coprime, $(N_i, n_i) = 1$. By Theorem 14 (the coprime case of linear congruences), there exists a unique $M_i$ modulo $n_i$ such that
$$N_i M_i \equiv 1 \pmod{n_i}.$$
Set
$$x = \sum_{i=1}^{k} a_i N_i M_i.$$
For any fixed $j$, consider $x$ modulo $n_j$. For $i \neq j$, $N_i$ contains the factor $n_j$, so $a_i N_i M_i \equiv 0 \pmod{n_j}$. For $i = j$, we have $a_j N_j M_j \equiv a_j \cdot 1 \equiv a_j \pmod{n_j}$. Hence
$$x \equiv a_j \pmod{n_j}$$
for each $j = 1, \ldots, k$. Thus $x$ is a solution of the system.

The general solution is $x + N t$ for any integer $t$, and the solution is uniquely determined modulo $N$. $\square$

**Remark.** This result also follows from an induction on $k$ using Theorem 14. For $k = 1$ the statement is trivial. Suppose a solution exists modulo $n_1 \cdots n_{k-1}$ and set $x = x_0 + n_1 \cdots n_{k-1} \cdot t$. Substituting into the $k$-th congruence
$$x_0 + n_1 \cdots n_{k-1} \cdot t \equiv a_k \pmod{n_k}$$
yields a linear congruence in $t$ with coefficient $n_1 \cdots n_{k-1}$, which is coprime to $n_k$. By Theorem 14, this has a unique solution $t_0$ modulo $n_k$, completing the induction step.
