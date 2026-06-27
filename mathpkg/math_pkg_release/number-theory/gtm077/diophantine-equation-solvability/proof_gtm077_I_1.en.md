---
role: proof
locale: en
of_concept: diophantine-equation-solvability
source_book: gtm077
source_chapter: "I"
source_section: "1"
---

# Proof of Solvability of Linear Diophantine Equations

**Theorem (Corollary to Theorem 3).** The linear Diophantine equation in $n$ variables

$$k = a_1 x_1 + a_2 x_2 + \cdots + a_n x_n \qquad (a_i, k \in \mathbb{Z})$$

is solvable in integers $x_1, \ldots, x_n$ if and only if the greatest common divisor of the coefficients divides $k$:

$$(a_1, a_2, \ldots, a_n) \mid k.$$

*Proof.* Let $d = (a_1, a_2, \ldots, a_n)$. The set of all values taken by the linear form $L(x_1, \ldots, x_n) = a_1 x_1 + \cdots + a_n x_n$ as $x_1, \ldots, x_n$ run through the integers forms a module $M$. By Theorem 2 and Theorem 3, this module consists precisely of all multiples of $d$.

Therefore, the equation $L(x_1, \ldots, x_n) = k$ has a solution if and only if $k$ belongs to $M$, which is equivalent to $d \mid k$.

**Necessity.** If integers $x_1, \ldots, x_n$ satisfy the equation, then $k$ is expressed as a linear combination of $a_1, \ldots, a_n$. Since $d$ divides each $a_i$, it divides the linear combination, hence $d \mid k$.

**Sufficiency.** If $d \mid k$, write $k = dm$ for some integer $m$. Since $d \in M$, there exist integers $y_1, \ldots, y_n$ such that $d = a_1 y_1 + \cdots + a_n y_n$. Multiplying by $m$, we obtain

$$k = a_1 (my_1) + \cdots + a_n (my_n),$$

so $x_i = my_i$ is an integer solution. $\square$

**Special case $n = 2$.** The equation $ax + by = k$ is solvable in integers if and only if $(a, b) \mid k$. In particular, the equation $ax + by = 1$ has a solution if and only if $(a, b) = 1$, i.e., $a$ and $b$ are coprime.
