---
role: proof
locale: en
of_concept: measure-algebra-satisfies-weak-distributive-law
source_book: gtm008
source_chapter: "20"
source_section: "Weak Distributive Laws"
---

Let $\{b_{n,k} \mid n, k < \omega\} \subseteq B$. Then for every real $\varepsilon > 0$,

$$(\forall n < \omega) (\exists l \in \omega) \left[ m \left( \sum_{k < \omega} b_{nk} - \sum_{k \leq l} b_{nk} \right) < \frac{\varepsilon}{2^{n+1}} \right].$$

For each $n$, choose $f(n) \in \omega$ satisfying this inequality and set

$$b = \prod_{n < \omega} \sum_{k \leq f(n)} b_{nk}.$$

Then $m(b) \geq 1 - \varepsilon$. Since $\varepsilon > 0$ is arbitrary and $B$ is a measure algebra, this forces the equality required by the $(\omega, \omega)$-WDL.
