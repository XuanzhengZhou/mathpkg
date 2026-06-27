---
role: introduce
locale: en
content_hash: ""
written_against: ""
---

The **closed segment** $[u, v]$ joining two vectors $u, v$ in a vector space $E$ over $\mathbb{K}$ is the set of all convex combinations of $u$ and $v$:

$$[u, v] = \{\alpha u + (1 - \alpha)v : 0 \leq \alpha \leq 1\}.$$

This set is always convex and is precisely the convex hull of the two-point set $\{u, v\}$: $[u, v] = \operatorname{conv}\{u, v\}$.

When $E$ carries a separated topological vector space structure, each closed segment $[u, v]$ is compact. This follows from the fact that $[u, v]$ is the image of the compact interval $[0, 1]$ under the continuous mapping $\alpha \mapsto \alpha u + (1 - \alpha)v$. Consequently, $[u, v]$ is also a closed subset of $E$.

Closed segments serve as the scaffolding for the theory of convex sets. They provide the simplest nontrivial examples of convex compact sets and are used to define the complementary notion of open segments, which in turn are essential for defining extremal points.
