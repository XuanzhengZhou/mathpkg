---
role: proof
locale: en
of_concept: simultaneous-congruences
source_book: gtm077
source_chapter: "I"
source_section: "4"
---
# Proof: Simultaneous Linear Congruences

**Theorem.** Consider the system of simultaneous congruences
$$x \equiv a_1 \pmod{n_1},\quad x \equiv a_2 \pmod{n_2},\quad \ldots,\quad x \equiv a_k \pmod{n_k}.$$

If a solution exists, any two solutions differ by a multiple of the least common multiple $v = \operatorname{lcm}(n_1, \ldots, n_k)$; i.e., the solution is unique modulo $v$. In the special case where the $n_i$ are pairwise coprime (so $v = n_1 n_2 \cdots n_k$), a solution always exists (Chinese Remainder Theorem).

*Proof.* **Uniqueness.** Suppose $x$ and $y$ are two integers satisfying the system. Then for each $i = 1, \ldots, k$,
$$x \equiv a_i \pmod{n_i} \quad \text{and} \quad y \equiv a_i \pmod{n_i},$$
so $x - y \equiv 0 \pmod{n_i}$. Thus each $n_i$ divides $x - y$. The set of all common multiples of $n_1, \ldots, n_k$ is precisely the set of multiples of $v = \operatorname{lcm}(n_1, \ldots, n_k)$. Hence $v \mid (x - y)$, i.e., $x \equiv y \pmod{v}$.

Conversely, if $x$ is a solution and $x \equiv y \pmod{v}$, then $y$ also satisfies each congruence (since each $n_i \mid v$). Therefore, if a solution exists, it is uniquely determined modulo $v$.

**Existence (pairwise coprime case).** Assume the $n_i$ are pairwise coprime, so $v = N = n_1 n_2 \cdots n_k$. For each $i$, set $N_i = N / n_i$. Since $(N_i, n_i) = 1$, Theorem 14 guarantees the existence of $M_i$ with $N_i M_i \equiv 1 \pmod{n_i}$. Define
$$x = \sum_{i=1}^{k} a_i N_i M_i.$$
For each $j$, all terms with $i \neq j$ are divisible by $n_j$ (since $N_i$ contains the factor $n_j$), while the $j$-th term reduces to $a_j N_j M_j \equiv a_j \pmod{n_j}$. Thus $x \equiv a_j \pmod{n_j}$ for all $j$, establishing existence. The proof can also be carried out by induction on $k$, solving the congruences one at a time using Theorem 14.

**General case.** When the $n_i$ are not necessarily pairwise coprime, the system (7) is solvable if and only if the pairwise compatibility conditions
$$a_i \equiv a_j \pmod{\gcd(n_i, n_j)}$$
hold for all $i, j$. In this case, the system can be reduced stepwise: solving the first congruence gives $x = a_1 + n_1 t$; substituting into the second yields a linear congruence in $t$ modulo $n_2 / \gcd(n_1, n_2)$, which is solvable precisely when the compatibility condition holds. $\square$
