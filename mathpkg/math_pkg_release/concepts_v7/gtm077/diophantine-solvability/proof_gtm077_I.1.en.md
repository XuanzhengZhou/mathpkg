---
role: proof
locale: en
of_concept: diophantine-solvability
source_book: gtm077
source_chapter: "I"
source_section: "1"
---

# Proof of Solvability of Linear Diophantine Equations (Theorem 3)

Consider an arbitrary linear form in $n$ variables with integer coefficients, not all vanishing:

$$L(x_1, \ldots, x_n) = a_1 x_1 + a_2 x_2 + \cdots + a_n x_n, \qquad a_i \in \mathbb{Z}.$$

Let $M$ be the set of all values taken by $L$ as $x_1, \ldots, x_n$ run through all integers:

$$M = \{a_1 x_1 + \cdots + a_n x_n \mid x_i \in \mathbb{Z}\}.$$

$M$ is clearly a module: it is closed under addition and under multiplication by arbitrary integers. By Theorem 2 (the Principal Module Theorem), $M$ consists precisely of all multiples of some non-negative integer $d$:

$$M = \{d \cdot x \mid x \in \mathbb{Z}\}.$$

We claim that $d$ is exactly the greatest common divisor of the coefficients $a_1, \ldots, a_n$.

First, since each $a_i$ (by setting $x_i = 1$ and all other $x_j = 0$) belongs to $M$, we have $d \mid a_i$ for all $i$, so $d$ is a common divisor. Conversely, any common divisor $c$ of $a_1, \ldots, a_n$ divides every linear combination $a_1 x_1 + \cdots + a_n x_n$, hence $c$ divides every element of $M$, in particular $c \mid d$. Therefore $d = (a_1, \ldots, a_n)$, the GCD.

Thus the range of values of $L$ is identical with the set of all multiples of $d = (a_1, \ldots, a_n)$:

$$L(x_1, \ldots, x_n) = d \cdot x.$$

As an immediate consequence, the Diophantine equation

$$k = a_1 x_1 + a_2 x_2 + \cdots + a_n x_n$$

is solvable in integers $x_1, \ldots, x_n$ if and only if $k \in M$, i.e., if and only if $d \mid k$, where $d = (a_1, \ldots, a_n)$.

In particular, for two variables, the equation $ax + by = k$ is solvable if and only if $(a, b) \mid k$.
