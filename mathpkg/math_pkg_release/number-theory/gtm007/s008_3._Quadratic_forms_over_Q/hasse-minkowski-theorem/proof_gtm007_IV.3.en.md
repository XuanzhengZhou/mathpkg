---
role: proof
locale: en
of_concept: hasse-minkowski-theorem
source_book: gtm007
source_chapter: "IV"
source_section: "3"
---

The necessity is obvious. We prove sufficiency by induction on the rank $n$ of $f$.

\textbf{i) The case $n=1$.} Trivial: $f = aX^2$ represents $0$ in $\mathbf{Q}$ iff it represents $0$ in all $\mathbf{Q}_v$, since both conditions are equivalent to $a=0$. For nondegenerate forms ($a \neq 0$), neither condition holds.

\textbf{ii) The case $n=2$.} Write $f = aX^2 + bY^2$. The form represents $0$ in $\mathbf{Q}_v$ iff $-ab$ is a square in $\mathbf{Q}_v$, i.e., $(a, b)_v = 1$ for all $v$. By the Hilbert product formula $\prod_v (a,b)_v = 1$, this implies $(a,b)_\infty = 1$, so $-ab > 0$ in $\mathbf{R}$ and $-ab$ is a square in $\mathbf{Q}$.

\textbf{iii) The case $n=3$ (Legendre).} We have $f = X_1^2 - aX_2^2 - bX_3^2$. Multiplying $a, b$ by squares we may assume $a,b$ are square-free integers with $|a| \leq |b|$. We use induction on $m = |a| + |b|$. If $m=2$, then $f = X_1^2 \pm X_2^2 \pm X_3^2$; the case $X_1^2 + X_2^2 + X_3^2$ is excluded because $f_\infty$ represents $0$; in the other cases $f$ represents zero.

Suppose $m > 2$ ($|b| \geq 2$) and write $b = \pm p_1 \cdots p_k$ with distinct primes. Let $p$ be one of the $p_i$. We prove that $a$ is a square modulo $p$. This is clear if $a \equiv 0 \pmod{p}$. Otherwise $a$ is a $p$-adic unit. By hypothesis there exists a primitive $(x,y,z) \in \mathbf{Q}_p^3$ with $z^2 - ax^2 - by^2 = 0$. Modulo $p$, $z^2 - ax^2 \equiv 0$. If $x \equiv 0 \pmod{p}$, then also $z \equiv 0 \pmod{p}$, forcing $by^2$ divisible by $p^2$; since $v_p(b) = 1$, this gives $y \equiv 0 \pmod{p}$, contradicting primitivity. Hence $x \not\equiv 0 \pmod{p}$ and $a \equiv (z/x)^2 \pmod{p}$ is a square modulo $p$.

Thus $a$ is a square modulo every $p \mid b$, so $a$ is a square modulo $b$. We can write $a = t^2 - bb'$ with $t \in \mathbf{Z}$, and $|b'| < |b|$ by choosing $|t| \leq |b|/2$. Setting $X_1' = X_1 + tX_3$, we transform $f$ to a form with $a,b$ replaced by $a,b'$, reducing $m$. By induction, $f$ represents $0$.

\textbf{iv) The case $n=4$.} Write $f = aX_1^2 + bX_2^2 + cX_3^2 + dX_4^2$. Since $\prod_v (a,b)_v = \prod_v (c,d)_v = 1$, by Theorem 4 of Chapter III, §2.2, there exists $x \in \mathbf{Q}^*$ such that $(x, -ab)_v = (a,b)_v$ and $(x, -cd)_v = (c,d)_v$ for all $v \in V$. The forms $aX_1^2 + bX_2^2 - xZ^2$ and $cX_3^2 + dX_4^2 - xZ^2$ represent $0$ in each $\mathbf{Q}_v$, hence in $\mathbf{Q}$ by the $n=3$ case. Thus $x$ is represented by both $aX_1^2 + bX_2^2$ and $cX_3^2 + dX_4^2$, from which $f$ represents $0$.

\textbf{v) The case $n \geq 5$.} Write $f = h \oplus g$ with $h = a_1X_1^2 + a_2X_2^2$ and $g = -(a_3X_3^2 + \cdots + a_nX_n^2)$. Let $S$ be the finite subset of $V$ consisting of $\infty$, $2$, and those primes $p$ with $v_p(a_i) \neq 0$ for some $i \geq 3$. For $v \in S$, since $f_v$ represents $0$, there exists $a_v \in \mathbf{Q}_v^*$ represented in $\mathbf{Q}_v$ by both $h$ and $g$. The squares of $\mathbf{Q}_v^*$ form an open set; by the approximation theorem we can find $a \in \mathbf{Q}^*$ close to each $a_v$ in the $v$-adic topology, so that $a$ is represented by $h$ and $g$ in each $\mathbf{Q}_v$. The quadratic forms $h - aZ^2$ (rank 3) and $g + aZ^2$ (rank $n-1$) represent $0$ in each $\mathbf{Q}_v$. By induction (and the $n=3$ case for the first), they represent $0$ in $\mathbf{Q}$, so $a$ is represented by $h$ and $-a$ by $g$, hence $f$ represents $0$.

When $n=4$ and $d(f)=1$, we argue similarly, replacing the equality by $(-1, -1)_v = \varepsilon_v(f)$.

\textbf{Remarks.} (1) If $n=2$ and $f$ represents $0$ in all $\mathbf{Q}_v$ except a finite number, one can still conclude $f$ represents $0$ using the theorem on arithmetic progressions. (2) Theorem 8 does not extend to homogeneous polynomials of degree $\geq 3$; Selmer's counterexample $3X^3+4Y^3+5Z^3=0$ has a nontrivial solution in every $\mathbf{Q}_v$ but none in $\mathbf{Q}$.
