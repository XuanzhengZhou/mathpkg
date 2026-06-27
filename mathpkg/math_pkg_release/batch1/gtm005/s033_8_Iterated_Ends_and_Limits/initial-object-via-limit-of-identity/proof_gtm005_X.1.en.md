---
role: proof
locale: en
of_concept: initial-object-via-limit-of-identity
source_book: gtm005
source_chapter: "X"
source_section: "1. Adjoints and Limits"
---

**Proof.** Since $\lambda$ is a cone, for each $i \in J$ and each arrow $f: d \to c$ in $C$, the triangles

$$\begin{CD}
d @>{\lambda_d}>> d \\
@V{\lambda_{Fi}}VV @VV{\lambda_{Fi}}V \\
Fi @= Fi
\end{CD}$$

and

$$\begin{CD}
d @>{f}>> c \\
@V{\lambda_c}VV @| \\
c @= c
\end{CD}$$

commute. But $\lambda F$ is a limiting cone; applying the first two triangles with the universal property of the limit yields $\lambda_d = 1_d$. Then by the third triangle, any arrow $f: d \to c$ must equal $\lambda_c$. Thus there is exactly one arrow $f = \lambda_c$ from $d$ to each object $c$, and $d$ is indeed initial.
