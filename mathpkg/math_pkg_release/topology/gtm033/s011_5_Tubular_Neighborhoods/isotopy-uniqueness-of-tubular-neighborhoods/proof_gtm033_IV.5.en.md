---
role: proof
locale: en
of_concept: isotopy-uniqueness-of-tubular-neighborhoods
source_book: gtm033
source_chapter: "IV"
source_section: "5"
---

# Proof of Isotopy Uniqueness of Tubular Neighborhoods (Theorem 5.3)

**Theorem (5.3).** Let $M \subset V$ be a submanifold, $\partial M = \partial V = \varnothing$. Then any two tubular neighborhoods of $M$ in $V$ are isotopic.

*Proof.* Let the tubular neighborhoods be $(f_i, \xi_i = (p_i, E_i, M))$, $i = 0, 1$.

**Step 1: Reduction to the case $f_0(E_0) \subset f_1(E_1)$.**

First suppose $f_0(E_0) \subset f_1(E_1)$. If not, pull $E_0$ into the open set $f_0^{-1} f_1(E_1) \subset E_0$ by a preliminary isotopy of the form

$$G: E_0 \times I \rightarrow E_0,$$
$$G(z, t) = (1 - t)z + t \cdot h(z)$$

where

$$h: E_0 \rightarrow E_0,$$
$$h(y) = \left[ \frac{\delta(p(y))}{1 + \|y\|^2} \right] y$$

and $\delta: M \rightarrow \mathbb{R}_+$ is a suitably small $C^\infty$ map. This isotopy shrinks the fibers sufficiently so that the image lies inside $f_1(E_1)$ while fixing the zero section. Thus we may assume $f_0(E_0) \subset f_1(E_1)$ without loss of generality.

**Step 2: Fibre derivative and canonical homotopy.**

Let $g = f_1^{-1} \circ f_0: E_0 \rightarrow E_1$. Let $\Phi: \xi_0 \rightarrow \xi_1$ be the fibre derivative of $g$. Thus $\Phi$ is the component along the fibres of the morphism

$$T_M g: T_M E_0 = TM \oplus \xi_0 \rightarrow TM \oplus \xi_1 = T_M E_1,$$

which shows that $\Phi$ is an isomorphism of vector bundles (since $g$ is an embedding with $g|M = 1_M$, its differential along the zero section is the identity on $TM$ and an isomorphism on the fibre direction).

We define the **canonical homotopy** from $\Phi$ to $g$ to be

$$H: E_0 \times I \rightarrow E_1,$$
$$H(x, y, t) = \begin{cases}
t^{-1} g(x, ty) & t > 0, \\
\Phi(x, y) & t = 0.
\end{cases}$$

By Taylor's formula we can write

$$g_2(x, y) = \frac{\partial g_2}{\partial y}(x, 0) \cdot y + \langle s(x, y), y \rangle$$

where $\langle\cdot, \cdot\rangle$ is the inner product in $\mathbb{R}^k$ and $s: U \times \mathbb{R}^k \rightarrow \mathbb{R}^k$ is a $C^\infty$ map with $s(x, 0) = 0$.

The first coordinate of (the local representation of) $H$ defines a $C^\infty$ map $U \times \mathbb{R}^m \times I \rightarrow \mathbb{R}^m$. The second coordinate of $H$ is given by the formula

$$\frac{\partial g_2}{\partial y}(x, 0) \cdot y + \langle s(x, ty), y \rangle, \quad 0 \leq t \leq 1.$$

Clearly this is $C^\infty$ in $(t, x, y)$. Thus $H$ is $C^\infty$; and it is easily verified that $H$ is an isotopy.

**Step 3: The isotopy of tubular neighborhoods.**

An isotopy of tubular neighborhoods from $(f_0, \xi_0)$ to $(f_1, \xi_1)$ is now defined by

$$F(x, t) = f_1 H(x, 1 - t), \quad (x, t) \in E_0 \times I,$$

under the assumption that $f_0(E_0) \subset f_1(E_1)$. Combined with the shrinking isotopy from Step 1, this gives an isotopy between $(f_0, \xi_0)$ and $(f_1, \xi_1)$ in the general case. ∎
