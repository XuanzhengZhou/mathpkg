---
role: proof
locale: en
of_concept: monotone-function-countable-discontinuities
source_book: gtm002
source_chapter: "7"
source_section: "7"
---

If $f$ is monotone, there can be at most $|f(b) - f(a)|/\varepsilon$ points in $(a,b)$ where $\omega(x) \geq \varepsilon$, because each such point contributes a jump of at least $\varepsilon$ to the total variation. Taking the union over all rational intervals and a sequence of $\varepsilon \to 0$ shows the set of all discontinuity points is countable.

On the other hand, let $\{x_i\}$ be any countable set, and let $\sum \varepsilon_i$ be a convergent series of positive real numbers. The function

$$f(x) = \sum_{x_i \leq x} \varepsilon_i$$

is a monotone bounded function. It has the property that $\omega(x_i) = \varepsilon_i$ for each $i$, and $f$ is continuous at all other points. Hence the set of points of discontinuity of $f$ is exactly $\{x_i\}$.
