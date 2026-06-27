---
role: proof
locale: en
of_concept: jacobi-criterion-nonsingularity
source_book: gtm044
source_chapter: "II"
source_section: "7"
---

# Proof of Jacobi Criterion for Nonsingularity (Theorem 7.4)

**Theorem.** Let $p(X,Y) \in \mathbb{C}[X,Y]$ have no repeated factors. Then $V(p) \subset \mathbb{C}_{XY}$ is smooth at $P \in V(p)$ if and only if at least one of the following holds:

$$\frac{\partial p}{\partial X}(P) \neq 0, \quad \frac{\partial p}{\partial Y}(P) \neq 0.$$

*Proof.* Write $\mathbb{C}_{XY} = \mathbb{R}_{X_1 X_2 Y_1 Y_2} = \mathbb{R}^4$, where $X = X_1 + i X_2$ and $Y = Y_1 + i Y_2$. Without loss of generality, apply an affine translation so that $P = (0) \in \mathbb{R}^4$. Since we are proving smoothness, we may assume the part of $\mathbf{V}(p)$ near $(0)$ is the graph of a smooth function $f = (f_1, f_2)$, i.e.,

$$(Y_1, Y_2) = (f_1(X_1, X_2), f_2(X_1, X_2)) : U \to U'$$

for some open sets $U$ and $U'$ containing $0$ in $\mathbb{R}_{X_1 X_2}$ and $\mathbb{R}_{Y_1 Y_2}$ respectively. Since $f_1$ and $f_2$ are smooth, there exist in $\mathbb{R}^4$ real 3-spaces

$$Y_1 = c_{11} X_1 + c_{12} X_2 \quad \text{and} \quad Y_2 = c_{21} X_1 + c_{22} X_2$$

which locally approximate $f_1$ and $f_2$, these 3-spaces intersecting in a real tangent plane $T$. (Here $c_{ij} = \frac{\partial f_i}{\partial X_j}(0)$.)

We note two facts about the plane $T$:

**(7.6)** This real 2-space is actually a complex 1-space.

**(7.7)** Let $F_i = Y_i - f_i(X_1, X_2)$, $i = 1, 2$. For each real line in $T$ through $(0)$, the corresponding directional derivative at $(0)$ of each $F_i$ is zero.

We now apply a linear transformation of $\mathbb{C}_{XY}$ that sends the tangent plane $T$ to the $X$-axis. The derivatives (and hence the coordinate axes) change according to the inverse transformation. By the Implicit Function Theorem (Theorem 3.6), the part of $V(p)$ near $(0)$ is also a graph of a function relative to these new coordinates.

Now consider two cases.

**Case 1.** Suppose $(\partial p / \partial X)(0) = (\partial p / \partial Y)(0) = 0$. Then $p$ has zero derivative in every direction. Indeed, for any linear change of coordinates $X = \alpha X' + \beta Y'$, $Y = \gamma X' + \delta Y'$, let $p^*(\alpha X' + \beta Y', \gamma X' + \delta Y') = p^*(X', Y')$. By the chain rule,

$$\frac{\partial p^*}{\partial X'} = \frac{\partial p}{\partial X} \cdot \alpha + \frac{\partial p}{\partial Y} \cdot \gamma, \quad \frac{\partial p^*}{\partial Y'} = \frac{\partial p}{\partial X} \cdot \beta + \frac{\partial p}{\partial Y} \cdot \delta.$$

Since both $\partial p/\partial X$ and $\partial p/\partial Y$ vanish at $(0)$, so do $\partial p^*/\partial X'$ and $\partial p^*/\partial Y'$. Hence $p^*(X', Y')$ expanded about $(0,0)$ has order $s \geq 2$.

Now choose coordinates so that $(Y')^s$ is a term of $p^*(X', Y')$ when expanded about $(0,0)$. (A proof of this is similar to that of Assumption 4.2; for "almost all" choices of $\varepsilon$, the substitution $X' = X'' + \varepsilon Y''$ and $Y' = Y''$ will bring this about.) We continue to denote these new coordinates by $X'$ and $Y'$. Note that if a polynomial has no repeated factors it will continue to have no repeated factors after a linear change of coordinates. Therefore $\mathcal{D}_{Y'}(p^*(X', Y')) \not\equiv 0$—that is, at all but finitely many values of $x'$, $p^*(x', Y')$ has exactly $n = \deg p$ zeros. But we know $p^*(0, Y')$ has $Y' = 0$ as a zero of order $s \geq 2$, since $p^*(0, Y')$ is a polynomial in $Y'$ of order $s$.

Now one can apply the Argument Principle (Theorem 3.8), much as in the proof of Theorem 3.6 or as in Section 4 where we determined the structure of $C$ at the finitely many exceptional points, to conclude that:

When $x' \neq 0$ is sufficiently small, the $n$ zeros of $p^*(x', Y')$ form $s$ groups, each being the $s$-th roots of some number varying analytically with $x'$. Hence as $x'$ goes around $0$ in a small circle, the $n$ sheets are permuted in a nontrivial way—the curve has a ramp point at $(0)$, so $V(p)$ is singular at $P$.

**Case 2.** Suppose $(\partial p / \partial X)(P) \neq 0$ or $(\partial p / \partial Y)(P) \neq 0$. Then by the Implicit Function Theorem in the complex-analytic category (which follows from the real Implicit Function Theorem together with the Cauchy–Riemann equations), $V(p)$ is locally the graph of a complex-analytic function of one variable near $P$. A complex-analytic function is smooth (in fact, real-analytic), so $V(p)$ is smooth at $P$. This completes the proof of both directions. $\square$
