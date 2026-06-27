---
role: proof
locale: en
of_concept: initial-object-via-limit-of-identity
source_book: gtm005
source_chapter: "X"
source_section: "1. Adjoints and Limits"
---

Since $\lambda$ is a cone, the triangles

\[
\begin{CD}
d @= d @= d \\
@V{\lambda_d}VV @V{\lambda_{Fi}}VV @V{\lambda_c}VV \\
d @>Fi>> Fi @>f>> c
\end{CD}
\]

commute for each $i \in J$ and each arrow $f$ in $C$. But $\lambda F$ is a limiting cone, so the first two triangles prove $\lambda_d = 1_d$. Then by the third triangle, $f = \lambda_c$. Thus there is a unique arrow $f = \lambda_c$ from $d$ to each object $c \in C$, and $d$ is indeed initial in $C$.
