---
role: proof
locale: en
of_concept: recursive-iff-diophantine
source_book: gtm022
source_chapter: "10"
source_section: "1"
---

The proof consists of two directions.

**Direction 1: Diophantine $\Rightarrow$ Recursive.**

Suppose $f: \mathbb{N}^n \to \mathbb{N}$ is diophantine. Then there exist polynomials $P, Q$ in $n + 1 + m$ variables with coefficients in $\mathbb{N}$ such that

$$y = f(x_1, \ldots, x_n) \text{ iff } (\exists t_1, \ldots, t_m)\bigl(P(x_1, \ldots, x_n, y, t_1, \ldots, t_m) = Q(x_1, \ldots, x_n, y, t_1, \ldots, t_m)\bigr).$$

Denote the sequence number function by $S(z, i)$. By Lemma 6.5 of Chapter IX, for every choice of $y, t_1, \ldots, t_m$ there exists a value $u$ such that

$$S(u, 0) = y,\quad S(u, 1) = t_1,\quad \ldots,\quad S(u, m) = t_m.$$

Since $f$ is a function, there is exactly one $y$ for which $P = Q$. Hence

$$\begin{aligned}
f(x_1, \ldots, x_n) = y = S\Bigl(\min_u\bigl(&P(x_1, \ldots, x_n, S(u, 0), \ldots, S(u, m)) \\
&= Q(x_1, \ldots, x_n, S(u, 0), \ldots, S(u, m))\bigr), 0\Bigr).
\end{aligned}$$

By Exercise 1.4 (the pairing function $\ell, r$ and their well-definedness) and Theorem 1.2 (algebraic characterisation of recursive functions), this expresses $f$ in terms of composition and minimalisation of recursive functions, so $f$ is recursive. $\square$

**Direction 2: Recursive $\Rightarrow$ Diophantine.**

Using Theorem 1.2, it suffices to prove:
1. Every initial function in $I$ is diophantine.
2. The class of diophantine functions is closed under composition, primitive recursion, and minimalisation.

*Initial functions are diophantine.* See Exercise 1.10.

*Closure under composition.* If $f_1, \ldots, f_n$ and $g$ are diophantine, and

$$h(x_1, \ldots, x_m) = g(f_1(x_1, \ldots, x_m), \ldots, f_n(x_1, \ldots, x_m)),$$

then $h$ is diophantine because

$$y = h(x_1, \ldots, x_m) \text{ iff } (\exists t_1, \ldots, t_n)\bigl(t_1 = f_1(x_1, \ldots, x_m) \text{ and } \ldots$$
$$\text{and } t_n = f_n(x_1, \ldots, x_m) \text{ and } y = g(t_1, \ldots, t_n)\bigr),$$

and by Exercises 1.11 and 1.12, the conjunction of diophantine relations is diophantine.

*Closure under primitive recursion.* If $f: \mathbb{N}^n \to \mathbb{N}$ and $g: \mathbb{N}^{n+2} \to \mathbb{N}$ are diophantine and

$$h(x_1, \ldots, x_n, 0) = f(x_1, \ldots, x_n),$$
$$h(x_1, \ldots, x_n, z+1) = g(z, h(x_1, \ldots, x_n, z), x_1, \ldots, x_n),$$

then $y = h(x_1, \ldots, x_n, z)$ if and only if

$$(\exists u)\Bigl((\exists v)(v = S(u, 0) \land v = f(x_1, \ldots, x_n)) \land (\forall t \leqslant z)\bigl(t = z \lor (\exists w)(w = S(u, t+1) \land$$
$$w = g(t, S(u, t), x_1, \ldots, x_n))\bigr) \land y = S(u, z)\Bigr).$$

By Exercises 1.11 and 1.12, this shows $h$ is diophantine.

*Closure under minimalisation.* If $f, g$ are diophantine and

$$h(x_1, \ldots, x_n) = \min_y\bigl(f(x_1, \ldots, x_n, y) = g(x_1, \ldots, x_n, y)\bigr),$$

then $y = h(x_1, \ldots, x_n)$ if and only if

$$(\exists z)\bigl(z = f(x_1, \ldots, x_n, y) \land z = g(x_1, \ldots, x_n, y)\bigr) \land$$
$$(\forall t \leqslant y)\Bigl(t = y \lor (\exists u)(\exists v)\bigl(u = f(x_1, \ldots, x_n, t) \land v = g(x_1, \ldots, x_n, t) \land$$
$$(u < v \lor v < u)\bigr)\Bigr),$$

showing that $h$ is diophantine. $\square$

Since every recursive function can be obtained from $I$ by the operations (Theorem 1.2), and $I$ is diophantine while the operations preserve diophantineness, every recursive function is diophantine. Together with the first direction, we obtain the equivalence.
