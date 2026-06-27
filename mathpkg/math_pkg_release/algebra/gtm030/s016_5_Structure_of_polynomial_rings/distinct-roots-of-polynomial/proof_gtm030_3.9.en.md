---
role: proof
locale: en
of_concept: distinct-roots-of-polynomial
source_book: gtm030
source_chapter: "3"
source_section: "9"
---

If $c_1$ is a root of $f(x) = 0$, then by the Remainder Theorem $f(x) = (x - c_1)f_1(x)$. Suppose now that $c_1, c_2, \ldots, c_m$ are distinct roots of $f(x) = 0$. Substitute $c_2$ into $f(x) = (x - c_1)f_1(x)$ via the evaluation homomorphism $g(x) \mapsto g(c_2)$, obtaining
$$0 = f(c_2) = (c_2 - c_1)f_1(c_2).$$
Since $c_2 \neq c_1$ and $\mathfrak{F}$ is a field (hence an integral domain), $c_2 - c_1 \neq 0$ forces $f_1(c_2) = 0$. Hence $f_1(x) = (x - c_2)f_2(x)$, so $f(x) = (x - c_1)(x - c_2)f_2(x)$. Continuing by induction, we obtain
$$f(x) = (x - c_1)(x - c_2)\cdots(x - c_m)g(x)$$
for some polynomial $g(x)$. Comparing degrees, $\deg f = m + \deg g \geq m$, so $m \leq \deg f$.
