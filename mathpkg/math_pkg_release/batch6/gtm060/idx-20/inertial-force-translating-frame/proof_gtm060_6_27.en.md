---
role: proof
locale: en
of_concept: inertial-force-translating-frame
source_book: gtm060
source_chapter: "6"
source_section: "27"
---

Let $k$ be an inertial coordinate system and $K$ a coordinate system moving by translation relative to $k$, so that the position of the origin of $K$ in $k$ is $r(t)$. For a point with radius vector $q$ in $k$ and $Q$ in $K$, we have $Q = q - r(t)$.

The equations of motion in the inertial system $k$ are Newton's equations:
$$
m\ddot{q} = f(q, \dot{q}).
$$

Differentiating $Q = q - r(t)$ twice gives
$$
\ddot{Q} = \ddot{q} - \ddot{r}.
$$

Multiplying by $m$ and substituting $\ddot{q}$ from Newton's equation:
$$
m\ddot{Q} = f(q, \dot{q}) - m\ddot{r}.
$$

Expressing the force in terms of the coordinates in $K$, we obtain
$$
m\ddot{Q} = F(Q, \dot{Q}) - m\ddot{r},
$$
where $F(Q, \dot{Q}) = f(Q + r, \dot{Q} + \dot{r})$ is the physical force expressed in the moving coordinates.

Thus the motion in $K$ satisfies an equation of the same form as Newton's equation, but with an additional term $-m\ddot{r}$ which plays the role of a uniform force field. This additional term is the inertial force.
