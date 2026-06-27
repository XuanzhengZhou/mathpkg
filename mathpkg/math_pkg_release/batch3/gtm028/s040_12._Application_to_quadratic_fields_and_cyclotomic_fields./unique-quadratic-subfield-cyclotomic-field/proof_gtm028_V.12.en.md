---
role: proof
locale: en
of_concept: unique-quadratic-subfield-cyclotomic-field
source_book: gtm028
source_chapter: "V"
source_section: "12"
---

Since $p$ is odd, the Galois group of $\mathbb{Q}(z)$ over $\mathbb{Q}$ is a cyclic group of order $p-1$. A cyclic group of even order contains exactly one subgroup of index $2$ (the unique subgroup consisting of the squares). By the fundamental theorem of Galois theory, this subgroup corresponds to a quadratic subfield $K$ of $\mathbb{Q}(z)$, uniquely determined by $p$.

By the transitivity formula for discriminants (Theorem 31), the discriminant of the ring $R$ of algebraic integers of $K$ over $\mathbb{Z}$ divides $p^{p-2}$ (the discriminant of $\mathbb{Q}(z)$ over $\mathbb{Q}$). Since $K$ is a quadratic field, its discriminant is either a fundamental discriminant (an integer congruent to $1$ modulo $4$ and square-free, or $4$ times a square-free integer congruent to $2$ or $3$ modulo $4$). The only prime that can divide the discriminant is $p$ (since the discriminant divides $p^{p-2}$), so the discriminant of $K$ is either $p$ or $-p$ (or $4p$ or $-4p$, but the quadratic subfield in a cyclotomic field is always of the form $\mathbb{Q}(\sqrt{\pm p})$).

From the formulae for the discriminant of a quadratic field (derived from the algebraic integer criterion), we determine the exact field:
\begin{itemize}
\item If $p \equiv 1 \pmod{4}$, the discriminant $p$ (which is $\equiv 1 \pmod{4}$ and square-free) corresponds to $K = \mathbb{Q}(\sqrt{p})$.
\item If $p \equiv 3 \pmod{4}$, then $p \equiv 3 \pmod{4}$ is not a fundamental discriminant. The field with discriminant $p$ in this case is $\mathbb{Q}(\sqrt{-p})$, since $-p \equiv 1 \pmod{4}$ and is square-free.
\end{itemize}

In either case, the discriminant of $R$ over $\mathbb{Z}$ is $p$ (a prime), so the only ramified prime in $K$ is $p$.
