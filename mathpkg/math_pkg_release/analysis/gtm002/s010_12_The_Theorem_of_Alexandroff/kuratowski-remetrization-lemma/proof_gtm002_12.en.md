---
role: proof
locale: en
of_concept: kuratowski-remetrization-lemma
source_book: gtm002
source_chapter: "12"
source_section: "The Theorem of Alexandroff"
---

Define a new distance function in $X$ by

$$\sigma(x, y) = \varrho(x, y) + \sum_{i=1}^{\infty} \frac{1}{2^i} \min\left(1, |f_i(x) - f_i(y)|\right).$$

To verify the triangle axiom it suffices to observe that it is satisfied by each term. The other axioms are clearly satisfied.

For any $\varepsilon > 0$ and $x \in X$ there is an integer $N$ such that $2^{-N} < \varepsilon$ and a positive number $\delta < \varepsilon$ such that

$$\varrho(x, y) < \delta \quad \text{implies} \quad |f_i(x) - f_i(y)| < \varepsilon \qquad (i = 1, 2, \ldots, N).$$

If $\varrho(x, y) < \delta$, then

$$\sigma(x, y) < \varepsilon + \sum_{i=1}^{N} \frac{1}{2^i}\,\varepsilon + \sum_{i=N+1}^{\infty} \frac{1}{2^i} < \varepsilon + \varepsilon + \varepsilon = 3\varepsilon.$$

Hence $\sigma(x, y) \to 0$ whenever $\varrho(x, y) \to 0$. Conversely, since $\varrho(x, y) \leq \sigma(x, y)$, the opposite implication holds. Therefore the topologies induced by $\sigma$ and $\varrho$ coincide, and $\{x_n\}$ is Cauchy relative to $\sigma$ if and only if it is Cauchy relative to $\varrho$.

Now suppose that $\{x_n\}$ is a Cauchy sequence relative to $\sigma$. For each $i$, choose $N$ such that $\sigma(x_n, x_m) < 1/2^i$ for all $n, m \geq N$. For all $n, m \geq N$, we have

$$1 > 2^i\,\sigma(x_n, x_m) \geq \min\left(1, |f_i(x_n) - f_i(x_m)|\right),$$

and therefore

$$|f_i(x_n) - f_i(x_m)| < 1.$$

Hence the sequence $\{f_i(x_n)\}$ is bounded, for each $i$. Since $\varrho(x, y) \leq \sigma(x, y)$, the sequence $\{x_n\}$ is also Cauchy relative to $\varrho$. Therefore, by hypothesis, the sequence $\{x_n\}$ is convergent. Thus $X$ is complete under the metric $\sigma$. $\square$
