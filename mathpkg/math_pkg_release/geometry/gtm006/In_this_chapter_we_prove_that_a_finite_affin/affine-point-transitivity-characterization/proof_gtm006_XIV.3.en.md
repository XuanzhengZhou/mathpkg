---
role: proof
locale: en
of_concept: affine-point-transitivity-characterization
source_book: gtm006
source_chapter: "XIV"
source_section: "3"
---

Let $\Pi$ split the points of $l_\infty$ into $s$ orbits.

($\Rightarrow$) Suppose $\Pi$ is transitive on the affine points of $\mathcal{A} = \mathcal{P}^{l_\infty}$. Then the total number of point orbits of $\Pi$, considered as a collineation group of $\mathcal{P}$, is $s+1$ (one orbit for affine points plus $s$ orbits on $l_\infty$). By Theorem 13.4, $\Pi$ has $s+1$ line orbits in $\mathcal{P}$. As one line orbit is $\{l_\infty\}$, $\Pi$ has $s$ orbits of affine lines.

If $X, Y$ are special points in different orbits of $\Pi$, then clearly $\Pi$ cannot map an affine line through $X$ onto an affine line through $Y$. Since the number of affine line orbits equals $s$, each special point orbit corresponds to exactly one orbit of affine lines (the lines through points in that orbit). Thus for any $D \in l_\infty$, $\Pi_D$ is transitive on the affine lines through $D$.

($\Leftarrow$) Conversely, suppose for every $D \in l_\infty$, $\Pi_D$ is transitive on the affine lines through $D$. Then each parallel class forms a single orbit of affine lines under $\Pi$. Since there are $n+1$ parallel classes, $\Pi$ has at most $n+1$ line orbits. If $\Pi$ were not transitive on affine points, there would be at least $2$ affine point orbits, leading to at least $s+2$ point orbits in $\mathcal{P}$. But Theorem 13.4 would then imply at least $s+2$ line orbits, contradicting that there are only $s+1$ (where $s$ is the number of special point orbits). Therefore $\Pi$ must be transitive on affine points. $\square$
