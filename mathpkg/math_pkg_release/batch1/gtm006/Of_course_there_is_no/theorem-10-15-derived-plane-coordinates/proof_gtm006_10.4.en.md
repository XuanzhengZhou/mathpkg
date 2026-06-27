---
role: proof
locale: en
of_concept: theorem-10-15-derived-plane-coordinates
source_book: gtm006
source_chapter: "10"
source_section: "4"
---

We coordinatize $\mathcal{A}_1$ so that $[0,0]'$ is the Baer subplane $\mathcal{B}(1,0,0)$ and $[0]'$ is $\mathcal{B}(t,0,0)$. Then we label the points of $[0,0]'$ so that $(\alpha + \beta t, 0)'$ is $(\alpha, \beta)$, and we put $(0,1)' = (t, 0)$. (Note that this is all the choice we have in setting up the coordinate system for $\mathcal{A}_1$.)

Since $[1,0]' = (1,0) = (0(t-1) + 1, 0(t-1) + 0)$ and $(0,1)' = (t,0) = ((t-1) + 1, 0(t-1) + 0)$ in the original coordinates, the line $[1,1]'$ is $\mathcal{B}(t-1, 1, 0)$. Thus, by Exercise 10.5, the lines $[1,k]'$ have the form $\mathcal{B}(t-1, b, c)$. A point $(\alpha + \beta t, 0)'$ is on $\mathcal{B}(t-1, b, c)$ if $(\alpha, \beta)$ is in $\mathcal{B}(t-1, b, c)$, and thus:

The line $[\lambda, 0]'$ (for $\lambda \in F$) passes through $(0,0)'$ and $(-1, \alpha + \beta t)' = (-1 + \alpha t, \beta t)$. The proof then verifies through algebraic manipulation of the ternary operation that $T_1$ satisfies properties (1)-(5).

For property (5), imitating the proof of (3), one shows that $\eta + \mu t = \lambda(\alpha + \beta t) + \gamma + \delta t$, which gives the linear form of the ternary operation.

Properties (2) and (4) are established by the explicit coordinate choices: the addition is identical because the coordinatizing Baer subplanes share the same additive structure, and the line at infinity description follows from the definition of the derivation set $\mathcal{S}$ as the subset of the original line at infinity corresponding to the subfield $F$.
