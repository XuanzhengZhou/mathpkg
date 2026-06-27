---
role: exercise
locale: en
chapter: "25"
section: "25.1"
exercise_number: 1
---
# Exercise 25.1

Let $\Omega$ be the cylindrical domain $\{|z| < 1\} \times \mathbb{C}$ in $\mathbb{C}^2$. Let $a_1(z), a_2(z), \ldots, a_n(z)$ be analytic functions on $\{|z| < 1\}$ and let $E$ be the subset of $\Omega$ given by

$$w^n + a_1(z) w^{n-1} + a_2(z) w^{n-2} + \cdots + a_n(z) = 0.$$

Prove that $E$ is pseudoconcave in $\Omega$.

**Hint:** Model your proof on Example 25.1. For a point $(z, w) \in \Omega$ such that $P(z, w) = w^n + a_1(z) w^{n-1} + \cdots + a_n(z) \neq 0$, factor $P(z, w) = \prod_{j=1}^{n} (w - f_j(z))$ (locally, the roots $f_j(z)$ are analytic functions of $z$ away from the discriminant locus). Then consider the plurisubharmonic function

$$\psi(z, w) = -\log|P(z, w)| = -\sum_{j=1}^{n} \log|w - f_j(z)|$$

on $\Omega \setminus E$. Since each term $-\log|w - f_j(z)|$ is plurisubharmonic (as $(w - f_j(z))^{-1}$ is analytic), $\psi$ is a plurisubharmonic exhaustion function for $\Omega \setminus E$, establishing that $\Omega \setminus E$ is pseudoconvex, and hence $E$ is pseudoconcave in $\Omega$.
