---
role: proof
locale: en
of_concept: linear-form-module
source_book: gtm077
source_chapter: "I"
source_section: "1"
---

# Proof of Theorem 3: Range of Values of Linear Forms

Consider an arbitrary linear form in $n$ variables with integral coefficients, not all vanishing:

$$L(x_1, \ldots, x_n) = a_1 x_1 + a_2 x_2 + \cdots + a_n x_n, \qquad a_i \in \mathbb{Z}.$$

Let $M$ be the set of all values taken by $L$ as $x_1, \ldots, x_n$ run through all integers:

$$M = \{a_1 x_1 + \cdots + a_n x_n \mid x_i \in \mathbb{Z}\}.$$

$M$ is clearly a module: it is closed under addition and subtraction, and closed under multiplication by arbitrary integers (since $t \cdot L(x_1, \ldots, x_n) = L(tx_1, \ldots, tx_n) \in M$). By Theorem 2 (the Principal Module Theorem), $M$ consists precisely of all multiples of some non-negative integer $d$:

$$M = \{d \cdot x \mid x \in \mathbb{Z}\}.$$

We now determine $d$. Since each coefficient $a_i$ can be obtained by setting $x_i = 1$ and all other $x_j = 0$, we have $a_i \in M$, so $d \mid a_i$ for every $i$. Thus $d$ is a common divisor of $a_1, \ldots, a_n$.

Conversely, $d$ itself belongs to $M$, so there exist integers $y_1, \ldots, y_n$ such that

$$d = a_1 y_1 + a_2 y_2 + \cdots + a_n y_n.$$

Any common divisor $c$ of $a_1, \ldots, a_n$ divides the right-hand side, hence $c \mid d$. Therefore $d$ is the greatest common divisor of the coefficients:

$$d = (a_1, a_2, \ldots, a_n).$$

Thus the range of values of the linear form coincides with the set of all multiples of the GCD of its coefficients.

**Corollary (Solvability of linear Diophantine equations).** The equation

$$k = a_1 x_1 + a_2 x_2 + \cdots + a_n x_n$$

is solvable in integers $x_1, \ldots, x_n$ if and only if $(a_1, \ldots, a_n) \mid k$.

*Proof.* The condition is necessary because the left-hand side is always a multiple of $(a_1, \ldots, a_n)$. It is sufficient because $k$ belongs to $M$ precisely when it is a multiple of $d = (a_1, \ldots, a_n)$. $\square$
