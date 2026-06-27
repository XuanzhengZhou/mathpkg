---
role: proof
locale: en
of_concept: uniform-convexity-not-topological
source_book: gtm036
source_chapter: "5"
source_section: "17"
---

This is stated as Problem C(c) in the text. For uniform convexity, the counterexample is the plane $\mathbb{R}^2$: under the Euclidean norm it is uniformly convex, but under the $\ell^1$ norm $\|(x,y)\|_1 = |x| + |y|$ the unit ball is a diamond, which is not strictly convex (its boundary contains line segments), hence not uniformly convex.

For the convergence property, consider the product $E \times \mathbb{R}$ where $E$ is an infinite-dimensional uniformly convex space. Under the norm $\|(x,t)\| = \max(\|x\|_E, |t|)$, one can construct a net converging weakly and in norm to a limit without converging in the product norm, violating the convergence property.
