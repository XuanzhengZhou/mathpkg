---
role: proof
locale: en
of_concept: kuratowski-necessity-f9-f9
source_book: gtm054
source_chapter: "10"
source_section: "Section 50"
---

Let $\mathbb{F}$ be a field and let $\Gamma = (V, f, E)$ be a multigraph. For each $x \in V$, we choose a function $i_x: E \rightarrow \mathbb{F}$ satisfying

$$i_x(e) = 0 \quad \text{if } x \notin f(e);$$

$$i_x(e) = \pm 1 \quad \text{if } x \in f(e);$$

$$i_x(e)i_y(e) = -1 \quad \text{if } f(e) = \{x, y\}.$$

The function $i_x$ for $x \in V$ in effect orients the edges in the vertex cocycle of $x$.

Let $\varphi: \mathbb{F}^E \rightarrow \mathbb{F}^V$ be defined so that for each $h \in \mathbb{F}^E$, its image $\varphi(h)$ is given by $\varphi(h)(x) = \sum_{e \in E} i_x(e)h(e)$. It is immediate that $\varphi$ is a linear transformation. Let $\mathcal{T}$ denote the kernel of $\varphi$. We will show that the minimal nonempty supports of functions in $\mathcal{T}$ are precisely the elementary cycles of $\Gamma$; that is, we show that $\mathcal{T}$ is a Tutte subspace over $\mathbb{F}$ for $(E, \mathcal{M}(\mathcal{Z}(\Gamma)))$.

Let $Z$ be an elementary cycle of $\Gamma$ where $\Gamma_Z$ is the elementary circuit $x_0e_1x_1e_2 \ldots e_nx_n = x_0$. Let us define

$$h(e) = \begin{cases} 1 & \text{if } e = e_1; \\ -i_{x_j}(e_j)h(e_j)i_{x_j}(e_{j+1}) & \text{if } e = e_{j+1} (j = 1, \ldots, n-1); \\ 0 & \text{otherwise.} \end{cases}$$

Clearly $\sigma(h) = Z$, and one can verify that $h$ is well-

in Proposition IVA6 and if $S$ is a subspace of $\mathbb{F}^V$, then any function $h \in S$ has a decomposition satisfying conditions (a) and (b) of IVA6. If $F$ is an ordered field, then condition (c) also holds, but we shall not require this fact.
