---
role: proof
locale: en
of_concept: left-invariant-metric-uniformity
source_book: gtm015
source_chapter: "7"
source_section: "Complete topological groups"
---

# Proof of Left-invariant compatible metric yields the left uniformity

Let $G$ be a metrizable topological group and let $d$ be a left-invariant compatible metric on $G$ (whose existence is guaranteed by (6.3)). Let $\mathcal{U}_d$ be the uniform structure derived from $d$, and let $\mathcal{U}_s$ be the left uniform structure of $G$. We prove $\mathcal{U}_d = \mathcal{U}_s$.

It suffices to show that the two filters have a common base. Let $\varepsilon > 0$. A basic neighborhood of the neutral element $e$ is

$$V = \{x : d(e, x) < \varepsilon\}.$$

The corresponding basic entourage for $\mathcal{U}_s$ is

$$V_s = \{(x, y) : x^{-1}y \in V\} = \{(x, y) : d(e, x^{-1}y) < \varepsilon\}.$$

By left-invariance of $d$, $d(e, x^{-1}y) = d(x, y)$. Hence

$$V_s = \{(x, y) : d(x, y) < \varepsilon\},$$

which is precisely a basic entourage for $\mathcal{U}_d$. Thus every basic entourage of $\mathcal{U}_s$ is a basic entourage of $\mathcal{U}_d$, and conversely, so $\mathcal{U}_d = \mathcal{U}_s$.

(There is a dual result with "left" replaced by "right" throughout.)
