---
role: proof
locale: en
of_concept: cycle-representation-fermat
source_book: gtm050
source_chapter: "7"
source_section: "7.10"
---

Let $D \equiv 1 \pmod 4$ be a positive prime. Consider the cycle of reduced divisors equivalent to the principal class:
$$I \sim A_1 \sim A_2 \sim \cdots \sim A_p \sim I$$
where $p$ is the period length. Since $D \equiv 1 \pmod 4$, the divisor $(-1, *)$ is an ambiguous divisor and lies in the principal class. This implies that the conjugate $\bar{A}_i$ of each divisor in the cycle also appears in the cycle.

Because norms alternate in sign along the cycle and because $\bar{A}_i$ has the same norm as $A_i$ (up to sign), there must exist consecutive divisors $A_i$ and $A_{i+1}$ with $N(A_i) = -N(A_{i+1})$.

Now for a reduced divisor $A_i = (a, r + \sqrt{D})$ with norm $N(A_i) = a$, the condition $a = -b$ where $b = N(A_{i+1})$ means that $ab = -a^2 = r^2 - D$ for some $r$, hence $D = r^2 + a^2$. Setting $u = r$ and $v = a$ gives the representation $D = u^2 + v^2$.

The method can be applied explicitly: for $D = 13$, the cycle is $I \sim (2, 1+\sqrt{13}) \sim (3, 1+\sqrt{13}) \sim (3, 2+\sqrt{13}) \sim (2, 1+\sqrt{13}) \sim I$, and $13 = 2^2 + 3^2$. For $D = 233$, the computation yields $233 = 8^2 + 13^2$.
