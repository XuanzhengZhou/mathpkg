---
role: proof
locale: en
of_concept: affine-line-transitivity-equivalent-conditions
source_book: gtm006
source_chapter: "XIV"
source_section: "3"
---

Let $\mathcal{A} = \mathcal{P}^{l_\infty}$ where $\mathcal{P}$ is the projective completion of $\mathcal{A}$ and $l_\infty$ is the line at infinity.

(i) $\Rightarrow$ (ii): Suppose $\Pi$ is transitive on affine lines. Every affine point lies on $n+1$ affine lines, and by transitivity on lines, for any two affine points their line stabilizers are conjugate. Counting arguments show $\Pi$ is transitive on affine points. For special points (points on $l_\infty$), if $X, Y \in l_\infty$, then any affine line through $X$ can be mapped to an affine line through $Y$ by an element of $\Pi$ (since $\Pi$ is transitive on affine lines). This forces the images of $X$ under $\Pi$ to cover all of $l_\infty$, so $\Pi$ is transitive on special points.

(ii) $\Rightarrow$ (iii): Since $\Pi$ is transitive on affine points and on special points, the stabilizer of an affine point acts transitively on the lines through that point (each determined by a special point). This gives transitivity on affine flags: any flag $(V, l)$ can be mapped to any other flag $(V', l')$ by first mapping $V$ to $V'$ and then using the transitivity of the point stabilizer on lines.

(iii) $\Rightarrow$ (i): Flag-transitivity immediately implies line-transitivity by projecting each flag to its line component. $\square$
