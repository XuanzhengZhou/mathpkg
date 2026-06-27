---
role: proof
locale: en
of_concept: modular-functions-as-rational-functions-of-j
source_book: gtm041
source_chapter: "2"
source_section: "2.6"
---

The first part is clear. To prove the second, suppose $f$ has zeros at $z_1, \ldots, z_n$ and poles at $p_1, \ldots, p_n$ with the usual conventions about multiplicities. Let

$$g(\tau) = \prod_{k=1}^{n} \frac{J(\tau) - J(z_k)}{J(\tau) - J(p_k)}$$

where a factor $1$ is inserted whenever $z_k$ or $p_k$ is $\infty$. Then $g$ is a rational function of $J$, hence $g$ is a modular function. Moreover, $g$ has the same zeros and poles as $f$ in the closure of the fundamental region $R_{\Gamma}$. Therefore the quotient $f/g$ is a modular function with no zeros or poles in the closure of $R_{\Gamma}$, hence $f/g$ has no zeros or poles anywhere in the upper half-plane $H$. By a standard argument (applying the maximum modulus principle to suitable powers), $f/g$ must be constant. Thus $f = c \cdot g$ for some constant $c$, and $f$ is a rational function of $J$.
