---
role: proof
locale: en
of_concept: tvs-minus-zero-is-connected
source_book: gtm015
source_chapter: "3"
source_section: "28"
---

# Proof of A TVS of dimension at least 2 minus the origin is connected

If $E$ is a TVS over $\mathbb{R}$ and $\dim_{\mathbb{R}} E \ge 2$, then $E - \{\theta\}$ is connected.

Given $x, y \in E - \{\theta\}$, it suffices to show there exists a connected subset $C$ of $E - \{\theta\}$ containing both $x$ and $y$.

Suppose first that $x$ and $y$ are linearly independent. Then the mapping $f: [0, 1] \rightarrow E$ defined by $f(\alpha) = (1 - \alpha)x + \alpha y$ does not assume the value $\theta$ (for $\theta = (1-\alpha)x + \alpha y$ with $\alpha \in [0,1]$ would imply linear dependence). The range $C = f([0, 1])$ is connected (continuous image of a connected set) and contains $x = f(0)$ and $y = f(1)$.

Now suppose $x$ and $y$ are linearly dependent (so $y = \lambda x$ for some $\lambda \ne 0$). Since $\dim E \ge 2$, there exists $z \in E$ linearly independent from $x$. Then there is a connected set containing $x$ and $z$ (by the first case), and similarly a connected set containing $z$ and $y$. The union of these two (intersecting at $z$) is connected. Thus $E - \{\theta\}$ is path-connected, hence connected.
