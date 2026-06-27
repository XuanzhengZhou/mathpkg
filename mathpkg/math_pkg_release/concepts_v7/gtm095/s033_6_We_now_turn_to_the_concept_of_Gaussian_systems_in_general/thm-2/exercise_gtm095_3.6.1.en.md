---
role: exercise
locale: en
chapter: "3"
section: "6"
exercise_number: 1
---

# Exercise 1

Let us say that a function $F = F(x)$, defined on $R^m$, is continuous at $x \in R^m$ provided that, for every $\varepsilon > 0$, there is a $\delta > 0$ such that $|F(x) - F(y)| < \varepsilon$ for all $y \in R^m$ that satisfy

$$x - \delta e < y < x + \delta e,$$

where $e = (1, \ldots, 1) \in R^m$. Let us say that a sequence of distribution functions $\{F_n\}$ converges in general to the distribution function $F$ ($F_n \Rightarrow F$) if $F_n(x) \rightarrow F(x)$ for all points $x \in R^m$ at which $F = F(x)$ is continuous.

Show that the conclusion of Theorem 2 remains valid for $R^m$, $m > 1$. (See Remark 1 on Theorem 1.)

*Hint.* The proof for $R^m$ follows the same strategy as for $R$. The key step is to show that the class of "elementary" sets $(-\infty, x_1] \times \cdots \times (-\infty, x_m]$ (or equivalently, half-open rectangles with vertices at continuity points of $F$) is a convergence-determining class. Any open set in $R^m$ can be approximated by finite unions of such rectangles, similarly to how open sets in $R$ are countable unions of intervals.
