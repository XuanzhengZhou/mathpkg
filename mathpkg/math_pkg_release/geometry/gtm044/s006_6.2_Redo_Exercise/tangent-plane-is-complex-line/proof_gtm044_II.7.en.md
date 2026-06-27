---
role: proof
locale: en
of_concept: tangent-plane-is-complex-line
source_book: gtm044
source_chapter: "II"
source_section: "7"
---

# Proof of Tangent Plane as a Complex Line (7.6)

**Statement.** The real 2-dimensional tangent plane $T$ to a smooth complex algebraic curve $V(p) \subset \mathbb{C}_{XY}$ at a smooth point is actually a complex 1-dimensional subspace.

*Proof.* Write $\mathbb{C}_{XY} = \mathbb{R}_{X_1 X_2 Y_1 Y_2} = \mathbb{R}^4$ with $X = X_1 + iX_2$, $Y = Y_1 + iY_2$. Assume without loss of generality that the smooth point is at the origin $(0,0,0,0) \in \mathbb{R}^4$ and that $V(p)$ is locally the graph of a smooth function $f = (f_1, f_2)$:

$$(Y_1, Y_2) = (f_1(X_1, X_2), f_2(X_1, X_2))$$

for $(X_1, X_2)$ in an open neighborhood of $0 \in \mathbb{R}^2$.

Because $V(p)$ is defined by the zero set of the complex polynomial $p(X,Y)$, the function

$$F(X_1 + iX_2) = f_1(X_1, X_2) + i f_2(X_1, X_2)$$

is holomorphic in the complex variable $X = X_1 + iX_2$. Therefore $f_1$ and $f_2$ satisfy the Cauchy–Riemann equations:

$$\frac{\partial f_1}{\partial X_1} = \frac{\partial f_2}{\partial X_2}, \qquad \frac{\partial f_1}{\partial X_2} = -\frac{\partial f_2}{\partial X_1}.$$

The tangent plane $T$ to $V(p)$ at $(0)$ is given by the real linear approximation:

$$Y_1 = \frac{\partial f_1}{\partial X_1}(0) X_1 + \frac{\partial f_1}{\partial X_2}(0) X_2,$$
$$Y_2 = \frac{\partial f_2}{\partial X_1}(0) X_1 + \frac{\partial f_2}{\partial X_2}(0) X_2.$$

Let $a = \frac{\partial f_1}{\partial X_1}(0)$ and $b = \frac{\partial f_1}{\partial X_2}(0)$. By the Cauchy–Riemann equations, we have $\frac{\partial f_2}{\partial X_1}(0) = -b$ and $\frac{\partial f_2}{\partial X_2}(0) = a$. Thus the tangent plane equations become:

$$Y_1 = a X_1 + b X_2,$$
$$Y_2 = -b X_1 + a X_2.$$

Now combine these into a single complex equation by multiplying the second by $i$ and adding to the first:

$$Y_1 + i Y_2 = (a X_1 + b X_2) + i(-b X_1 + a X_2) = (a - ib)(X_1 + i X_2).$$

That is,

$$Y = c X, \quad \text{where} \quad c = a - ib = \frac{\partial f_1}{\partial X_1}(0) - i \frac{\partial f_1}{\partial X_2}(0) \in \mathbb{C}.$$

This is a complex-linear equation: it defines a 1-dimensional complex subspace of $\mathbb{C}^2$. As a real subspace, it is 2-dimensional, which coincides with the tangent plane $T$. Hence the real tangent plane $T$ is actually a complex line. $\square$
