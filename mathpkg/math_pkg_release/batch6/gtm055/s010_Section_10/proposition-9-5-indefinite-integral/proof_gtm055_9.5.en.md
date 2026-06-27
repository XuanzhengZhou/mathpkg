---
role: proof
locale: en
of_concept: proposition-9-5-indefinite-integral
source_book: gtm055
source_chapter: "9"
source_section: "2"
---

The countable additivity of $v_f$ follows from the monotone convergence theorem (or the theorem of Beppo--Levi): if $\{E_n\}$ is a disjoint sequence in $\mathbf{S}$ with union $E$, then $f \chi_E = \sum_n f \chi_{E_n}$ pointwise, and integrating termwise yields $v_f(E) = \sum_n v_f(E_n)$. The fact that $v_f(\emptyset) = 0$ is immediate from the definition of the integral over the empty set. For the change-of-measure formula $\int_X g \, dv_f = \int_X gf \, d\mu$, one verifies it first for characteristic functions $g = \chi_E$, where both sides equal $\int_E f \, d\mu$, then extends to simple functions by linearity, to nonnegative measurable functions by monotone convergence, and finally to integrable functions by the usual decomposition into positive and negative parts.
