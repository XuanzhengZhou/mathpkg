---
role: proof
locale: en
of_concept: subadditive-function-metric-topology
source_book: gtm027
source_chapter: "4"
source_section: "C. Problem on Metrics"
---

# Proof of Subadditive Function Preserves Metric Topology

Let $f: [0, \infty) \to [0, \infty)$ be a continuous function such that:

1. $f(x) = 0$ if and only if $x = 0$,
2. $f$ is non-decreasing,
3. $f(x + y) \leq f(x) + f(y)$ for all $x, y \geq 0$ (subadditivity).

Let $(X, d)$ be a metric space and define $e(x, y) = f(d(x, y))$ for all $x, y \in X$.

## Part 1: $(X, e)$ is a metric space

- **Positive definiteness**: $e(x, y) = f(d(x, y)) \geq 0$ since $f$ maps to non-negative reals. $e(x, x) = f(d(x, x)) = f(0) = 0$. Conversely, if $e(x, y) = 0$, then $f(d(x, y)) = 0$, so by property (1), $d(x, y) = 0$, hence $x = y$.

- **Symmetry**: $e(x, y) = f(d(x, y)) = f(d(y, x)) = e(y, x)$.

- **Triangle inequality**: For any $x, y, z \in X$,
  $$e(x, z) = f(d(x, z)) \leq f(d(x, y) + d(y, z)) \quad \text{(since $f$ is non-decreasing)}$$
  $$\leq f(d(x, y)) + f(d(y, z)) = e(x, y) + e(y, z) \quad \text{(by subadditivity)}.$$

Thus $(X, e)$ is a metric space.

## Part 2: The metric topologies coincide

We must show that the identity map $\mathrm{id}: (X, d) \to (X, e)$ is a homeomorphism.

**Continuity of $\mathrm{id}: (X, d) \to (X, e)$**: Let $x \in X$ and $\varepsilon > 0$. Since $f$ is continuous at $0$ and $f(0) = 0$, there exists $\eta > 0$ such that $f(t) < \varepsilon$ whenever $0 \leq t < \eta$. Choose $\delta = \eta$. Then if $d(x, y) < \delta$, we have $f(d(x, y)) < \varepsilon$, i.e., $e(x, y) < \varepsilon$. This establishes continuity.

**Continuity of $\mathrm{id}: (X, e) \to (X, d)$**: Let $x \in X$ and $\varepsilon > 0$. We need $\delta > 0$ such that $e(x, y) < \delta$ implies $d(x, y) < \varepsilon$.

Since $f$ is continuous and $f(t) > 0$ for $t > 0$, and $f(\varepsilon) > 0$, there exists (by the properties of $f$) a $\delta > 0$ with $\delta = f(\varepsilon)/2$ or more directly: if $f(d(x, y)) < f(\varepsilon)$, then since $f$ is non-decreasing and $f(t) = 0$ only at $t = 0$, we must have $d(x, y) < \varepsilon$ (otherwise, if $d(x, y) \geq \varepsilon$, then $f(d(x, y)) \geq f(\varepsilon)$, contradiction). So set $\delta = f(\varepsilon) > 0$.

Then $e(x, y) = f(d(x, y)) < \delta = f(\varepsilon)$ implies $d(x, y) < \varepsilon$ by the monotonicity argument.

Therefore both maps are continuous, and the topologies are identical.

A particular case: $f(x) = \frac{x}{1+x}$ satisfies all the hypotheses.
