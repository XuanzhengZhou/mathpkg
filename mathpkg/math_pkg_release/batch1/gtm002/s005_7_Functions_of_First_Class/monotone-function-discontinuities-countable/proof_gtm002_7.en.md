---
role: proof
locale: en
of_concept: monotone-function-discontinuities-countable
source_book: gtm002
source_chapter: "7"
source_section: "Functions of First Class"
---

**Forward direction.** If $f$ is monotone on $(a, b)$, then for any $\varepsilon > 0$, there can be at most $|f(b) - f(a)|/\varepsilon$ points in $(a, b)$ where $\omega(x) \geq \varepsilon$. Indeed, at each such point the jump in $f$ is at least $\varepsilon$, and the total variation of a monotone function on $(a, b)$ is $|f(b) - f(a)|$. Hence the set of points where $\omega(x) \geq 1/n$ is finite for each $n$, and the set of all discontinuity points $D = \bigcup_{n=1}^{\infty} \{x : \omega(x) \geq 1/n\}$ is a countable union of finite sets, hence countable.

**Converse direction.** Let $\{x_i\}$ be any countable set, and let $\sum \varepsilon_i$ be a convergent series of positive real numbers. Define $f(x) = \sum_{x_i \leq x} \varepsilon_i$. Then $f$ is monotone non-decreasing and bounded. At each $x_i$, the function $f$ has a jump discontinuity of size $\varepsilon_i$, so $\omega(x_i) = \varepsilon_i > 0$. At any point $x$ not in $\{x_i\}$, the series defining $f$ has no term concentrated at $x$, and $f$ is continuous there. Thus the set of discontinuities of $f$ is exactly $\{x_i\}$.
