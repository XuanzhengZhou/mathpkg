---
role: proof
locale: en
of_concept: potential-with-support-in-union
source_book: gtm040
source_chapter: "9"
source_section: "2"
---

For existence, let $x$ be a function that is 1 on $E$ and 0 on $F$, and set $h = B^{E \cup F} x$. By Proposition 9-43, conditions (1) and (3) are satisfied and $f$ has support in $E \cup F$. For condition (2), note that if $i \in E$, then $f_i$ is the probability of hitting $F$ before returning to $E$ (since $x$ is 1 on $E$ and 0 on $F$, the hitting matrix $B^{E \cup F}$ gives the exit distribution). Similarly, if $i \in F$, then $-f_i$ is the probability of hitting $E$ before returning to $F$.

For uniqueness, suppose $x$ satisfies (1), (2), and (3). Then by (3), $x = g + c1$ where $g$ is a potential. By (2), $(I - P)g = (I - P)x$ vanishes outside $E \cup F$, so $g$ has support in $E \cup F$. Hence $g = B^{E \cup F}g$. Therefore,
$$B^{E \cup F}x = B^{E \cup F}g + B^{E \cup F}(c1) = g + c1 = x,$$
and $x$ is uniquely determined by its values on $E \cup F$, which are fixed by condition (1).
