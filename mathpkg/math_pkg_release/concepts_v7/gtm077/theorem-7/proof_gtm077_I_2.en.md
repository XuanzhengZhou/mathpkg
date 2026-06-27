---
role: proof
locale: en
of_concept: theorem-7
source_book: gtm077
source_chapter: "I"
source_section: "2"
---

# Proof of Theorem 7: Translation of Complete Residue Systems

**Theorem.** If $x_1, x_2, \ldots, x_n$ forms a complete system of residues modulo $n$ (with $n > 0$), then

$$a x_1 + b, \; a x_2 + b, \; \ldots, \; a x_n + b$$

is also a complete system of residues modulo $n$, provided $a$ and $b$ are integers and $(a, n) = 1$.

*Proof.* A complete system of residues modulo $n$ consists of $n$ integers that are pairwise incongruent modulo $n$. We must therefore show that the $n$ numbers $a x_i + b$ ($i = 1, 2, \ldots, n$) are pairwise incongruent modulo $n$.

Suppose, for a contradiction, that two of these numbers are congruent modulo $n$:

$$a x_i + b \equiv a x_j + b \pmod{n} \quad \text{for some} \quad i \neq j.$$

Subtracting $b$ from both sides, we obtain

$$a x_i \equiv a x_j \pmod{n}.$$

Since $(a, n) = 1$, Theorem 6 (with $c = a$ and $d = 1$) allows us to cancel $a$:

$$x_i \equiv x_j \pmod{n}.$$

But this contradicts the hypothesis that $x_1, \ldots, x_n$ form a complete residue system (i.e., are pairwise incongruent modulo $n$). Therefore, no two of the numbers $a x_i + b$ are congruent modulo $n$.

Since there are exactly $n$ such numbers and they are pairwise incongruent modulo $n$, they form a complete system of residues modulo $n$. $\square$

**Remark.** The condition $(a, n) = 1$ is essential. If $(a, n) > 1$, the mapping $x \mapsto a x + b \pmod{n}$ is not injective on the residue classes modulo $n$, and the resulting $n$ numbers may not be pairwise incongruent.
