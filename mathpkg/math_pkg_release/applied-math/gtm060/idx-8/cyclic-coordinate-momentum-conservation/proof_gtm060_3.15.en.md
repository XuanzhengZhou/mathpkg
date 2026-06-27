---
role: proof
locale: en
of_concept: cyclic-coordinate-momentum-conservation
source_book: gtm060
source_chapter: "3"
source_section: "15"
---

From Hamilton's equations, $\dot{p}_1 = -\partial H/\partial q_1$. If $\partial H/\partial q_1 = 0$, then $\dot{p}_1 = 0$, so $p_1 = \text{const}$.

Once the reduced system of $2n-2$ equations for $\mathbf{p}'(t)$ and $\mathbf{q}'(t)$ is solved, the value of $p_1$ enters only as a parameter in the Hamiltonian function. The equation for the cyclic coordinate $q_1$ becomes

$$\frac{d}{dt} q_1 = \frac{\partial H}{\partial p_1}(p_1, \mathbf{p}'(t), \mathbf{q}'(t), t) = f(t),$$

which is integrated directly: $q_1(t) = \int f(t) \, dt + \text{const}$.
