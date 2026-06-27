---
role: proof
locale: en
of_concept: continuity-nonstandard-characterization
source_book: gtm037
source_chapter: "Part 4"
source_section: "Model Theory"
---

Assume $f$ is continuous at $a$ in the standard sense. Let $x \in {}^*\mathbb{R}$ with $x \simeq a$, and let $\varepsilon > 0$ be standard. By continuity, there exists a standard $\delta > 0$ such that $|y - a| < \delta \implies |f(y) - f(a)| < \varepsilon$ for all standard $y$. By elementary extension, the same holds in $^*\mathbb{R}$. Since $x \simeq a$, we have $|x - a| < \delta$, so $|{}^*f(x) - f(a)| < \varepsilon$. Since $\varepsilon$ is arbitrary, $^*f(x) \simeq f(a)$.

Conversely, assume the nonstandard condition $(ii)$. Let $\varepsilon > 0$ be standard. Let $\zeta$ be a positive infinitesimal. Then for any $x \in {}^*\mathbb{R}$, $|x - a| < \zeta$ implies $x \simeq a$, hence by $(ii)$ we have $^*f(x) \simeq f(a)$, so $|{}^*f(x) - f(a)| < \varepsilon$. Thus in $^*\mathbb{R}$,
$$\exists \zeta > 0 \; \forall x \in {}^*\mathbb{R} \;( |x - a| < \zeta \implies |{}^*f(x) - f(a)| < \varepsilon ).$$
Since the same statement holds in $\mathbb{R}$ by elementary equivalence, $f$ is continuous at $a$.
