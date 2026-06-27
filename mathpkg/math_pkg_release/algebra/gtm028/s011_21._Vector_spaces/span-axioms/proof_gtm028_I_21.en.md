---
role: proof
locale: en
of_concept: span-axioms
source_book: gtm028
source_chapter: "I"
source_section: "21"
---

Properties $(S_1)$ and $(S_3)$ are evident. Property $(S_2)$ follows from the fact that every element of $s(X)$ is a linear combination of a finite number of elements of $X$.

Since the span of a subspace $W$ is $W$ itself, $(S_4)$ holds: for any subset $X$, $s(X)$ is a subspace, and the span of a subspace is the subspace itself, hence $s(s(X)) = s(X)$.

Finally, to verify the exchange property $(S_5)$: the relation $y \in s(X, x)$ means that there exist elements $a, b_i$ of $F$ and $x_i$ of $X$ such that
$$y = ax + \sum_{i=1}^{n} b_i x_i.$$
We have $a \neq 0$ since $y \notin s(X)$ (otherwise $y$ could be expressed without $x$). Whence
$$x = a^{-1}y - \sum_{i=1}^{n} a^{-1}b_i x_i,$$
and therefore $x \in s(X, y)$.
