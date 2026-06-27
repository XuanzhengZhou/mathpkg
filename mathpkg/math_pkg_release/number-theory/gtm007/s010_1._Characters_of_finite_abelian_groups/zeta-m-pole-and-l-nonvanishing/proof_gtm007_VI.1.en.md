---
role: proof
locale: en
of_concept: zeta-m-pole-and-l-nonvanishing
source_book: gtm007
source_chapter: "VI"
source_section: "§1. Characters of finite abelian groups"
---

\textbf{(b) $\Rightarrow$ (a):} If $L(1,\chi) \neq 0$ for all $\chi \neq 1$, then the only pole among the factors of $\zeta_m$ comes from $L(s,1)$, which has a simple pole at $s=1$ (Proposition 11). Hence $\zeta_m$ has a simple pole at $s=1$.

\textbf{(a) $\Rightarrow$ (b):} Suppose for contradiction that $L(1,\chi) = 0$ for some $\chi \neq 1$. Then $\zeta_m$ would be holomorphic at $s=1$, hence in the entire half-plane $R(s) > 0$ (Propositions 11, 12). By Lemma 6, the local $p$-th factor of $\zeta_m$ is $(1-p^{-f(p)s})^{-g(p)}$, whose series expansion has positive coefficients. Thus $\zeta_m$ is a Dirichlet series with positive coefficients. By Proposition 7 (Landau\'s theorem), its domain of convergence would extend to $R(s) > 0$.

But the coefficients of $\zeta_m$ dominate those of $\sum_{(n,m)=1} n^{-\phi(m)s}$ (since each prime factor contributes $(1+p^{-f(p)s}+\cdots)^{g(p)}$ which dominates $1+p^{-\phi(m)s}+\cdots$). The latter series diverges at $s = 1/\phi(m)$, contradicting convergence for all $s > 0$. Hence $L(1,\chi) \neq 0$.
