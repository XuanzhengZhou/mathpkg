---
role: proof
locale: en
of_concept: residue-class-group-decomposition
source_book: gtm077
source_chapter: "III"
source_section: "13"
---
# Proof of Theorem 42: Decomposition of the Residue Class Group

**Theorem 42.** Suppose $(n_1, n_2) = 1$, $n = n_1 \cdot n_2$. Then

$$\Re(n) = \Re(n_1) \cdot \Re(n_2).$$

*Proof.* We assign to each element $A$ of $\Re(n)$ a pair of elements $C_1$ from $\Re(n_1)$ and $C_2$ from $\Re(n_2)$ as follows: If $a$ is a number in $A$, then choose any two numbers $c_1, c_2$ according to the conditions

$$c_1 \equiv a \pmod{n_1}, \quad c_2 \equiv a \pmod{n_2}. \tag{20}$$

The residue class $C_1$ of $c_1$ modulo $n_1$ is determined uniquely by $A$, likewise the residue class $C_2$ of $c_2$ modulo $n_2$. We set

$$A = (C_1, C_2)$$

where $C_1$ belongs to $\Re(n_1)$ and $C_2$ belongs to $\Re(n_2)$. Conversely, if $c_1$ and $c_2$ are two numbers relatively prime to $n_1$ and $n_2$ respectively, then by Theorem 15 (the Chinese Remainder Theorem), since $(n_1, n_2) = 1$, there is an $a$ determined uniquely by the modulus $n = n_1 \cdot n_2$ which satisfies (20).

Moreover, it obviously follows from

$$A = (C_1, C_2), \quad A' = (C'_1, C'_2)$$

that

$$AA' = (C_1 C'_1, C_2 C'_2).$$

Thus the group $\Re(n)$ is represented as a direct product of the groups $\Re(n_1)$ and $\Re(n_2)$. The mapping $A \mapsto (C_1, C_2)$ is a group isomorphism:

1. **Well-defined:** If $a' \equiv a \pmod{n}$ is another representative of $A$, then $a' \equiv a \pmod{n_1}$ and $a' \equiv a \pmod{n_2}$, so the residue classes $C_1$ and $C_2$ are uniquely determined by $A$.

2. **Surjective:** For any $(C_1, C_2) \in \Re(n_1) \times \Re(n_2)$ with representatives $c_1, c_2$, the Chinese Remainder Theorem (Theorem 15) guarantees a unique $a$ modulo $n$ satisfying both congruences simultaneously. The class $A$ of $a$ modulo $n$ maps to $(C_1, C_2)$.

3. **Injective:** If $A$ and $A'$ map to the same pair, then their representatives satisfy $a \equiv a' \pmod{n_1}$ and $a \equiv a' \pmod{n_2}$. Since $(n_1, n_2) = 1$, this implies $a \equiv a' \pmod{n}$, so $A = A'$.

4. **Homomorphism:** The multiplication rule $AA' = (C_1 C_1', C_2 C_2')$ shows that the map preserves the group operation.

Therefore $\Re(n) \cong \Re(n_1) \times \Re(n_2)$. $\square$

By repeated application, this reduces the study of $\Re(n)$ to the case where $n$ is a prime power.
