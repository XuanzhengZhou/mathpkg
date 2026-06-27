---
role: proof
locale: en
of_concept: principal-objects-correspond-to-H1
source_book: gtm026
source_chapter: "3"
source_section: "13"
---

Given a principal object $(E, \gamma, p, m, s)$, we construct a $1$-cocycle representing its isomorphism class.

By the hint, $(m, \operatorname{pr}_E, p)$ is an absolute coequalizer (using the result of Exercise 1.5). The pullback property in the definition of a principal object allows us to define a $\mathcal{K}$-morphism $\sigma: E \rightarrow Y$ such that

$$Y \xleftarrow{\sigma} E \xrightarrow{p} X$$

is a product diagram in $\mathcal{K}$. Specifically, the pullback condition ensures that for each point, the fiber over $x \in X$ is isomorphic to $Y$, and the section $s$ provides a basepoint. The morphism $\sigma$ measures the deviation from the trivial product.

From the diagram data $(m, \operatorname{pr}_E, p, \sigma)$ one extracts a $1$-cocycle in $[XT^2, Y]$ using the $\mathbf{T}$-algebra structure $\gamma$ on $E$ and the action $m$. The cohomology class of this cocycle depends only on the isomorphism class of the principal object (morphisms of principal objects preserve $m$ and $p$ but not necessarily the section $s$).

Conversely, given a $1$-cocycle representing an element of $H^1(X, \xi)$, construct a principal object via the "twisted product" (semi-direct product) of $Y$ and $X$, where the $\mathbf{T}$-algebra structure on $E = Y \times X$ is the one $\gamma$ constructed in part (a) of the exercise, and $m$ and $p$ are the natural projections. The section $s$ is the canonical inclusion of $X$ via the zero element of $Y$.

These constructions are mutually inverse up to isomorphism, establishing the bijection.
