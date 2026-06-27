---
role: proof
locale: en
of_concept: euler-sufficient-condition-cube
source_book: gtm050
source_chapter: "2"
source_section: "2.3"
---

Assume $p + q\sqrt{-3} = (a + b\sqrt{-3})^3$ for integers $a, b$. Expanding the cube:

$$
\begin{aligned}
(a + b\sqrt{-3})^3
&= a^3 + 3a^2(b\sqrt{-3}) + 3a(b\sqrt{-3})^2 + (b\sqrt{-3})^3 \\
&= a^3 + 3a^2b\sqrt{-3} + 3ab^2(-3) + b^3(-3)\sqrt{-3} \\
&= (a^3 - 9ab^2) + (3a^2b - 3b^3)\sqrt{-3}.
\end{aligned}
$$

Thus $p = a^3 - 9ab^2$ and $q = 3a^2b - 3b^3$.

Its conjugate is obtained by replacing $\sqrt{-3}$ with $-\sqrt{-3}$:
$$
p - q\sqrt{-3} = (a - b\sqrt{-3})^3.
$$

Multiplying the two factorizations:
$$
\begin{aligned}
p^2 + 3q^2 &= (p + q\sqrt{-3})(p - q\sqrt{-3}) \\
&= (a + b\sqrt{-3})^3 (a - b\sqrt{-3})^3 \\
&= \bigl((a + b\sqrt{-3})(a - b\sqrt{-3})\bigr)^3 \\
&= (a^2 + 3b^2)^3.
\end{aligned}
$$

Since $a, b$ are integers, $a^2 + 3b^2 \in \mathbb{Z}$, so $p^2 + 3q^2$ is a perfect integer cube.
