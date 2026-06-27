---
role: proof
locale: en
of_concept: crt-residue-system
source_book: gtm077
source_chapter: "I"
source_section: "2"
---

# Proof of Theorem 8: Residue Systems for Composite Moduli

**Theorem.** If $a_1, a_2, \ldots, a_n$ are pairwise relatively prime positive integers, then a complete residue system modulo $A = a_1 a_2 \cdots a_n$ is obtained in the form

$$L(x_1, \ldots, x_n) = \frac{A}{a_1} c_1 x_1 + \frac{A}{a_2} c_2 x_2 + \cdots + \frac{A}{a_n} c_n x_n,$$

where each $x_i$ runs independently through a complete residue system modulo $a_i$, and the $c_i$ are arbitrary integers satisfying $(c_i, a_i) = 1$.

*Proof.* The number of distinct $n$-tuples $(x_1, \ldots, x_n)$ in the Cartesian product is $a_1 \times a_2 \times \cdots \times a_n = A$. It suffices to prove that the $A$ values of $L(x_1, \ldots, x_n)$ are pairwise incongruent modulo $A$.

Suppose $L(x_1, \ldots, x_n) \equiv L(x'_1, \ldots, x'_n) \pmod{A}$. We will show that $x_i \equiv x'_i \pmod{a_i}$ for each $i$.

**Step 1: Reduction modulo each $a_k$.** For a fixed index $k$, consider the congruence modulo $a_k$. Note that for any $i \neq k$, the coefficient $A/a_i$ is divisible by $a_k$ (since $a_k$ is one of the factors in $A$ and is distinct from $a_i$, so $a_k$ divides $A/a_i$). Thus

$$\frac{A}{a_i} c_i x_i \equiv 0 \pmod{a_k} \quad \text{for all} \quad i \neq k.$$

The congruence $L(x_1, \ldots, x_n) \equiv L(x'_1, \ldots, x'_n) \pmod{A}$ implies it also holds modulo $a_k$. Reducing modulo $a_k$, all terms with $i \neq k$ vanish, leaving

$$\frac{A}{a_k} c_k x_k \equiv \frac{A}{a_k} c_k x'_k \pmod{a_k}.$$

**Step 2: Cancellation.** We have $(A/a_k, a_k) = 1$ because $A/a_k$ is the product of all $a_i$ with $i \neq k$, each of which is coprime to $a_k$. Also, by hypothesis $(c_k, a_k) = 1$. Therefore

$$\left(\frac{A}{a_k} c_k, \; a_k\right) = 1.$$

By Theorem 6, since the coefficient $(A/a_k)c_k$ is coprime to the modulus $a_k$, we may cancel it:

$$x_k \equiv x'_k \pmod{a_k}.$$

**Step 3: Conclusion.** Since this holds for every $k = 1, \ldots, n$, distinct $n$-tuples $(x_1, \ldots, x_n)$ from the complete residue systems modulo the respective $a_i$ give incongruent values of $L$ modulo $A$. Hence the $A$ values form a complete residue system modulo $A$. $\square$

**Remark.** This theorem provides a constructive parametrization of residue classes modulo a product of pairwise coprime integers, and is a form of the Chinese Remainder Theorem. The constants $c_i$ can be chosen to satisfy $(A/a_i) c_i \equiv 1 \pmod{a_i}$, which is possible precisely because $(A/a_i, a_i) = 1$ (by Theorem 1). With such a choice, $L(x_1, \ldots, x_n) \equiv x_i \pmod{a_i}$ for each $i$.
