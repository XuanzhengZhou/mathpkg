---
role: proof
locale: en
of_concept: hall-quasifield-equation-solvability
source_book: gtm006
source_chapter: "IX"
source_section: "2"
---

We need to solve the equations:

$$(x + \lambda y)(z + \lambda t) = p + \lambda q.$$

**Case 1: $y \neq 0$.** Using the multiplication formula (2), we have:

$$xz - y^{-1}tf(x) + \lambda(yz - xt + at) = p + \lambda q.$$

Equating components yields the system:

\begin{align}
xz - y^{-1}tf(x) &= p, \\
yz - xt + at &= q.
\end{align}

Multiplying the first equation by $y$ and rearranging:

$$xyz - tf(x) = py.$$

Now $f(x) = x^2 - ax - b$, so $xyz - t(x^2 - ax - b) = py$, or:

$$-tx^2 + (yz + at)x + bt = py.$$

This is equivalent to the linear system obtained by multiplying the first equation of the original pair by $y$, the second by $x$, and subtracting:

$$bt = py - qx.$$

Combining with the second equation, we obtain the linear system:

\begin{align}
py - qx &= bt, \\
zy - tx &= q - at.
\end{align}

If $t = 0$, the system has unique solution $y = qz^{-1}$, $x = pz^{-1}$, with $y = 0$ iff $q = 0$.

If $t \neq 0$, multiply the second equation by $qt^{-1}$ and subtract from the first:

$$y(p - qt^{-1}z) = bt - q^2t^{-1} + aq.$$

Simplifying the right-hand side:

$$bt - q^2t^{-1} + aq = -t^{-1}(q^2 - aqt - bt^2) = -t^{-1}t^2\left(\left(\frac{q}{t}\right)^2 - a\left(\frac{q}{t}\right) - b\right) = -t\,f\!\left(\frac{q}{t}\right).$$

Thus:

$$y(pt - qz) = -t^2\,f\!\left(\frac{q}{t}\right).$$

Since $f(s)$ is irreducible over $F$, $f(qt^{-1}) \neq 0$ for all $q, t \in F$ with $t \neq 0$. Hence the right-hand side is non-zero.

If $pt - qz = 0$ (i.e., $p = 0$ and $z = 0$, or $z \neq 0$ and $pz^{-1} = qt^{-1}$), the equations are inconsistent: no solution with $y \neq 0$.

If $pt - qz \neq 0$, then:

$$y = \frac{-t^2\,f(qt^{-1})}{pt - qz} \neq 0,$$

and $x$ is uniquely determined from the linear system.

**Case 2: $y = 0$.** Then the equation becomes:

$$x(z + \lambda t) = p + \lambda q,$$

which by formula (3) gives $xz = p$ and $xt = q$. This has a solution exactly when $z \neq 0$ or $t \neq 0$ (given that $(z, t) \neq (0, 0)$), with $x = pz^{-1}$ if $z \neq 0$, and consistency requires $pt = qz$.

Thus, in all cases where a solution exists, it is unique. The construction shows $H$ is a weak quasifield, and since $F$ is contained in the kernel of $H$ with $H$ finite-dimensional over its kernel, $H$ is a quasifield.
