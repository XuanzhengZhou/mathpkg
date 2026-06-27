---
role: proof
locale: en
of_concept: zeta-function-pole-asymptotics
source_book: gtm007
source_chapter: "VI"
source_section: "§1. Characters of finite abelian groups"
---

Write
$$
\frac{1}{s-1} = \int_1^\infty t^{-s} dt = \sum_{n=1}^\infty \int_n^{n+1} t^{-s} dt.
$$
Then
$$
\zeta(s) - \frac{1}{s-1} = \sum_{n=1}^\infty \int_n^{n+1} (n^{-s} - t^{-s}) dt.
$$
Define $\phi_n(s) = \int_n^{n+1} (n^{-s} - t^{-s}) dt$. The derivative of $t \mapsto n^{-s} - t^{-s}$ with respect to $t$ is $s/t^{s+1}$, giving the bound $|\phi_n(s)| \leq |s|/n^{x+1}$ where $x = R(s)$. The series $\sum \phi_n(s)$ converges normally on compact subsets for $R(s) > 0$, proving $\phi(s)$ is holomorphic there.
