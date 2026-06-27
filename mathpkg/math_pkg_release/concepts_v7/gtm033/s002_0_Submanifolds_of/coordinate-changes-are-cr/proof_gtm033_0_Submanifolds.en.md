---
role: proof
locale: en
of_concept: coordinate-changes-are-cr
source_book: gtm033
source_chapter: "0"
source_section: "Submanifolds of R^{n+k}"
---

# Proof of Coordinate Changes are $C^r$

Let $M$ be an $n$-dimensional submanifold of $\mathbb{R}^{n+k}$, given locally as a regular level surface of a $C^r$ map, and let $\{(\varphi_i, U_i)\}$ be the atlas of charts constructed from local coordinate systems on $M$. The coordinate change (or transition map) between two overlapping charts is

$$\varphi_j \circ \varphi_i^{-1} : \varphi_i(U_i \cap U_j) \to \varphi_j(U_i \cap U_j).$$

We must show this map is of class $C^r$.

Recall how the charts are constructed. Near a point $x \in M$, there exists an open set $W \subset \mathbb{R}^{n+k}$ and a $C^r$ map $f : W \to \mathbb{R}^k$ of rank $k$ such that $W \cap M = f^{-1}(0)$. After a permutation of coordinates, the Implicit Function Theorem (which is valid in the $C^r$ category) provides a $C^r$ map $g : U \to \mathbb{R}^k$ on some open $U \subset \mathbb{R}^n$ such that locally

$$M \cap W = \{ (x, g(x)) \mid x \in U \}.$$

The chart $(\varphi, V)$ is then defined by $V = M \cap W$ and $\varphi(x, g(x)) = x$, which is the restriction of the projection $\mathbb{R}^{n+k} \to \mathbb{R}^n$. Its inverse is $x \mapsto (x, g(x))$, which is $C^r$ because $g$ is $C^r$.

Now take two such charts $(\varphi_i, U_i)$ and $(\varphi_j, U_j)$ with respective $C^r$ graphing maps $g_i$ and $g_j$. On the overlap, both representations of points in $M$ are valid. The transition map can be expressed via the projections. Specifically, on $\varphi_i(U_i \cap U_j)$ we have

$$\varphi_j \circ \varphi_i^{-1}(x) = \text{proj}_{\mathbb{R}^n} \circ \big( \text{id}_{\mathbb{R}^n} \times g_j \big)^{-1} \circ \big( \text{id}_{\mathbb{R}^n} \times g_i \big) (x).$$

Since $g_i$ and $g_j$ are $C^r$, the maps $\text{id} \times g_i$ and $\text{id} \times g_j$ are $C^r$. The inversion $(\text{id} \times g_j)^{-1}$ on its (open) image is the projection, which is $C^\omega$ (in fact linear). Composing $C^r$ maps with an analytic projection yields a $C^r$ map.

Alternatively, if one constructs charts via the Rank Theorem / parametrization $h : V \to M$ (where $V \subset \mathbb{R}^n$ is open and $h$ is a $C^r$ homeomorphism onto an open subset of $M$ with $Dh$ injective), then two parametrizations $h_i, h_j$ give a transition map $h_j^{-1} \circ h_i$, which is $C^r$ by the inverse function theorem in the $C^r$ category.

In all cases, the coordinate changes $\varphi_j \circ \varphi_i^{-1}$ are $C^r$ maps between open subsets of $\mathbb{R}^n$. This is the essential observation that justifies the abstract definition of a differentiable manifold: the transition maps are automatically differentiable of the same class as the defining maps of the submanifold. $\square$
