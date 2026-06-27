---
role: proof
locale: en
of_concept: lindenbaum-is-all-truth-functions
source_book: gtm022
source_chapter: "III"
source_section: "3"
---

By induction on $n$. For $n = 0$, the constant functions $0 = \bar{F}$ and $1 = \overline{F \Rightarrow F}$ are in $L(X_n)$. Assume the result for $n-1$. For any truth function $f(x_1, \ldots, x_n)$, define $g(x_1, \ldots, x_{n-1}) = f(x_1, \ldots, x_{n-1}, 0)$ and $h(x_1, \ldots, x_{n-1}) = f(x_1, \ldots, x_{n-1}, 1)$. By induction, $g, h \in L(X_{n-1}) \subseteq L(X_n)$. Then $f = (\bar{x}_n \wedge g) \vee (x_n \wedge h)$, where $\bar{x}_n = \sim x_n$, is in $L(X_n)$ since $L(X_n)$ is closed under Boolean operations.
