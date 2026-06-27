---
role: proof
locale: en
of_concept: dual-transformation-existence
source_book: gtm036
source_chapter: "21"
source_section: "1"
---

If $T$ is $w(E,F)$-$w(G,H)$ continuous, then for each $f \in H$ the map $x \mapsto \langle T(x), f \rangle$ is a $w(E,F)$-continuous linear functional on $E$. Hence, by the representation theorem 16.2 for $w(E,F)$-continuous linear functionals, there exists an element $f^* \in F$ such that $\langle T(x), f \rangle = \langle x, f^* \rangle$ for all $x \in E$. Moreover, the element $f^*$ is unique if and only if $E$ distinguishes points of $F$.

A dual $T'$ of $T$ may then be constructed as follows: for each member $f$ of a Hamel base $B$ for $H$, let $T'(f)$ be an element $f^* \in F$ such that $\langle T(x), f \rangle = \langle x, f^* \rangle$ for all $x \in E$, and extend $T'$ linearly to all of $H$ by assigning the values so determined on $B$. It follows without difficulty that $T'$ is a dual for $T$, and that $T'$ is unique if and only if $E$ distinguishes points of $F$.

Conversely, if $T$ has a dual $T'$, then for each $h \in H$, the linear functional $x \mapsto \langle T(x), h \rangle = \langle x, T'(h) \rangle$ is $w(E,F)$-continuous on $E$, which implies that $T$ is $w(E,F)$-$w(G,H)$ continuous. Also, since $T'$ has a dual, the transformation $T'$ is necessarily $w(H,G)$-$w(F,E)$ continuous.
