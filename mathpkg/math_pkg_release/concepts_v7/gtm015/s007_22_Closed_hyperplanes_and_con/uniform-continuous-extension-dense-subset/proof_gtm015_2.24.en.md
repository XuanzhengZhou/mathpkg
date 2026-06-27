---
role: proof
locale: en
of_concept: uniform-continuous-extension-dense-subset
source_book: gtm015
source_chapter: "2"
source_section: "24"
---

# Proof of Extension of uniformly continuous maps from dense subsets

Let $(X, \mathcal{U})$ be a uniform structure, $(Y, \mathcal{V})$ a complete, separated uniform structure, $A$ a dense subset of $X$, and $f: A \rightarrow Y$ a uniformly continuous mapping.

Given any $x \in X$, there exists a filter $\mathcal{F}$ on $A$ converging to $x$ (since $A$ is dense). The image $f(\mathcal{F})$ is a Cauchy filter on $Y$ (by uniform continuity of $f$). Since $Y$ is complete, $f(\mathcal{F})$ converges to a unique point $\bar{f}(x) \in Y$. This defines the extension $\bar{f}: X \rightarrow Y$. One verifies that $\bar{f}$ is uniformly continuous and that it is the unique continuous extension of $f$.
