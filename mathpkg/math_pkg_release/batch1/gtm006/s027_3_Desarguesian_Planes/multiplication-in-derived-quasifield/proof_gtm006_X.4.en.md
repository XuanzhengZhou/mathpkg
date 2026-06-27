---
role: proof
locale: en
of_concept: multiplication-in-derived-quasifield
source_book: gtm006
source_chapter: "X"
source_section: "4. General Derivation"
---

The line $[\alpha + \beta t, 0]'$ passes through $(0, 0)' = (0, 0)$ and $(-1, \alpha + \beta t)' = (-1 + \alpha t, \beta t)$. If $\beta \neq 0$, then $[\alpha + \beta t, 0]'$ is not of the form $\mathcal{B}(x, y, z)$ (since $(0, 0)$ lies on $\mathcal{B}(x, y, z)$ if and only if $\mathcal{B}(x, y, z) = \mathcal{B}(w, 0, 0)$ for some $w$, and $(-1 + \alpha t, \beta t)$ lies on no such line). Hence this line must be treated as a "new" line of the derived plane.

Equation (1) determines $\varrho$ and $\sigma$ from the incidence of $(-1 + \alpha t, \beta t)$ with the appropriate Baer subplane. Equation (2) then determines the point $(\gamma + \delta t, \eta + \mu t)$ on the same line, yielding the product. Solving the linear system gives:

$$r = -abu(a^2 u + av - 1)^{-1}, \quad s = -b(a^2 u + av - 1)^{-1}$$

and subsequently:

$$h = ac - b^{-1}dg(a), \quad m = bc - ad - dv/u$$

where $g(a) = a^2 + (v/u)a - 1/u$. Since every irreducible quadratic over $GF(q)$ is satisfied by some element in $GF(q^2)$, the polynomial $g$ ranges over all irreducible quadratics, establishing that any Hall quasifield can be obtained. For $\beta = 0$, the multiplication reduces to scalar multiplication because $[\alpha, 0]'$ is the Baer subplane $\mathcal{B}(\alpha, 0, 0)$ and the line structure is inherited directly from $\mathcal{A}$. $\square$
