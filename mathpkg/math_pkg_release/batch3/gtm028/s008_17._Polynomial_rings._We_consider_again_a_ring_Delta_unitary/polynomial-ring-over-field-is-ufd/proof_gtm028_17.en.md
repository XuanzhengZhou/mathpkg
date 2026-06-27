---
role: proof
locale: en
of_concept: polynomial-ring-over-field-is-ufd
source_book: gtm028
source_chapter: "I"
source_section: "17"
---

**Proof.** Since $F$ is a field, every non-zero element is a unit, hence regular. Theorem 9 shows that $F[x]$ satisfies the Euclidean algorithm (condition E2), so $F[x]$ is a Euclidean domain. Every Euclidean domain is a principal ideal domain, and every PID is a unique factorization domain. Hence $F[x]$ is a UFD.

For the second statement: every polynomial $f(x) = a_n x^n + \cdots + a_0$ with $a_n \neq 0$ has monic associate $a_n^{-1} f(x)$. Two polynomials are associates if and only if each divides the other; since degree considerations force the quotient to have degree zero, they differ by a non-zero factor in $F$.
