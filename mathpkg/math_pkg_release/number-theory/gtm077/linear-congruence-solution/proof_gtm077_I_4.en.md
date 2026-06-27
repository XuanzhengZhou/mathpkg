---
role: proof
locale: en
of_concept: linear-congruence-solution
source_book: gtm077
source_chapter: "I"
source_section: "4"
---
# Proof of Theorem 14: Solvability of Linear Congruences

**Theorem.** The congruence
$$ax + b \equiv 0 \pmod{n}, \quad n > 0$$
has exactly one solution modulo $n$ if $(a, n) = 1$. If $(a, n) = d > 1$, then the congruence is solvable if and only if $d \mid b$, and in this case it has exactly $d$ distinct solutions modulo $n$.

*Proof.* We treat the two cases separately.

**Case 1: $(a, n) = 1$.** By Theorem 7, as $x$ runs through a complete residue system modulo $n$, the values $ax$ also run through a complete residue system modulo $n$. Hence $ax + b$ runs through a complete residue system, and in particular falls exactly once into the residue class $0$ modulo $n$. Therefore there is exactly one solution $x \pmod{n}$.

Moreover, since $(a, n) = 1$, there exists a modular inverse $a'$ with $aa' \equiv 1 \pmod{n}$ (by Theorem 9, one may take $a' = a^{\varphi(n)-1}$). Multiplying the congruence by $a'$ gives the explicit solution
$$x \equiv -a'b \pmod{n}.$$

**Case 2: $(a, n) = d > 1$.** Write $n = d n_1$, $a = d a_1$, where $(a_1, n_1) = 1$. The congruence $ax + b \equiv 0 \pmod{n}$ is equivalent to the Diophantine equation $ax - nz = -b$, i.e.,
$$d(a_1 x - n_1 z) = -b.$$
Thus a necessary condition for solvability is $d \mid b$. Set $b = d b_1$. The congruence then reduces to
$$a_1 x + b_1 \equiv 0 \pmod{n_1}.$$
Since $(a_1, n_1) = 1$, Case 1 applies and this reduced congruence has exactly one solution $x_0$ modulo $n_1$. All solutions of the original congruence are given by
$$x = x_0 + n_1 y, \quad y \in \mathbb{Z}.$$
Letting $y$ run through a complete residue system modulo $d$ yields exactly $d$ distinct solutions modulo $n$. $\square$
