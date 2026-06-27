---
role: proof
locale: en
of_concept: union-and-intersection-of-algebraic-sets
source_book: gtm052
source_chapter: "I"
source_section: "1"
---

If $Y_1 = Z(T_1)$ and $Y_2 = Z(T_2)$, then $Y_1 \cup Y_2 = Z(T_1 T_2)$, where $T_1 T_2$ denotes the set of all products of an element of $T_1$ by an element of $T_2$. Indeed, if $P \in Y_1 \cup Y_2$, then either $P \in Y_1$ or $P \in Y_2$, so $P$ is a common zero of either $T_1$ or $T_2$, hence of $T_1 T_2$. Conversely, if $P \in Z(T_1 T_2)$ but $P \notin Y_1$, then there exists $f \in T_1$ with $f(P) \neq 0$. But for all $g \in T_2$, $fg \in T_1 T_2$, so $(fg)(P) = f(P)g(P) = 0$, which implies $g(P) = 0$ for all $g \in T_2$, hence $P \in Y_2$. For the intersection, if $Y_\alpha = Z(T_\alpha)$ is any family of algebraic sets, then $\bigcap_\alpha Y_\alpha = Z(\bigcup_\alpha T_\alpha)$, because $P$ belongs to the intersection if and only if $f(P) = 0$ for all $f \in T_\alpha$ and all $\alpha$, which means $f(P) = 0$ for all $f \in \bigcup_\alpha T_\alpha$. The empty set is $Z(1)$ and the whole space is $Z(0)$.
