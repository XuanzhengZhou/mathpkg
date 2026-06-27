---
role: proof
locale: en
of_concept: linear-congruence-general
source_book: gtm077
source_chapter: "I"
source_section: "4"
---
# Proof of Theorem 15: The General Linear Congruence

**Theorem.** Consider $ax + b \equiv 0 \pmod{n}$ with $d = (a, n) > 1$. The congruence is solvable if and only if $d \mid b$. In this case there are exactly $d$ distinct solutions modulo $n$. They are obtained by solving the reduced congruence $(a/d)x + (b/d) \equiv 0 \pmod{n/d}$, which has a unique solution $x_0$ modulo $n/d$, and taking
$$x = x_0 + \frac{n}{d}\,y, \quad y = 0, 1, \ldots, d-1.$$

*Proof.* Set $d = (a, n)$ and write
$$a = d a_1, \quad n = d n_1, \quad \text{with } (a_1, n_1) = 1.$$

The congruence $ax + b \equiv 0 \pmod{n}$ means $n \mid (ax + b)$, i.e., there exists an integer $z$ such that $ax + b = nz$. Substituting the factorizations,
$$d a_1 x + b = d n_1 z \implies b = d(n_1 z - a_1 x).$$
Hence $d \mid b$ is necessary for solvability.

Suppose $d \mid b$ and write $b = d b_1$. Dividing the original congruence by $d$ (which is legitimate since all terms are multiples of $d$) yields the equivalent reduced congruence
$$a_1 x + b_1 \equiv 0 \pmod{n_1}.$$

Since $(a_1, n_1) = 1$, Theorem 14 (the coprime case) guarantees exactly one solution $x_0$ modulo $n_1$. Thus every integer of the form
$$x = x_0 + n_1 y = x_0 + \frac{n}{d}\,y, \quad y \in \mathbb{Z}$$
satisfies the reduced congruence and hence the original one.

To determine how many of these are distinct modulo $n$, note that two such values $x_0 + n_1 y_1$ and $x_0 + n_1 y_2$ are congruent modulo $n = d n_1$ if and only if $y_1 \equiv y_2 \pmod{d}$. Therefore letting $y$ run through a complete residue system modulo $d$ — for instance $y = 0, 1, \ldots, d-1$ — produces exactly $d$ distinct solutions modulo $n$. $\square$
