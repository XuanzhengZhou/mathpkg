---
role: proof
locale: en
of_concept: linear-congruence-general-case
source_book: gtm077
source_chapter: "I"
source_section: "4"
---
# Proof: General Solution of a Linear Congruence

**Theorem.** If $(a, n) = d > 1$, the congruence $ax + b \equiv 0 \pmod{n}$ is solvable if and only if $d \mid b$. In that case, there are exactly $d$ distinct solutions modulo $n$.

*Proof.* Write $a = d a_1$, $n = d n_1$ with $(a_1, n_1) = 1$.

*Necessity.* The congruence $ax + b \equiv 0 \pmod{n}$ is equivalent to the Diophantine equation
$$ax - nz = -b$$
for some integer $z$. Since $d \mid a$ and $d \mid n$, the left-hand side $ax - nz$ is divisible by $d$ for all integers $x, z$. Therefore $d \mid b$ is a necessary condition for any integer solution $x$ to exist.

*Sufficiency.* Assume $d \mid b$ and write $b = d b_1$. The congruence
$$d a_1 x + d b_1 \equiv 0 \pmod{d n_1}$$
is equivalent (by cancelling the common factor $d$) to
$$a_1 x + b_1 \equiv 0 \pmod{n_1}.$$

Since $(a_1, n_1) = 1$, Theorem 14 yields a unique solution $x_0$ modulo $n_1$. Every integer congruent to $x_0$ modulo $n_1$ satisfies the reduced congruence, hence also the original one. The general solution is therefore
$$x = x_0 + n_1 y, \quad y \in \mathbb{Z}.$$

*Number of distinct solutions modulo $n$.* Two such values $x_0 + n_1 y_1$ and $x_0 + n_1 y_2$ are congruent modulo $n = d n_1$ precisely when $n_1(y_1 - y_2)$ is divisible by $d n_1$, i.e., when $y_1 \equiv y_2 \pmod{d}$. Thus the $d$ choices $y = 0, 1, \ldots, d-1$ give $d$ pairwise incongruent solutions modulo $n$, and every other integer $y$ gives a solution congruent to one of these $d$. $\square$
