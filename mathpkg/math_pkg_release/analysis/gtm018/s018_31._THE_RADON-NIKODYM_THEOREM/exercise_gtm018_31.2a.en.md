---
role: exercise
locale: en
chapter: "31"
section: "31"
exercise_number: "2a"
---

If $(X, \mathbf{S}, \mu)$ is a measure space and $f$ is a measurable function such that $0 \leq f < 1$, and if $\nu$ is the measure defined by
$$\nu(E) = \int_E \frac{f}{1-f} \, d\mu$$
for every measurable set $E$, then for every nonnegative measurable function $g$,
$$\int g \, d\nu = \int f g \, d\mu.$$
(Hint: rewrite the hypothesis in the form $\int g(1-f) \, d\nu = \int f g \, d\mu$ and, given $E$, write $g = \frac{\chi_E}{1-f}$.)
