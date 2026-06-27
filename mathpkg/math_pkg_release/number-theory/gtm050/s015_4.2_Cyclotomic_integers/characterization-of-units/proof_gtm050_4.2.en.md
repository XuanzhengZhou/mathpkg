---
role: proof
locale: en
of_concept: characterization-of-units
source_book: gtm050
source_chapter: "4"
source_section: "4.2"
---

Suppose $f(\alpha)g(\alpha) = 1$ for cyclotomic integers $f(\alpha)$ and $g(\alpha)$. Taking norms of both sides and using the multiplicativity of the norm,
$$N\bigl(f(\alpha)g(\alpha)\bigr) = Nf(\alpha) \cdot Ng(\alpha) = N(1) = 1.$$
Since $Nf(\alpha)$ and $Ng(\alpha)$ are ordinary integers (by the proposition that the norm is an integer), and their product is $1$, each must be $\pm 1$. However, norms of cyclotomic integers are always non-negative (as products of complex numbers times their complex conjugates in a suitable grouping), so $Nf(\alpha) \geq 0$ and $Ng(\alpha) \geq 0$. Therefore $Nf(\alpha) = Ng(\alpha) = 1$. Hence $f(\alpha)$ is a unit.

Now multiply both sides of $f(\alpha)g(\alpha) = 1$ by $f(\alpha^2)f(\alpha^3)\cdots f(\alpha^{\lambda-1})$:
$$\bigl(f(\alpha^2)f(\alpha^3)\cdots f(\alpha^{\lambda-1})\bigr) \cdot f(\alpha) \cdot g(\alpha) = f(\alpha^2)f(\alpha^3)\cdots f(\alpha^{\lambda-1}).$$
But $f(\alpha) \cdot f(\alpha^2)\cdots f(\alpha^{\lambda-1}) = Nf(\alpha) = 1$, so the left side equals $g(\alpha)$. Thus
$$g(\alpha) = f(\alpha^2)f(\alpha^3)\cdots f(\alpha^{\lambda-1}),$$
as claimed.
