---
role: proof
locale: en
of_concept: continuous-on-compact-uniform-implies-uniformly-continuous
source_book: gtm027
source_chapter: "6"
source_section: "Compact Spaces"
---

# Proof that Continuous Functions on Compact Uniform Spaces are Uniformly Continuous (Theorem 6.31)

**Theorem 6.31.** Each continuous function on a compact uniform space to a uniform space is uniformly continuous.

**Proof.** Let $f : X \to Y$ be a continuous function where $(X, \mathcal{U})$ is a compact uniform space and $(Y, \mathcal{V})$ is a uniform space. Define $f_2 : X \times X \to Y \times Y$ by $f_2(x,y) = (f(x), f(y))$.

Since $f$ is continuous, $f_2$ is continuous relative to the product topologies. Let $d$ be any pseudo-metric belonging to the gage of $Y$ (i.e., $d$ is uniformly continuous on $Y \times Y$). Then the composition $d \circ f_2$ is continuous on $X \times X$, because it is the composition of the continuous function $f_2$ with the continuous function $d$ (pseudo-metrics in the gage are continuous functions).

The function $d \circ f_2$ is a pseudo-metric on $X$. By Theorem 6.29, every continuous pseudo-metric on the compact uniform space $X \times X$ belongs to the gage of $X$. However, more directly: since $d \circ f_2$ is continuous, for each $r > 0$, the set

$$\{(x,y) : d(f(x), f(y)) < r\} = (d \circ f_2)^{-1}((-\infty, r))$$

is an open neighborhood of the diagonal in $X \times X$. By Theorem 6.29, this open neighborhood belongs to $\mathcal{U}$. But this is exactly $f_2^{-1}[V_{d,r}]$, so $f_2^{-1}[V_{d,r}] \in \mathcal{U}$ for each subbase member $V_{d,r}$ of $\mathcal{V}$. Hence $f$ is uniformly continuous.
