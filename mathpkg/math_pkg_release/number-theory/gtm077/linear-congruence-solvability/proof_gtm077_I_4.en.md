---
role: proof
locale: en
of_concept: linear-congruence-solvability
source_book: gtm077
source_chapter: "I"
source_section: "4"
---
# Proof of Theorem 14 (with Theorem 15): Complete Solvability Theory

**Theorem.** Consider the linear congruence
$$ax + b \equiv 0 \pmod{n}, \quad n > 0.$$

*If $(a, n) = 1$:* The congruence has exactly one solution modulo $n$.

*If $(a, n) = d > 1$:* The congruence is solvable if and only if $d \mid b$. In this case there are exactly $d$ distinct solutions modulo $n$.

*Proof.* **Part 1: $(a, n) = 1$.** By Theorem 7 (the group property of residue systems), as $x$ runs through a complete residue system modulo $n$, the multiples $ax$ also run through a complete residue system. Hence $ax + b$ falls exactly once into the residue class $0 \pmod{n}$, giving exactly one solution. Explicitly, the unique solution modulo $n$ is $x \equiv -a'b \pmod{n}$, where $a'$ satisfies $aa' \equiv 1 \pmod{n}$.

**Part 2: $(a, n) = d > 1$.** The congruence $ax + b \equiv 0 \pmod{n}$ is equivalent to the linear Diophantine equation
$$ax - nz = -b, \quad z \in \mathbb{Z}.$$
Let $n = d n_1$, $a = d a_1$ with $(a_1, n_1) = 1$. Then
$$d(a_1 x - n_1 z) = -b,$$
so $d \mid b$ is a necessary condition. Assuming $d \mid b$, write $b = d b_1$. The congruence reduces to
$$a_1 x + b_1 \equiv 0 \pmod{n_1}.$$
Since $(a_1, n_1) = 1$, Part 1 yields a unique solution $x_0$ modulo $n_1$. All numbers of the form
$$x = x_0 + n_1 y, \quad y \in \mathbb{Z}$$
satisfy the reduced congruence and hence the original. Among these, exactly $d$ are distinct modulo $n = d n_1$, obtained by letting $y$ run through a complete residue system modulo $d$. $\square$

The result also follows from Theorem 1 (on linear Diophantine equations), providing an alternative derivation: the equation $ax - nz = -b$ has integer solutions iff $d = (a, n) \mid b$, and the general solution in $x$ yields exactly $d$ incongruent values modulo $n$. $\square$
