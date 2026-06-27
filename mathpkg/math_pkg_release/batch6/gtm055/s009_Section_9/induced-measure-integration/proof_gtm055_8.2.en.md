---
role: proof
locale: en
of_concept: induced-measure-integration
source_book: gtm055
source_chapter: "8"
source_section: "9"
---

Verify first for characteristic functions $\chi_E$ with $E \in \mathbf{T}$: by definition of the induced measure, $\nu(E) = \mu(\Phi^{-1}(E))$, so $\int_Y \chi_E d\nu = \nu(E) = \mu(\Phi^{-1}(E)) = \int_X \chi_E \circ \Phi d\mu$. Extend by linearity to simple functions, then to nonnegative measurable functions via the Monotone Convergence Theorem, and finally to integrable functions by decomposing into real/imaginary and positive/negative parts.
