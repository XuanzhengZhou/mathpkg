---
role: introduce
locale: en
content_hash: ""
written_against: ""
---

For vectors $u, v$ in a vector space $E$ over $\mathbb{K}$ ($\mathbb{R}$ or $\mathbb{C}$), the **open segment** $\langle u, v \rangle$ is the set of all strict convex combinations of $u$ and $v$:

$$\langle u, v \rangle = \{\alpha u + (1 - \alpha)v : 0 < \alpha < 1\}.$$

The corresponding **closed segment** $[u, v]$ is defined with $0 \leq \alpha \leq 1$. These sets are convex. In a separated topological vector space, $[u, v]$ is compact (as the continuous image of $[0, 1]$ under $\alpha \mapsto \alpha u + (1 - \alpha)v$). A segment is called **nondegenerate** when $u \neq v$.

An important technical point: $u \in \langle u, v \rangle$ if and only if $u = v$. (If $u = \alpha u + (1-\alpha)v$ with $0<\alpha<1$, then $(1-\alpha)u = (1-\alpha)v$ and $\alpha \neq 1$ forces $u=v$; conversely $\langle u, u \rangle = \{u\}$.)

Open segments are the fundamental tool for defining extremal points: a point is extremal precisely when it cannot be placed in the interior of a nondegenerate open segment that stays within the set.
