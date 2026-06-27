---
role: proof
locale: en
of_concept: lagrange-four-square-theorem
source_book: gtm007
source_chapter: "IV"
source_section: "§3. Quadratic forms over Q"
---

Let $n$ be a positive integer. Write $n = 4^a m$ where $m$ is not divisible by $4$.

If $m \equiv 1, 2, 3, 5, 6 \pmod{8}$, then $m$ is not of the form $8b-1$. By the three-square theorem, $m$ is a sum of three squares. Multiplying by $4^a$ (which is a square of $2^a$) and absorbing it into the squares, $n$ is also a sum of three squares, hence a fortiori a sum of four squares (add $0^2$).

If $m \equiv -1 \pmod{8}$, then $m-1 \equiv -2 \equiv 6 \pmod{8}$, so $m-1$ is not of the forbidden form $8b-1$. By the three-square theorem, $m-1 = x_1^2 + x_2^2 + x_3^2$. Hence
$$
m = x_1^2 + x_2^2 + x_3^2 + 1^2
$$
is a sum of four squares. Again, multiplying by $4^a$ preserves this property. Thus every positive integer is a sum of four squares.
