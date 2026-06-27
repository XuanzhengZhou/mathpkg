---
role: proof
locale: en
of_concept: cycle-cocycle-matroid-regular
source_book: gtm054
source_chapter: "F"
source_section: "52"
---

Let $\mathbb{F}$ be an arbitrary field and let $\Gamma = (V, f, E)$ be a multigraph. For each $x \in V$, choose a function $i_x: E \to \mathbb{F}$ satisfying:
$$i_x(e) = 0 \quad \text{if } x \notin f(e);$$
$$i_x(e) = \pm 1 \quad \text{if } x \in f(e);$$
$$i_x(e)i_y(e) = -1 \quad \text{if } f(e) = \{x, y\}.$$

The function $i_x$ orients the edges incident to $x$. Define $\varphi: \mathbb{F}^E \to \mathbb{F}^V$ by
$$\varphi(h)(x) = \sum_{e \in E} i_x(e) h(e)$$
for each $h \in \mathbb{F}^E$, $x \in V$. This is a linear transformation. Let $\mathcal{T} = \ker(\varphi)$.

We show that the minimal nonempty supports of functions in $\mathcal{T}$ are precisely the elementary cycles of $\Gamma$. Let $Z$ be an elementary cycle $x_0 e_1 x_1 e_2 \ldots e_n x_n = x_0$. Define $h: E \to \mathbb{F}$ by
$$h(e) = \begin{cases} 1 & \text{if } e = e_1; \\ -i_{x_j}(e_j) h(e_j) i_{x_j}(e_{j+1}) & \text{if } e = e_{j+1} \;(j = 1, \ldots, n-1); \\ 0 & \text{otherwise.} \end{cases}$$

One verifies that $\sigma(h) = Z$ and $h \in \ker(\varphi) = \mathcal{T}$. Conversely, any minimal nonempty support of a function in $\mathcal{T}$ is an elementary cycle of $\Gamma$. Thus $\mathcal{T}$ is a Tutte subspace over $\mathbb{F}$ for the cycle matroid $(E, \mathcal{M}(\mathcal{Z}(\Gamma)))$.

Since this construction works over any field $\mathbb{F}$, the cycle matroid is representable over every field, i.e., regular. By Proposition F6a, $\mathcal{T}^\perp$ is a Tutte subspace for the dual matroid (the cocycle matroid), which is therefore also regular.
