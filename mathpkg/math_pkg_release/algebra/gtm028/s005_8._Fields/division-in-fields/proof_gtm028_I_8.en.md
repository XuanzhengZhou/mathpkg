---
role: proof
locale: en
of_concept: division-in-fields
source_book: gtm028
source_chapter: "I"
source_section: "8. Fields"
---

(1) Let $a, b \in F$, $a \neq 0$. By $F_3$, $a$ has a multiplicative inverse $a^{-1}$. Then $x = a^{-1}b$ satisfies $ax = a(a^{-1}b) = (aa^{-1})b = 1 \cdot b = b$, so a solution exists. If $x_1, x_2$ are two solutions, then $ax_1 = b = ax_2$, so $ax_1 - ax_2 = 0$, i.e., $a(x_1 - x_2) = 0$. Since $a \neq 0$ and a field has no zero divisors (as shown in the proof that every field is an integral domain), we must have $x_1 - x_2 = 0$, hence $x_1 = x_2$. Thus the solution is unique and is denoted $b/a$.

(2) If $a \neq 0$, the equation $ax = 0$ has the unique solution $x = a^{-1} \cdot 0 = 0$, since $a$ is not a zero divisor. Thus $0/a = 0$.

(3) If $a = 0$, the equation becomes $0 \cdot x = b$ for any $x \in F$. If $b \neq 0$, no $x$ satisfies this equation, so there is no solution. If $b = 0$, every $x \in F$ satisfies $0 \cdot x = 0$, so every element is a solution and the quotient is not uniquely defined. Hence division by zero is impossible in a field.
