---
role: exercise
locale: en
chapter: "5"
section: "5.7"
exercise_number: 2
---

Suppose $f: U \to \mathbb{R}^3$ is a parameterized surface in the sense of (3.1.1). If $x, y,$ and $z$ are the coordinates in $\mathbb{R}^3$, we may consider $x \circ f(u), y \circ f(u),$ and $z \circ f(u)$ as functions on the surface $M$, represented in the coordinate chart and metric $(U, g) = (U, I)$. Here $g_u = I_u$ is the first fundamental form.

Show:

$$\Delta f(u) := (\Delta(x \circ f(u)), \Delta(y \circ f(u)), \Delta(z \circ f(u))) = 2H(u)\,n(u),$$

where $H$ is the mean curvature and $n$ is the unit normal vector field on the surface $f$.

**Remark.** This formula can be found in the proof of (6.2.9).

It follows from this formula that minimal surfaces, i.e., surfaces $f$ which satisfy $H = 0$, are characterized by the fact that their three coordinate functions are harmonic.
