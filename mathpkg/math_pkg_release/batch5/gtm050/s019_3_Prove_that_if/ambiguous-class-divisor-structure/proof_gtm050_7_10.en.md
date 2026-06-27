---
role: proof
locale: en
of_concept: ambiguous-class-divisor-structure
source_book: gtm050
source_chapter: "7"
source_section: "7.10"
---

Let $A_0 \sim A \sim \bar{A} \sim \bar{A}_0$ be divisors with $A$ in an ambiguous class, and let $A_0$ be reduced with norm $a_0 = N(A_0)$.

**Case 1:** $D \equiv 2$ or $3 \pmod 4$, and $a_1 > a_0$.

Apply the cyclic method to $\bar{A}_0$, which increases its norm. By the theorem of Section 7.7, $A_0 \sim \bar{A}_0$ implies $A_0 = \bar{A}_0$. Hence $A_0$ divides both $r_0 - \sqrt{D}$ and $r_0 + \sqrt{D}$, so $A_0$ divides $2r_0$. Thus $a_0$ divides $2r_0$. Since $a_0$ divides $r_0^2 - D$, it also divides $(2r_0)^2 - 4D$, and therefore $a_0$ divides $4D$. Every prime integer divisor of $4D$ is a prime which ramifies (because $D \equiv 2$ or $3 \pmod 4$). Hence $A_0$ has the desired form $(p_1,*)(p_2,*)\cdots(p_k,*)$.

**Case 2:** $D \equiv 2$ or $3 \pmod 4$, and $a_0 = a_1$.

Define $B$ by the condition that $A_0\bar{B}$ is the divisor of $r_0 + a_0 - \sqrt{D}$. Let $N(B) = b$. Then
$$a_0b = r_0^2 - D + 2a_0r_0 + a_0^2 = a_0a_1 + 2a_0r_0 + a_0^2,$$
so $b = 2(a_0 + r_0)$. Since $b$ divides $(r_0 + a_0)^2 - D$, it also divides $4(r_0 + a_0)^2 - 4D = b^2 - 4D$, hence $b \mid 4D$. Therefore $B \sim A_0$ is a divisor of the required form.

**Case 3:** $D < 0$, $D \equiv 1 \pmod 4$.

If $A_0 \sim \bar{A}_0$, then by the theorem of Section 7.7, $\bar{A}_0$ must occur in the period of $A_0$: say $\bar{A}_0 = A_j$. Then $A_0 = \bar{A}_j$, and $A_1 = \bar{A}_{j-1}$, $A_2 = \bar{A}_{j-2}$, and so forth. Since $N(A_j)$ alternates in sign and $N(A_0) = N(\bar{A}_0) = N(A_j)$, $j$ must be even; write $j = 2k$. Then $A_k = \bar{A}_{j-k} = \bar{A}_k$. Thus $A_k$ divides both $r_k - \sqrt{D}$ and $r_k + \sqrt{D}$, so $a_k$ divides $2r_k$. As before, $a_k$ divides $4D$, and $A_k$ is of the required form.

The remaining case $D > 0$, $D \equiv 1 \pmod 4$ follows from similar modifications.

Thus every ambiguous class is represented by a divisor of the form $(p_1,*)(p_2,*)\cdots(p_k,*)$ where each factor comes from a ramified prime (or $-1$ when $D > 0$).
