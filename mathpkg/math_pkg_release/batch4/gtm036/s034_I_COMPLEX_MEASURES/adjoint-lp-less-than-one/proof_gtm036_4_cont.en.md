---
role: proof
locale: en
of_concept: adjoint-lp-less-than-one
source_book: gtm036
source_chapter: "4"
source_section: "Problem section (L^p duality, part f)"
---
For $l^p(X)$: use 6N(d). The discrete nature of $X$ means that the continuous linear functionals on $l^p(X)$ correspond to sequences in $l^\infty(X)$ via the pairing $\phi(\{x_n\}) = \sum x_n y_n$.

For $L^p(X, \mu)$ on an interval with Lebesgue measure: use 6N(c). For $0 < p < 1$, the $L^p$ spaces are not locally convex. In fact, the only convex open neighborhood of $0$ in $L^p[0,1]$ is the whole space itself. By the Hahn-Banach theorem (which requires local convexity), no non-zero continuous linear functionals can exist. More directly, any continuous linear functional would induce a non-trivial convex open set separating points, which cannot exist in these "quasi-Banach" spaces.

The decisive contrast between the two cases is that sequence spaces $l^p(X)$ for $0 < p < 1$ do admit non-trivial continuous linear functionals (the evaluation functionals), while the continuous function space versions $L^p$ on a non-atomic measure space do not.
