---
role: proof
locale: en
of_concept: topological-classification-stationary-flows
source_book: gtm060
source_chapter: "Appendix 2"
source_section: "Section 47"
---

For a stationary flow, Euler's equation in vorticity form gives $\frac{\partial \operatorname{curl} v}{\partial t} = [v, \operatorname{curl} v] = 0$, so $v$ and $\operatorname{curl} v$ commute as vector fields.

The Bernoulli surfaces are defined as the level sets of the Bernoulli function. On each such surface, the commuting vector fields $v$ and $\operatorname{curl} v$ are tangent (since both are orthogonal to the gradient of the Bernoulli function). Being non-collinear by hypothesis, they span a two-dimensional distribution on the Bernoulli surface.

The flows of $v$ and $\operatorname{curl} v$ generate an $\mathbb{R}^2$ action on each closed Bernoulli surface. A closed surface admitting a locally free $\mathbb{R}^2$ action must be a torus (by Liouville's theorem on integrable systems: a compact connected manifold with $n$ commuting vector fields that are independent everywhere must be a torus $\mathbb{T}^n$; here $n = 2$).

For non-closed Bernoulli surfaces intersecting the boundary of $D$, the boundary conditions force the flow lines to be closed, and the surfaces consist of annuli bounded by these closed flow lines (one on the boundary and one in the interior). The proof follows by considering the $\mathbb{R}^2$ action restricted to surfaces with boundary. The analyticity of the vector fields guarantees that the flow lines and Bernoulli surfaces are real-analytic submanifolds, but the topological conclusion holds more generally as long as $v$ and $\operatorname{curl} v$ are not collinear.
