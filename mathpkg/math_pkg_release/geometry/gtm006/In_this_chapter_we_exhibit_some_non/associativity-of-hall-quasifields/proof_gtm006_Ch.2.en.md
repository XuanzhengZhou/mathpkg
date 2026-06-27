---
role: proof
locale: en
of_concept: associativity-of-hall-quasifields
source_book: gtm006
source_chapter: "IX"
source_section: "2"
---

The Hall quasifield $H$ satisfies the right distributive law if and only if $(x + \lambda y)\lambda = x\lambda + y\lambda^2$ for all $x, y \in F$. Computing both sides using the multiplication rule and comparing coefficients yields:
\[
bx = bx^{-1} \quad \text{for all } x \in F, x \neq 0, \tag{9}
\]
\[
ax = a \quad \text{for all } x \in F, x \neq 0. \tag{10}
\]

If $x \neq 1$, then from (10), $a = 0$. Since $b \neq 0$ (otherwise $f(s)$ would be reducible), condition (9) gives $x^2 = 1$ for all $x \in F, x \neq 0$.

In $\mathrm{GF}(2)$, there is no element $x \neq 0, 1$, so no contradiction arises. Indeed, for $F = \mathrm{GF}(2)$, the Hall quasifield is a field.

If $F$ contains an element $x \neq 0, 1$, then $a = 0$ and $x^2 = 1$ must hold for all non-zero $x$. The only field with this property is $\mathrm{GF}(3)$, and the only irreducible quadratic over $\mathrm{GF}(3)$ with $a = 0$ is $f(s) = s^2 + 1$.

For $F = \mathrm{GF}(3)$ with $f(s) = s^2 + 1$, since $x^{-1} = x$ for all $x \neq 0$, the multiplication simplifies to:
\[
(x + \lambda y)(z + \lambda t) = xz - yt(x^2 + 1) + \lambda(yz - xt),
\]
which can be verified to be associative by direct computation (see Exercise 9.2). $\square$
