---
role: proof
locale: en
of_concept: sophie-germains-theorem
source_book: gtm050
source_chapter: "3"
source_section: "3.2"
---

Suppose $x^p + y^p = z^p$ with $p \nmid xyz$ (Case I). Let $q$ be an auxiliary prime satisfying conditions (1) and (2). Working modulo $q$, condition (1) forces one of $x, y, z$ to be divisible by $q$. The proof proceeds by showing that this leads to a contradiction with condition (2) via descent arguments and properties of $p$-th power residues.

The key idea: since $p \nmid xyz$, one can factor $x^p + y^p = z^p$ as $(x+y)(x+\zeta y)\cdots(x+\zeta^{p-1}y) = z^p$ where $\zeta$ is a primitive $p$-th root of unity. The factors are pairwise relatively prime in a suitable sense. Condition (1) on $q$ ensures that $x+y$ is a $p$-th power modulo $q$, and the descent argument forces the existence of a solution to $x^p \equiv p \pmod{q}$, contradicting condition (2).
