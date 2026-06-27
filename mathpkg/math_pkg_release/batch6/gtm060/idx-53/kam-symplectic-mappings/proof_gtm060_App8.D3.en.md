---
role: proof
locale: en
of_concept: kam-symplectic-mappings
source_book: gtm060
source_chapter: "Appendix 8"
source_section: "D.3"
---

The KAM theorem for symplectic mappings is proved by an iterative Newton-type scheme analogous to the continuous case. The unperturbed mapping
$$I' = I, \qquad \varphi' = \varphi + \alpha(I), \quad \alpha(I) = \frac{\partial S_0}{\partial I}$$
preserves all tori $I = \text{const}$, with rotation vector $\alpha(I)$. Under the nondegeneracy condition $\det |\partial^2 S_0 / \partial I^2| = \det |\partial \alpha / \partial I| \neq 0$, the rotation map $I \mapsto \alpha(I)$ is locally invertible. For a fixed Diophantine rotation vector $\alpha$, one solves at each step a linearized conjugacy equation (a difference equation on the torus), whose small denominators are controlled by the Diophantine condition. At each iteration, the perturbation is quadratically smaller (Newton convergence), yielding a $C^\infty$ (or analytic) invariant torus for the perturbed mapping.

For $n = 1$, the invariant tori are invariant circles. If a point starts near such a circle, it remains in its neighborhood for all iterations.
