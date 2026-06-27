---
role: proof
locale: en
of_concept: resolution-curve-singularities-surface
source_book: gtm052
source_chapter: "V"
source_section: "3"
---

First apply (3.8) to each irreducible component of $Y$ to reduce to the case where every component is nonsingular, since added exceptional curves are already nonsingular.

If the total curve has a singular point $P$ other than a node, blow it up. If $\mu_P(Y) \geqslant 3$, then $p_a(\pi^{-1}(Y)) < p_a(Y)$ by (3.7), so only finitely many such steps occur. If $\mu_P(Y) = 2$, then $p_a(\pi^{-1}(Y)) = p_a(Y)$ and $Y.E = 2$ by (3.7). Three possibilities arise:
\begin{enumerate}
\item $\tilde{Y}$ meets $E$ transversally in two distinct points -- stop;
\item $\tilde{Y}$ meets $E$ in one point, tangent -- one more blowup creates a triple point, then $p_a$ drops;
\item $\tilde{Y}$ is singular at the intersection point -- blowing up creates multiplicity 3, so $p_a$ drops.
\end{enumerate}
Thus any non-nodal singularity forces the arithmetic genus to drop after finitely many blowups. Since arithmetic genus is a nonnegative integer, the process terminates after finitely many steps. At termination, every component is nonsingular and the only singularities are nodes, i.e., $f^{-1}(Y)$ has normal crossings.
