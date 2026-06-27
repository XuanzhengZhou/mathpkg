---
role: proof
locale: en
of_concept: counterexample-49-not-c5-method
source_book: gtm050
source_chapter: "2"
source_section: "2.3"
---

We have $49 = 2^2 + 5 \cdot 3^2$, so $x = 2$ and $y = 3$ with $c = 5$.

Euler's method would assert that $x = cq^2 - p^2$ and $y = 2pq$ for some integers $p, q$. This gives the system:

$$
\begin{cases}
2 = 5q^2 - p^2, \\
3 = 2pq.
\end{cases}
$$

From the second equation, $pq = 3/2$, which is not an integer, so no integer solutions $(p, q)$ exist. Even allowing rational solutions, eliminating $p = 3/(2q)$ and substituting into the first equation:

$$
2 = 5q^2 - \frac{9}{4q^2}.
$$

Multiplying by $4q^2$: $8q^2 = 20q^4 - 9$, or $20q^4 - 8q^2 - 9 = 0$. Let $u = q^2$; then $20u^2 - 8u - 9 = 0$, which gives $u = \frac{8 \pm \sqrt{64 + 720}}{40} = \frac{8 \pm \sqrt{784}}{40} = \frac{8 \pm 28}{40}$. The positive root is $u = 36/40 = 9/10$, so $q = \sqrt{9/10}$ and $p = 3/(2q) = 3/(2\sqrt{9/10}) = \sqrt{5/2}$, as stated.

Thus the hyperbolas intersect only at irrational points, and Euler's parametric representation fails to capture the integer solution $49 = 2^2 + 5 \cdot 3^2$. This counterexample shows that Euler's method is not generally valid for arbitrary $c$.
