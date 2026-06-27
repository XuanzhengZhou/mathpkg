---
role: proof
locale: en
of_concept: riesz-approximation-theorem
source_book: gtm018
source_chapter: "56"
source_section: "56. LINEAR FUNCTIONALS"
---

Let $g_0$ be a function in $\mathcal{L}_+$ such that

$$C \subset g_0 \quad \text{and} \quad \Lambda(g_0) \leq \lambda(C) + \epsilon.$$

If $f_0 = g_0 \cap 1$ (i.e., $f_0(x) = \min(g_0(x), 1)$), then it follows that

$$\Lambda(f_0) \leq \Lambda(g_0) \leq \lambda(C) + \epsilon = \mu(C) + \epsilon \leq \int f_0 \, d\mu + \epsilon,$$

since $C \subset f_0$ implies $\mu(C) = \int_C 1 \, d\mu \leq \int f_0 \, d\mu$.
