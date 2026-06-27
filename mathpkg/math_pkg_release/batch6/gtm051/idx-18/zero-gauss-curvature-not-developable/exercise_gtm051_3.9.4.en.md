---
role: exercise
locale: en
chapter: "3"
section: "3.9"
exercise_number: 4
---

**3.9.4 A surface with $K = 0$ which is not a developable surface.** We construct a surface $f: \mathbb{R} \times {]-1,1[} \to \mathbb{R}^3$ whose first and second fundamental forms satisfy
$$g_{ik} = \delta_{ik},$$
$$h_{ik} = P_{ik}(u,v) \, e^{-((1 \pm v)/u)^2},$$
where
$$P_{11} = \frac{1}{1 \pm v}, \quad P_{12} = \mp \frac{u}{(1 \pm v)^2}, \quad P_{22} = \frac{u^2}{(1 \pm v)^3},$$
using the upper sign for $u \geq 0$ and the lower sign for $u \leq 0$.

(a) Show that the $h_{ik}$ are differentiable.
(b) Show that $h_{11}h_{22} - h_{12}^2 = 0$, hence $K = 0$.
(c) Verify that $h_{11,2} = h_{12,1}$ and $h_{22,1} = h_{12,2}$.
(d) From (b) and (c), prove that the first and second fundamental forms satisfy the Gauss and Codazzi-Mainardi equations. By the fundamental theorem of surface theory (3.8.8), there exists a surface $f$ with the required first and second fundamental forms, unique up to an isometry of $\mathbb{R}^3$.
(e) The second fundamental form has been chosen so that the inverse image of the generators of $f$ in the set $u < 0$ are the straight lines through $(0,1)$. In the set $u > 0$, they are the straight lines through $(0,-1)$. The slope of these straight lines blows up as one moves through $(0,0)$ on the $u$-axis.
(f) Prove that $f$ is not a developable surface near $(0,0)$: there is no change of variables $\phi: V \to U' \subset U$, $(0,0) \in U'$, such that $f \circ \phi(s,t) = sX(t) + c(t)$.
