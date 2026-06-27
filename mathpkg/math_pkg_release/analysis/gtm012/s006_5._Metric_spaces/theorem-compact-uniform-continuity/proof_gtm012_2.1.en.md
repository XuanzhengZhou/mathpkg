---
role: proof
locale: en
of_concept: theorem-compact-uniform-continuity
source_book: gtm012
source_chapter: "2"
source_section: "1. Continuity, uniform continuity, and compactness"
---

# Proof of Theorem 1.3: Continuous on Compact implies Uniformly Continuous

Suppose $(S, d)$ and $(S', d')$ are metric spaces and suppose $f: S \to S'$ is continuous. Assume $S$ is compact.

Given $\varepsilon > 0$, we know that for each $x \in S$ there is a number $\delta(x) > 0$ such that

$$d'(f(x), f(y)) < \tfrac{1}{2}\varepsilon \quad \text{if } d(x, y) < 2\delta(x).$$

(This follows from continuity of $f$ at $x$: choose $\delta(x)$ corresponding to $\varepsilon/2$, then take half of it.)

Let $N(x) = B_{\delta(x)}(x)$. By the definition of compactness, there are points $x_1, x_2, \ldots, x_n \in S$ such that

$$S \subset \bigcup_{j=1}^{n} N(x_j).$$

Let $\delta = \min\{\delta(x_1), \delta(x_2), \ldots, \delta(x_n)\}$, and suppose $d(x, y) < \delta$. There is some $x_i$ such that $x \in N(x_i)$. Then

$$d(x_i, x) < \delta(x_i) < 2\delta(x_i),$$
$$d(x_i, y) \leq d(x_i, x) + d(x, y) < \delta(x_i) + \delta \leq 2\delta(x_i).$$

Therefore

$$d'(f(x), f(y)) \leq d'(f(x), f(x_i)) + d'(f(x_i), f(y)) \leq \tfrac{1}{2}\varepsilon + \tfrac{1}{2}\varepsilon = \varepsilon.$$

Thus $f$ is uniformly continuous on $S$. $\square$
