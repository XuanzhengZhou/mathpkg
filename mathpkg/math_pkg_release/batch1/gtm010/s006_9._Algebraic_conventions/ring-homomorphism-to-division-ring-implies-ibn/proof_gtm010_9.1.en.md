---
role: proof
locale: en
of_concept: ring-homomorphism-to-division-ring-implies-ibn
source_book: gtm010
source_chapter: "9"
source_section: "9"
---

The condition (*) is satisfied by a given ring if and only if every matrix $A$, with entries in $R$, for which there is a matrix $B$ with $AB = I_m$ and $BA = I_n$, is square (i.e., has $m = n$). Let $f_*$ be the induced map taking matrices over $R$ into matrices over $D$, given by $f_*((a_{ij})) = (f(a_{ij}))$. Since $f$ is a ring homomorphism, $f_*(AB) = f_*(A)f_*(B)$ for all $A, B$.

Suppose that $A$ and $B$ are arbitrary matrices such that $AB = I_m$ and $BA = I_n$. Because $f(1)$ is a unit, $f(1) = 1$. So $f_*(I_q) = I_q$ for all $q$. Thus $f_*(A)f_*(B) = I_m$ and $f_*(B)f_*(A) = I_n$. Since $D$ is a division ring, $f_*(A)$ is square, implying that $A$ is square. Therefore $R$ satisfies (*).
