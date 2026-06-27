---
role: proof
locale: en
of_concept: union-intersection-of-algebraic-sets
source_book: gtm052
source_chapter: "I"
source_section: "§1"
---
If $Y_1 = Z(T_1)$ and $Y_2 = Z(T_2)$, then $Y_1 \cup Y_2 = Z(T_1 T_2)$, where $T_1 T_2$ denotes the set of all products of an element of $T_1$ by an element of $T_2$. Indeed, if $P \in Y_1 \cup Y_2$, then either $P \in Y_1$ or $P \in Y_2$, so $P$ is a zero of every polynomial in $T_1 T_2$. Conversely, if $P \in Z(T_1 T_2)$, and $P \notin Y_1$ say, then there is an $f \in T_1$ such that $f(P) \neq 0$. But for any $g \in T_2$, we have $(fg)(P) = 0$ by assumption, hence $g(P) = 0$ for all $g \in T_2$, so $P \in Y_2$.

If $Y_i = Z(T_i)$ is any family of algebraic sets, then $\bigcap Y_i = Z(\bigcup T_i)$. Clearly $P \in \bigcap Y_i$ if and only if $f(P) = 0$ for all $f \in T_i$ and all $i$, which is equivalent to $f(P) = 0$ for all $f \in \bigcup T_i$.

The empty set is $Z(1)$ and the whole space is $Z(0)$.
