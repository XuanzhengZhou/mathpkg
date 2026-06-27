---
role: proof
locale: en
of_concept: triangulable-set-is-tame
source_book: gtm047
source_chapter: "5"
source_section: "15"
---

By hypothesis for $M$, we have a complex $K$ and a homeomorphism $f: |K| \leftrightarrow M$. By Theorem 8 there is an $h$ such that
\begin{enumerate}
\item[(1')] $h(f(|K^1|))$ is a polyhedron
\end{enumerate}
and such that (2) $h|(\mathbf{R}^2 - U)$ is the identity and (3) $h|U$ is a $\phi$-approximation of the identity.

Consider a 2-simplex $\sigma^2 \in K$. Then $h(f(\sigma^2))$ is a 2-cell, and $h(f(\operatorname{Bd} \sigma^2))$ is a polygon, with interior $I$ in $\mathbf{R}^2$. By Theorem 12,
$$I = \operatorname{Int} h(f(\sigma^2)) = h(f(\operatorname{Int} \sigma^2)),$$
so that $\overline{I} = h(f(\sigma^2))$. By Theorem 2.2 there is a complex $L(\sigma^2)$ such that $|L(\sigma^2)| = h(f(\sigma^2))$ and such that the triangulation of $h(f(\operatorname{Bd} \sigma^2))$ induced by $K$ is a subcomplex of $L(\sigma^2)$.

Taking the union of all such $L(\sigma^2)$ together with the triangulation of $h(f(|K^1|))$ yields a complex $L$ such that $|L| = h(M)$. Therefore $h(M)$ is a polyhedron.
