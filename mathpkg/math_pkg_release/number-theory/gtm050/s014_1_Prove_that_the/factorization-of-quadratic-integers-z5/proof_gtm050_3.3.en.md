---
role: proof
locale: en
of_concept: factorization-of-quadratic-integers-z5
source_book: gtm050
source_chapter: "3"
source_section: "3.3"
---

Granted Dirichlet's Lemma, the argument proceeds as follows. By the lemma, for each prime factor $P_i$ of $a^2 - 5b^2$, there exist integers $p_i, q_i$ such that $p_i^2 - 5q_i^2 = P_i$. (Note that $P_i$ is odd because $a$ and $b$ have opposite parity.)

Since $P_1$ divides both $a^2 - 5b^2$ and $p_1^2 - 5q_1^2$, it also divides

$$(p_1 b - q_1 a)(p_1 b + q_1 a) = p_1^2 b^2 - q_1^2 a^2 = b^2(p_1^2 - 5q_1^2) - q_1^2(a^2 - 5b^2).$$

Therefore $P_1$ divides either $p_1 b - q_1 a$ or $p_1 b + q_1 a$. By changing the sign of $q_1$ if necessary, one can ensure $P_1$ divides $p_1 b - q_1 a$. Then

$$\frac{a + b\sqrt{5}}{p_1 + q_1\sqrt{5}} = \frac{(a + b\sqrt{5})(p_1 - q_1\sqrt{5})}{p_1^2 - 5q_1^2} = \frac{a p_1 - 5b q_1}{P_1} + \frac{b p_1 - a q_1}{P_1}\sqrt{5}$$

is an element of $\mathbb{Z}[\sqrt{5}]$ (both coefficients are integers because $P_1$ divides the numerators). Iterating this process for each prime factor $P_i$ with its exponent $n_i$ yields the factorization

$$a + b\sqrt{5} = (p_1 + q_1\sqrt{5})^{n_1} (p_2 + q_2\sqrt{5})^{n_2} \cdots (p_k + q_k\sqrt{5})^{n_k} (t + u\sqrt{5})$$

where the remaining factor $t + u\sqrt{5}$ must satisfy $t^2 - 5u^2 = 1$, i.e., it is a unit in $\mathbb{Z}[\sqrt{5}]$ arising from Pell's equation.
