---
role: proof
locale: en
of_concept: complete-mols-implies-ptr
source_book: gtm006
source_chapter: "5"
source_section: "5. Latin Squares"
---

**Proof.** We verify that the ternary operation $T$ defined above satisfies the axioms (A), (B), (D), and (E) of Theorem 5.1. By Theorem 5.4, this suffices to show that $(R,T)$ is a planar ternary ring.

**(A)** $T(x, 0, c) = c$ for all $x, c$. This holds because all squares $\{x\}$ are in normal form, so each has $(0, 1, \dots, n-1)$ as its top row (row $0$). For $x = 0$, we have $T(0, 0, c) = c$ by definition. For $x \neq 0$, the entry in row $0$, column $c$ of $\{x\}$ is $c$.

**(B)** $T(a, 1, 0) = a$ because $\{a\}$ is the square with $a$ in the $(1,0)$-position by our labeling convention. Also $T(1, a, 0) = a$ since $\{1\}$ has $(0, 1, \dots, n-1)^\top$ (i.e., $0,1,\dots,n-1$ read down) as its left column, meaning that the entry in row $a$, column $0$ of $\{1\}$ is $a$.

**(D)** For $a \neq 0$ and any given $b, c$, the equation $T(a, b, x) = c$ has a unique solution $x$. This follows because every row of the Latin square $\{a\}$ contains each element of $R$ exactly once, so for fixed $a$ and row $b$, the map $x \mapsto T(a, b, x)$ is a bijection. For $a = 0$, $T(0, b, x) = x$, so $x = c$ is the unique solution. (Together with the corresponding property for columns, this establishes the Latin square properties used in the definition.)

**(E)** The remaining axiom (E) of Theorem 5.1 states that for $x \neq y$, the system
$$T(x, a, b) = T(y, a, b)$$
has a unique solution $a$. This follows from the orthogonality of the squares $\{x\}$ and $\{y\}$ for $x \neq y$. When the two Latin squares are superimposed, orthogonality implies that every ordered pair occurs exactly once. In particular, the ordered pair $(u, u)$ occurs exactly once, which means there is exactly one position where $\{x\}$ and $\{y\}$ have the same entry—this determines $a$. The corresponding statement for $b$ follows similarly from the Latin square column property.

Thus $(R, T)$ satisfies all required axioms and is a planar ternary ring.
