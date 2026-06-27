---
role: proof
locale: en
of_concept: linear-congruence-unique-solution
source_book: gtm077
source_chapter: "I"
source_section: "4"
---
# Proof of Theorem 14 (Unique Solution — Coprime Case)

**Theorem.** The congruence
$$ax + b \equiv 0 \pmod{n}$$
has exactly one solution modulo $n$ if $(a, n) = 1$.

*Proof.* Assume $(a, n) = 1$. By Theorem 7, as $x$ runs through a complete residue system modulo $n$, the values $ax$ also run through a complete residue system modulo $n$. Consequently, $ax + b$ runs through a complete residue system modulo $n$ as well.

In particular, $ax + b$ falls exactly once into the residue class $0$ modulo $n$. Hence there exists exactly one residue class $x \pmod{n}$ satisfying the congruence.

The unique solution can be expressed explicitly: since $(a, n) = 1$, there exists an integer $a'$ such that
$$aa' \equiv 1 \pmod{n}$$
(by Theorem 9, one may take $a' \equiv a^{\varphi(n)-1} \pmod{n}$). Multiplying the congruence by $a'$ yields the solution in the form
$$x \equiv -a'b \pmod{n}.$$

Thus there exists exactly one solution modulo $n$. $\square$
