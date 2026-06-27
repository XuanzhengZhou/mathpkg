---
role: proof
locale: en
of_concept: general-stability-criterion
source_book: gtm014
source_chapter: "III"
source_section: "§6. Stable Mappings in Low Dimensions"
---

For simplicity we consider the case $s = 2$. Let $p = p_1$ and $p' = p_2$, and consider $f$ in the vicinity of $p$. If $p$ is an $S_{1_k}$ singularity, choose coordinate systems centered at $p$ and at $q = f(p)$ such that $f$ has the canonical form (4.2). Let $x_1$ be the first coordinate function at $p$, and $y_1, \ldots, y_k$ the first $k$ coordinate functions about $q$. Then the tangent space to $S_{1_k}(f)$ at $p$ is characterized by the equations
$$
dx_1 = df^*y_2 = \cdots = df^*y_k = 0
$$
and the image space by
$$
dy_1 = dy_2 = \cdots = dy_k = 0. \tag{6.6}
$$
Similarly, relative to $p'$ and $q$, the tangent space to $S_{1_{k'}}(f)$ at $p'$ is characterized by
$$
dx'_1 = df^*y'_2 = \cdots = df^*y'_{k'} = 0
$$
and the image space by
$$
dy'_1 = \cdots = dy'_{k'} = 0. \tag{6.6'}
$$
By assumption the subspaces (6.6) and (6.6)' are in general position, so the differentials $dy_1, \ldots, dy_k, dy'_1, \ldots, dy'_{k'}$ are linearly independent at $q$. Hence $y_1, \ldots, y_k, y'_1, \ldots, y'_{k'}$ can be introduced as the first $k + k'$ coordinate functions of some coordinate system, in which the map simultaneously takes the required canonical forms near both preimage points. The general case follows by the same reasoning with more indices.
