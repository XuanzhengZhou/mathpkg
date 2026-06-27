---
role: proof
locale: en
of_concept: monotone-function-discontinuities-countable
source_book: gtm002
source_chapter: "7"
source_section: "7. Functions of First Class"
---

**Forward direction:** If $f$ is monotone, there can be at most $|f(b) - f(a)|/\varepsilon$ points in $(a, b)$ where $\omega(x) \geq \varepsilon$. Hence the set of points of discontinuity of $f$ is countable.

**Converse:** Let $\{x_i\}$ be any countable set, and let $\sum \varepsilon_i$ be a convergent series of positive real numbers. The function $f(x) = \sum_{x_i \leq x} \varepsilon_i$ is a monotone bounded function. It has the property that at each $x_i$, the jump is exactly $\varepsilon_i$, and it is continuous elsewhere. Thus any countable set can be realized as the discontinuity set of a monotone function.
