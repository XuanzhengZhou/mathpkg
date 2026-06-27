---
role: proof
locale: en
of_concept: rho-defines-a-metric-on-c-g-omega
source_book: gtm011
source_chapter: "VII"
source_section: "1"
---

It is clear that $\rho(f, g) = \rho(g, f)$. Also, since each $\rho_n$ satisfies the triangle inequality, the preceding lemma can be used to show that $\rho$ satisfies the triangle inequality. Finally, the fact that $G = \bigcup_{n=1}^{\infty} K_n$ gives that $f = g$ whenever $\rho(f, g) = 0$.

[The "preceding lemma" referred to is: if $d_n$ is a family of pseudometrics on a set $X$ and $\varphi(t) = t/(1+t)$, then the sum $\sum (1/2)^n \varphi(d_n(x,y))$ is a metric provided the $d_n$ separate points. The key point is that $\varphi$ is increasing, subadditive ($\varphi(s+t) \leq \varphi(s) + \varphi(t)$ for $s,t \geq 0$), and satisfies $\varphi(t) = 0$ iff $t = 0$.]
