---
role: proof
locale: en
of_concept: ptr-addition-and-multiplication-are-loops
source_book: gtm006
source_chapter: "5"
source_section: "4"
---

**Proof.**

**(i) Addition.** For any $a \in R$, $0 + a = T(1, 0, a) = a$ and $a + 0 = T(1, a, 0) = a$ by conditions (A) and (B) of Theorem 5.1. Thus $(R, +)$ has $0$ as an identity.

The equation $a + x = b$ has a unique solution for $x$ if and only if $T(1, a, x) = b$ has a unique solution for $x$. But this is true by condition (D) of Theorem 5.1.

The equation $x + a = b$ has a unique solution for $x$ if and only if $T(1, x, a) = b$ has a unique solution for $x$. By condition (E) of Theorem 5.1, there exists a unique ordered pair $(x, y)$ such that $T(1, x, y) = b$ and $T(0, x, y) = a$. But, by (A), $T(0, x, y) = a$ has $y = a$ as a solution, and so there exists a unique $x$ such that $T(1, x, a) = b$. Therefore $(R, +)$ is a loop with identity $0$.

**(ii) Multiplication.** First we show $R^*$ is closed under multiplication. Suppose $x, y \in R^*$ but $xy = 0$. Then $T(x, y, 0) = T(0, y, 0) = 0$. Since by (C) of Theorem 5.1 the equation $T(u, y, 0) = T(0, y, 0)$ has a unique solution, and $u = 0$ is certainly a solution, the only solution to $T(u, y, 0) = T(u, 0, 0)$ is $u = 0$. But since $xy = 0$, $T(x, y, 0) = 0$ and, certainly, $T(x, 0, 0) = 0$. Thus $x = 0$, a contradiction since $x \in R^*$. Hence $R^*$ is closed under multiplication.

By (B) of Theorem 5.1, $1 \cdot x = T(1, x, 0) = x$ and $x \cdot 1 = T(x, 1, 0) = x$, so $1$ is an identity element for $(R^*, \cdot)$.

The equation $ax = b$ has a unique solution for $x$ if and only if $T(a, x, 0) = b$ has. By (E) of Theorem 5.1 there is a unique ordered pair $(x, y)$ such that
$$
T(a, x, y) = b, \qquad T(0, x, y) = 0.
$$
Since $T(0, x, y) = 0$ implies $y = 0$ by (A), we obtain that $T(a, x, 0) = b$ has a unique solution for $x$.

The equation $xa = b$ has a unique solution for $x$ if and only if $T(x, a, 0) = b$ has. By (C) of Theorem 5.1, since $a \neq 0$, we have $T(x, a, 0) = T(x, 0, b)$, and by (A), $T(x, 0, b) = b$ for all $x$. Thus $T(x, a, 0) = b$ has a unique solution for $x$, and $(R^*, \cdot)$ is a loop. $\square$
