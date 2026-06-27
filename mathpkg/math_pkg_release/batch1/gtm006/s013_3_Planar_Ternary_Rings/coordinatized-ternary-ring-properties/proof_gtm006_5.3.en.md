---
role: proof
locale: en
of_concept: coordinatized-ternary-ring-properties
source_book: gtm006
source_chapter: "5"
source_section: "3"
---

**(A)** $T(0, b, c) = k$ implies $(b, c)$ is on the line joining $(0)$ to $(0, k)$. But $(b, c)$ is the intersection of the line joining $(0)$ to $(0, c)$ with the line joining $(\infty)$ to $(b, c)$. Thus, since the line joining $(b, c)$ to $(0)$ has a unique intersection with $l_1$, $c = k$ and $T(0, b, c) = c$. The equality $T(a, 0, c) = c$ follows by a similar argument with the roles of the coordinates interchanged.

**(B)** $T(a, 1, 0) = k$ implies that $(1, 0)$ is on $[a, k]$, i.e. $(1, 0)$ is on the line joining $(a)$ to $(0, k)$. But $(a)$ is the intersection of the line joining $(1, 0)$ to $(0, a)$ with $l_{\infty}$, and so, since the line joining $(1, 0)$ to $(a)$ intersects $l_1$ in a unique point, $(0, k) = (0, a)$ or $k = a$. Hence $T(a, 1, 0) = a$.

$T(1, a, 0) = k$ implies $(a, 0)$ is on the line joining $(1)$ to $(0, k)$. But $(a, 0)$ is the intersection of $l_2$ with the line joining $(1)$ to $(0, a)$. Thus $(0, a) = (0, k)$ and $T(1, a, 0) = a$.

**(C)** Let $a, b, c, d \in R$, $a \neq c$. Then there is a unique line joining $(a, b)$ to $(c, d)$. Since $a \neq c$, this line does not pass through $(\infty)$ and, hence, intersects $l_{\infty}$ in a unique point $(m)$ where $m \in R$. If this line also intersects $l_1$ in $(0, k)$ then $T(m, a, b) = T(m, c, d) = k$, and so since $(m)$ is unique, there is a unique $x \in R$ such that $T(x, a, b) = T(x, c, d)$.

**(D)** *[Proof truncated in source — the uniqueness of $x$ in $T(a,b,x)=c$ follows from the fact that given $a,b,c$, the horizontal line $[b]$ meets the vertical line through $(a)$ on $l_\infty$ in a unique point, which determines a unique intersection with $l_1$, yielding the unique $x$.]*

**(E)** *[Proof truncated in source — given $a,b,c,d \in R$ with $a \neq c$, the points $(a,b)$ and $(c,d)$ determine a unique line not passing through $(\infty)$. This line meets $l_\infty$ in a unique point $(m)$ and $l_1$ in $(0,k)$, yielding the unique solution $(x,y) = (m,k)$ such that $T(m,a,b)=k$ and $T(m,c,d)=k$. The formal statement: there exist unique $x,y \in R$ such that $T(a,x,y)=b$ and $T(c,x,y)=d$.]*
