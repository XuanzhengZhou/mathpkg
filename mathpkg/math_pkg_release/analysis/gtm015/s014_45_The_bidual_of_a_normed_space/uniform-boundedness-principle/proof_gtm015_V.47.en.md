---
role: proof
locale: en
of_concept: uniform-boundedness-principle
source_book: gtm015
source_chapter: "V"
source_section: "47"
---

# Proof of the Uniform Boundedness Principle

By assumption, the family $(T_i)_{i \in I}$ is pointwise bounded; we wish to show that the family is uniformly bounded on the closed unit ball of $E$.

For each $i \in I$ define $f_i: E \to \mathbb{R}$ by the formula $f_i(x) = \|T_i x\|$; $f_i$ is continuous, by the continuity of $T_i$ and the continuity of the norm in $E_i$ (16.4). By Theorem 46.7 (uniform boundedness on an open set in a Baire space), there exist a nonempty open set $U$ in $E$ and a constant $M$, such that $f_i(x) \leq M$ for all $i \in I$ and $x \in U$. We can suppose $U$ is an open ball, say $U = \{x : \|x - a\| < r\}$ for suitable $a \in E$ and $r > 0$. Then

$$\|x - a\| < r \implies \|T_i x\| \leq M \quad \text{for all } i \in I. \qquad (*)$$

The proof will be concluded by showing that $\|T_i\| \leq 2M/r$ for all $i \in I$. Fix $i \in I$. Given any $y \in E$ with $\|y\| < 1$, it is to be shown that $\|T_i y\| \leq 2M/r$. Set $x = a + ry$; clearly $x \in U$, therefore $\|T_i x\| \leq M$ by $(*)$, i.e., $\|T_i a + r(T_i y)\| \leq M$. On the other hand $a \in U$, therefore $\|T_i a\| \leq M$. Then

$$\|r(T_i y)\| = \|T_i a + r(T_i y) - T_i a\| \leq \|T_i a + r(T_i y)\| + \|T_i a\| \leq M + M = 2M,$$

so $\|T_i y\| \leq 2M/r$. Since $y$ was arbitrary with $\|y\| < 1$, we obtain $\|T_i\| \leq 2M/r$ for all $i \in I$. Thus the family is uniformly bounded. $\square$
