---
role: proof
locale: en
of_concept: euler-failure-2x2-minus-5-cube
source_book: gtm050
source_chapter: "2"
source_section: "2.3"
---

Euler's method for the cube case: to find $x$ such that $2x^2 - 5$ is a cube, set

$$
x\sqrt{2} + \sqrt{5} = (a\sqrt{2} + b\sqrt{5})^3,
$$

where $a, b$ are integers. Expanding the cube:

$$
\begin{aligned}
(a\sqrt{2} + b\sqrt{5})^3
&= a^3(\sqrt{2})^3 + 3a^2b(\sqrt{2})^2\sqrt{5} + 3ab^2\sqrt{2}(\sqrt{5})^2 + b^3(\sqrt{5})^3 \\
&= a^3(2\sqrt{2}) + 3a^2b(2\sqrt{5}) + 3ab^2\sqrt{2}(5) + b^3(5\sqrt{5}) \\
&= (2a^3 + 15ab^2)\sqrt{2} + (6a^2b + 5b^3)\sqrt{5}.
\end{aligned}
$$

Comparing coefficients with $x\sqrt{2} + 1\cdot\sqrt{5}$ gives:

$$
\begin{cases}
x = 2a^3 + 15ab^2, \\
1 = 6a^2b + 5b^3.
\end{cases}
$$

The second equation is a Diophantine equation in integers $a, b$. Since $b$ divides the right-hand side, $b \mid 1$, so $b = \pm 1$. Substituting:

- If $b = 1$: $6a^2 + 5 = \pm 1$. Then $6a^2 = -4$ or $6a^2 = -6$, both impossible for integer $a$.
- If $b = -1$: $-6a^2 - 5 = \pm 1$. Then $6a^2 + 5 = \mp 1$, which again gives $6a^2 = -4$ or $6a^2 = -6$, impossible.

Therefore no integer solutions $(a, b)$ exist, so Euler's method finds no solution for $2x^2 - 5 = \text{cube}$. This is not a contradiction — the equation may genuinely have no solution — but it demonstrates that the method itself gives no positive result. More importantly, it shows that Euler was aware his method did not always produce solutions, unlike the integer case where a factorization as a product of relatively prime cubes always implies each factor is a cube.
