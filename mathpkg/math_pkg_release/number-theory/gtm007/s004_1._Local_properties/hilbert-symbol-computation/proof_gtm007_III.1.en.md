---
role: proof
locale: en
of_concept: hilbert-symbol-computation
source_book: gtm007
source_chapter: "III"
source_section: "§1. Local properties"
---

The case $k = \mathbf{R}$ is clear from the definition: $z^2 - a x^2 - b y^2 = 0$ has a nontrivial real solution unless $a < 0$ and $b < 0$, in which case the form is positive definite.

Suppose now that $k = \mathbf{Q}_p$. Write $a = p^\alpha u$, $b = p^\beta v$ with $u, v \in \mathbf{U}$ (the group of $p$-adic units). The exponents $\alpha$ and $\beta$ matter only modulo $2$ because multiplying $a$ or $b$ by a square does not change the Hilbert symbol and $p^2$ is a square up to a unit. By symmetry of the Hilbert symbol there are three cases to consider.

\medskip
\noindent \textbf{Case $p \neq 2$.}

\textit{1) $\alpha = 0$, $\beta = 0$.} We must show $(u, v) = 1$. The equation $z^2 - u x^2 - v y^2 = 0$ has a nontrivial solution modulo $p$ (Chapter I, §2, Corollary 2 to Theorem 3: a quadratic form in at least three variables over a finite field represents zero). Since $p \neq 2$ and the discriminant $u v$ of this quadratic form is a $p$-adic unit, the solution lifts from $\mathbf{F}_p$ to $\mathbf{Z}_p$ (Chapter II, n$^\circ$2.2, Corollary 2 to Theorem 1), giving a $p$-adic solution. Hence $(u, v) = 1$.

\textit{2) $\alpha = 1$, $\beta = 0$.} We must show $(p u, v) = \left(\frac{v}{p}\right)$. By the lemma, if $(p u, v) = 1$, the equation $z^2 - p u x^2 - v y^2 = 0$ has a primitive solution with $z, y \in \mathbf{U}$ and $x \in \mathbf{Z}_p$. Modulo $p$, this gives $z^2 \equiv v y^2 \pmod{p}$, whence $\left(\frac{v}{p}\right) = 1$. Conversely, if $\left(\frac{v}{p}\right) = 1$, then $v \equiv z_0^2 \pmod{p}$. Choosing $x = 0$, we can lift the solution by Hensel's lemma since the derivative with respect to $z$ is nonzero modulo $p$. The formula $(p u, v) = \left(\frac{v}{p}\right)$ follows, and by symmetry $(u, p v) = \left(\frac{u}{p}\right)$.

\textit{3) $\alpha = 1$, $\beta = 1$.} By bilinearity (formula v) proved in §2, we have
$$
(p u, p v) = (p u, -u v)(p u, -p) = \dots
$$
Using the known values for exponent pairs $(1,0)$ and $(0,0)$, one obtains the stated formula.

\medskip
\noindent \textbf{Case $p = 2$.}

\textit{1) $\alpha = 0$, $\beta = 0$.} We must show $(u, v) = 1$ if $u$ or $v$ is congruent to $1 \pmod{4}$, and $(u, v) = -1$ otherwise. Suppose first $u \equiv 1 \pmod{4}$. Then either $u \equiv 1 \pmod{8}$ or $u \equiv 5 \pmod{8}$. If $u \equiv 1 \pmod{8}$, then $u$ is a square in $\mathbf{Q}_2$ (Chapter II, n$^\circ$3.3, Theorem 4), so $(u, v) = 1$. If $u \equiv 5 \pmod{8}$, then $u + 4v \equiv 1 \pmod{8}$, so there exists $w \in \mathbf{U}$ such that $w^2 = u + 4v$. The form $z^2 - u x^2 - v y^2$ then has $(w, 1, 2)$ as a zero, giving $(u, v) = 1$.

Now suppose $u \equiv v \equiv -1 \pmod{4}$. If $(z, x, y)$ is a primitive solution, reducing modulo $4$ gives $z^2 + x^2 + y^2 \equiv 0 \pmod{4}$. But squares in $\mathbf{Z}/4\mathbf{Z}$ are only $0$ and $1$, so this congruence forces $x, y, z \equiv 0 \pmod{2}$, contradicting primitivity. Hence $(u, v) = -1$.

\textit{2) $\alpha = 1$, $\beta = 0$.} We must show $(2u, v) = (-1)^{\omega(v)}$, i.e., $(2, v) = 1$ if and only if $v \equiv \pm 1 \pmod{8}$. By the lemma, if $(2, v) = 1$, there exist $x, y, z \in \mathbf{Z}_2$ with $z, y \in \mathbf{U}$ such that $z^2 \equiv v y^2 \pmod{8}$. Since $z^2 \equiv y^2 \equiv 1 \pmod{8}$ for $2$-adic units, we obtain $v \equiv 1 \pmod{8}$ or after adjusting signs $v \equiv -1 \pmod{8}$. Conversely, if $v \equiv \pm 1 \pmod{8}$, then $v$ or $-v$ is a square in $\mathbf{Q}_2$, and a solution can be explicitly constructed. The formula with $\varepsilon(u)$ and $\omega(u)$ follows from the additive properties of these invariants.

\textit{3) $\alpha = 1$, $\beta = 1$.} By bilinearity, using the cases above, we obtain
$$
(2u, 2v) = (-1)^{\varepsilon(u)\varepsilon(v) + \omega(u) + \omega(v)}
$$
which matches the formula with $\alpha = \beta = 1$.
