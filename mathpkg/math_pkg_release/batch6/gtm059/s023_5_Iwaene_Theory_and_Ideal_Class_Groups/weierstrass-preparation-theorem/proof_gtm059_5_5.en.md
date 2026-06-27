---
role: proof
locale: en
of_concept: weierstrass-preparation-theorem
source_book: gtm059
source_chapter: "5"
source_section: "5"
---
By the Weierstrass Division Theorem (Theorem 2.1), divide $X^n$ by $f$: there exist $q \in A[[X]]$ and $r \in A[X]$ with $\deg r < n$ such that $X^n = qf + r$. Then $r \equiv X^n \pmod{\mathfrak{m}}$ because $a_n$ is a unit and the lower coefficients of $f$ lie in $\mathfrak{m}$. Hence $r$ is a monic polynomial of degree $n$ modulo $\mathfrak{m}$, and $q$ is a unit in $A[[X]]$ (its constant term is $a_n^{-1}$ modulo $\mathfrak{m}$). Rearranging gives $qf = X^n - r$, so $f = q^{-1}(X^n - r)$. Setting $P(X) = X^n - r$ and $u = q^{-1}$ yields the desired factorization. Uniqueness follows from the uniqueness in the Division Theorem.
