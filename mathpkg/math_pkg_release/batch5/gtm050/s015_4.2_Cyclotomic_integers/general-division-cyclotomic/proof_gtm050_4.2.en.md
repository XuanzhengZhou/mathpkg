---
role: proof
locale: en
of_concept: general-division-cyclotomic
source_book: gtm050
source_chapter: "4"
source_section: "4.2"
---

Given the equation $f(\alpha)g(\alpha) = h(\alpha)$ with $f(\alpha) \neq 0$, multiply both sides by the product of the non-trivial conjugates of $f(\alpha)$:
$$f(\alpha)g(\alpha) \cdot f(\alpha^2)f(\alpha^3)\cdots f(\alpha^{\lambda-1}) = h(\alpha) \cdot f(\alpha^2)f(\alpha^3)\cdots f(\alpha^{\lambda-1}).$$

The left side simplifies by the definition of the norm:
$$f(\alpha)f(\alpha^2)\cdots f(\alpha^{\lambda-1}) \cdot g(\alpha) = Nf(\alpha) \cdot g(\alpha).$$

Thus the original equation $f(\alpha)g(\alpha) = h(\alpha)$ is equivalent to
$$Nf(\alpha) \cdot g(\alpha) = h(\alpha) \cdot f(\alpha^2)f(\alpha^3)\cdots f(\alpha^{\lambda-1}).$$

Since $Nf(\alpha)$ is an ordinary integer, this reduces the general division problem to the special case of division by an ordinary integer. By the division-by-ordinary-integer criterion, a solution $g(\alpha)$ exists if and only if all coefficients of the right-hand side $h(\alpha) \cdot f(\alpha^2)\cdots f(\alpha^{\lambda-1})$ are congruent to one another modulo $Nf(\alpha)$. In that case, $g(\alpha)$ is constructed by dividing each coefficient (after making them congruent) by $Nf(\alpha)$.
