---
role: proof
locale: en
of_concept: tangent-space-basis
source_book: gtm035
source_chapter: "4"
source_section: "4.1"
---

# Proof of Basis of Tangent Space

**Lemma 4.1.** $\partial/\partial x_1|_x, \ldots, \partial/\partial x_N|_x$ forms a basis for $T_x$.

## Proof

Recall that $T_x$ is the collection of all maps $v: C^\infty \to \mathbb{C}$ satisfying:
- (a) $v$ is linear.
- (b) $v(f \cdot g) = f(x) \cdot v(g) + g(x) \cdot v(f)$ for all $f, g \in C^\infty$.

The operators $\partial/\partial x_j|_x$ are defined by
$$\frac{\partial}{\partial x_j}\bigg|_x(f) = \frac{\partial f}{\partial x_j}(x).$$

First, verify that each $\partial/\partial x_j|_x$ belongs to $T_x$: linearity is clear, and property (b) is the Leibniz rule for partial derivatives.

**Step 1: Linear independence.** Suppose
$$\sum_{j=1}^{N} c_j \frac{\partial}{\partial x_j}\bigg|_x = 0$$
for scalars $c_j \in \mathbb{C}$. Apply this to the coordinate function $x_k$ (which lies in $C^\infty$). Then
$$0 = \sum_{j=1}^{N} c_j \frac{\partial x_k}{\partial x_j}(x) = c_k,$$
since $\partial x_k/\partial x_j = \delta_{kj}$. Hence $c_k = 0$ for all $k$, proving linear independence.

**Step 2: Spanning.** Let $v \in T_x$ be an arbitrary tangent vector. Define constants $c_j = v(x_j)$ for $j = 1, \ldots, N$, where $x_j$ is the $j$-th coordinate function. We claim that
$$v = \sum_{j=1}^{N} c_j \frac{\partial}{\partial x_j}\bigg|_x.$$

For any $f \in C^\infty$, write the first-order Taylor expansion about $x = (x_1^0, \ldots, x_N^0)$:
$$f(y) = f(x) + \sum_{j=1}^{N} \frac{\partial f}{\partial x_j}(x)(y_j - x_j^0) + o(|y-x|).$$

By properties (a) and (b) of tangent vectors, $v$ applied to a constant function yields $0$ (since $v(1) = v(1 \cdot 1) = 1 \cdot v(1) + 1 \cdot v(1) = 2v(1)$, so $v(1) = 0$). Moreover, $v$ vanishes on functions vanishing to order $\ge 2$ at $x$ (a standard consequence of (a) and (b)). Applying $v$ to the Taylor expansion gives:
$$v(f) = \sum_{j=1}^{N} \frac{\partial f}{\partial x_j}(x) \, v(x_j - x_j^0) = \sum_{j=1}^{N} \frac{\partial f}{\partial x_j}(x) \, v(x_j).$$

Since $c_j = v(x_j)$ and $v(x_j^0) = 0$ (constant function), we obtain
$$v(f) = \sum_{j=1}^{N} c_j \frac{\partial f}{\partial x_j}(x) = \left(\sum_{j=1}^{N} c_j \frac{\partial}{\partial x_j}\bigg|_x\right)(f).$$

Thus $v$ is expressed as a linear combination of the $\partial/\partial x_j|_x$, proving they span $T_x$.

Therefore $\{\partial/\partial x_1|_x, \ldots, \partial/\partial x_N|_x\}$ is a basis for $T_x$. $\square$
