---
role: proof
locale: en
of_concept: inverse-characterization-of-cyclotomic-units
source_book: gtm050
source_chapter: "4"
source_section: "4.2"
---

Suppose $f(\alpha)g(\alpha) = 1$. Taking norms and using multiplicativity,
$$Nf(\alpha) \cdot Ng(\alpha) = N(f(\alpha)g(\alpha)) = N(1) = 1.$$

Since $Nf(\alpha)$ and $Ng(\alpha)$ are ordinary integers, and norms of nonzero cyclotomic integers are positive, we must have $Nf(\alpha) = 1$ and $Ng(\alpha) = 1$. Hence $f(\alpha)$ is a unit by definition.

Now, by definition of the norm,
$$Nf(\alpha) = f(\alpha) \cdot f(\alpha^2) f(\alpha^3) \cdots f(\alpha^{\lambda-1}) = 1.$$

Multiplying the equation $f(\alpha)g(\alpha) = 1$ by the product $f(\alpha^2) \cdots f(\alpha^{\lambda-1})$ on both sides, we obtain
$$g(\alpha) = f(\alpha^2) f(\alpha^3) \cdots f(\alpha^{\lambda-1}),$$
since $f(\alpha)g(\alpha) \cdot (f(\alpha^2) \cdots f(\alpha^{\lambda-1})) = 1 \cdot (f(\alpha^2) \cdots f(\alpha^{\lambda-1}))$, and the left side becomes $g(\alpha) \cdot Nf(\alpha) = g(\alpha) \cdot 1 = g(\alpha)$. Therefore $g(\alpha)$ must equal the product of the conjugates $f(\alpha^2), \ldots, f(\alpha^{\lambda-1})$, establishing both the formula for the inverse and the fact that $f(\alpha) \cdot (f(\alpha^2) \cdots f(\alpha^{\lambda-1})) = 1$.
