---
role: proof
locale: en
of_concept: semialgebraic-function-piecewise-algebraic
source_book: gtm053
source_chapter: "4"
source_section: "4.8"
---

Suppose $g(x)$ is a semialgebraic function. By $o$-minimality, we may assume $\operatorname{Dom} g = (a, b)$, a single open interval (after partitioning the domain into finitely many intervals and points).

The graph of $g$ is a semialgebraic set, so it is defined by a Boolean combination of polynomial equations and inequalities over $R$. Among the defining conditions, at least one must be an equation $p(x, y) = 0$, because otherwise the graph would have interior (by the structure of inequalities), contradicting that it is the graph of a function.

Write $p(x, y)$ as $a_0(x)y^n + a_1(x)y^{n-1} + \cdots + a_n(x)$, for some $n > 0$ and $a_i(x) \in R[x]$. For each fixed $x$, $g(x)$ must satisfy $p(x, g(x)) = 0$, so $g(x)$ is one of the $n$ roots of the polynomial in $y$.

Since the roots of a polynomial vary continuously (in the sense of the ordering) as functions of the coefficients away from where the discriminant vanishes, and since the discriminant locus is a finite set of points (zeros of a polynomial in $x$), we can partition $(a, b)$ further so that on each subinterval the discriminant does not vanish. On such a subinterval, the real roots of $p(x, y)$ maintain a consistent ordering by size. By continuity, $g(x)$ must coincide with a fixed choice among these ordered roots (the greatest, second greatest, etc.) throughout the subinterval.
