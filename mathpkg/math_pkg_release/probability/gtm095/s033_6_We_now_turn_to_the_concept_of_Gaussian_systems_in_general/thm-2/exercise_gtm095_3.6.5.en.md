---
role: exercise
locale: en
chapter: "3"
section: "6"
exercise_number: 5
---

# Exercise 5

Let $F_n \Rightarrow F$ and let $F$ be continuous. Show that in this case $F_n(x)$ converges uniformly to $F(x)$:

$$\sup_{x \in R} |F_n(x) - F(x)| \to 0, \qquad n \to \infty.$$

*Hint.* Since $F$ is continuous, every point $x \in R$ is a continuity point, so $F_n(x) \to F(x)$ pointwise. To upgrade to uniform convergence, use the fact that $F$ is a distribution function (hence $F(-\infty) = 0$, $F(+\infty) = 1$) and is uniformly continuous on any compact interval. For any $\varepsilon > 0$, choose $M$ large enough so that $F(-M) < \varepsilon$ and $F(M) > 1 - \varepsilon$. On $[-M, M]$, use a finite covering argument with the pointwise convergence at a dense set of points. Outside $[-M, M]$, bound the difference by $\varepsilon$ using the tail behavior.
