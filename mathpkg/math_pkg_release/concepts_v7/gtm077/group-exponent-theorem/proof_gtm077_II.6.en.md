---
role: proof
locale: en
of_concept: group-exponent-theorem
source_book: gtm077
source_chapter: "II"
source_section: "6"
---

# Proof of Theorem 21: Exponent Property in Finite Groups

**Theorem 21.** If $h$ is the order of a finite group $\mathfrak{G}$, then $A^h = E$ for every element $A \in \mathfrak{G}$. Furthermore, if $a$ is the order of $A$ (so that $A^r = E$ iff $a \mid r$), then $a$ divides $h$, and for any integers $m, n$, $A^m = A^n$ implies $m \equiv n \pmod{a}$.

**Proof.** Let $a$ be the order of the element $A$. The powers $E, A, A^2, \ldots, A^{a-1}$ form a cyclic subgroup $\langle A \rangle$ of $\mathfrak{G}$ of order $a$ (all $a$ elements are distinct; if $A^i = A^j$ with $0 \leq i < j < a$, then $A^{j-i} = E$, contradicting minimality of $a$). By Lagrange's Theorem (Theorem 19), the order of any subgroup divides the order of the group, so $a \mid h$.

Write $h = a \cdot k$ for some integer $k$. Then

$$A^h = A^{a \cdot k} = (A^a)^k = E^k = E.$$

For the second assertion: if $A^m = A^n$, then $A^{m-n} = E$. By definition of the order $a$, this holds if and only if $a \mid (m-n)$, i.e., $m \equiv n \pmod{a}$.

**Remarks.**
- This generalizes Euler's Theorem from number theory (in the multiplicative group modulo $n$, $\varphi(n)$ plays the role of $h$).
- For the additive group of residue classes modulo an ideal (as used in the text), the statement becomes $h \cdot \alpha \equiv 0 \pmod{\mathfrak{a}}$. ∎
