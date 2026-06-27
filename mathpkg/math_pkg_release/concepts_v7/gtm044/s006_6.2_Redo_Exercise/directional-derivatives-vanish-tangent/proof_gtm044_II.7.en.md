---
role: proof
locale: en
of_concept: directional-derivatives-vanish-tangent
source_book: gtm044
source_chapter: "II"
source_section: "7"
---

# Proof of Vanishing of Directional Derivatives on the Tangent Plane (7.7)

**Statement.** Let $F_i = Y_i - f_i(X_1, X_2)$ for $i = 1, 2$. For each real line in the tangent plane $T$ through the origin, the corresponding directional derivative at $(0)$ of each $F_i$ is zero.

*Proof.* Write $\mathbb{C}_{XY} = \mathbb{R}_{X_1 X_2 Y_1 Y_2} = \mathbb{R}^4$. As before, assume the smooth point is at the origin and $V(p)$ is locally the graph of a smooth function $f = (f_1, f_2)$. Define

$$F_i(X_1, X_2, Y_1, Y_2) = Y_i - f_i(X_1, X_2), \qquad i = 1, 2.$$

The tangent plane $T$ at the origin is given by the linear equations

$$Y_i = c_{i1} X_1 + c_{i2} X_2 \qquad (i = 1, 2),$$

where $c_{ij} = \frac{\partial f_i}{\partial X_j}(0)$. By differentiability of $f_i$, we have

$$\lim_{(x_1, x_2) \to 0} \frac{f_i(x_1, x_2) - (c_{i1} x_1 + c_{i2} x_2)}{|x_1| + |x_2|} = 0 \qquad (i = 1, 2).$$

Equivalently,

$$\lim_{(x_1, x_2, y_1, y_2) \to 0} \frac{\bigl(y_i - f_i(x_1, x_2)\bigr) - \bigl(y_i - (c_{i1} x_1 + c_{i2} x_2)\bigr)}{|x_1| + |x_2|} = 0 \qquad (i = 1, 2). \tag{1}$$

Now consider points that approach the origin *along* the tangent plane $T$. For any point $(x_1, x_2, y_1, y_2) \in T$, we have by definition $y_i - (c_{i1} x_1 + c_{i2} x_2) = 0$. Substituting this into (1), the second term in the numerator vanishes, leaving

$$\lim_{\substack{(x_1, x_2, y_1, y_2) \to 0 \\ (x_1, x_2, y_1, y_2) \in T}} \frac{y_i - f_i(x_1, x_2)}{|x_1| + |x_2|} = 0.$$

That is,

$$\lim_{\substack{(x_1, x_2, y_1, y_2) \to 0 \\ (x_1, x_2, y_1, y_2) \in T}} \frac{F_i(x_1, x_2, y_1, y_2)}{|x_1| + |x_2|} = 0. \tag{2}$$

Now let $v = (v_1, v_2, v_3, v_4) \in T$ be any nonzero tangent vector. For a curve $\gamma(t) = t v$ lying in $T$ (since $T$ is a linear subspace), the directional derivative of $F_i$ at the origin in the direction $v$ is

$$D_v F_i(0) = \lim_{t \to 0} \frac{F_i(t v) - F_i(0)}{t} = \lim_{t \to 0} \frac{F_i(t v)}{t},$$

since $F_i(0) = 0 - f_i(0,0) = 0$ (the origin lies on $V(p)$). Equation (2) implies that this limit is zero, because $|t v| = |t| \|v\|$ and $|x_1| + |x_2|$ is comparable to $|t|$ along any line through the origin (provided the projection of $v$ onto the $(X_1, X_2)$-coordinates is nonzero; if it is zero, the limit is trivially zero since $F_i$ then depends only on $Y_i$). Hence $D_v F_i(0) = 0$ for every $v \in T$ and $i = 1, 2$. $\square$
