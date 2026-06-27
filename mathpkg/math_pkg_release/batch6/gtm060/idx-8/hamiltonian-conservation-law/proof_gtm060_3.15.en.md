---
role: proof
locale: en
of_concept: hamiltonian-conservation-law
source_book: gtm060
source_chapter: "3"
source_section: "15"
---

Consider the variation of $H$ along a trajectory $H(\mathbf{p}(t), \mathbf{q}(t), t)$. By the chain rule and Hamilton's equations,

$$\frac{dH}{dt} = \frac{\partial H}{\partial \mathbf{p}} \dot{\mathbf{p}} + \frac{\partial H}{\partial \mathbf{q}} \dot{\mathbf{q}} + \frac{\partial H}{\partial t}.$$

Substituting Hamilton's equations $\dot{\mathbf{p}} = -\partial H/\partial \mathbf{q}$ and $\dot{\mathbf{q}} = \partial H/\partial \mathbf{p}$:

$$\frac{dH}{dt} = \frac{\partial H}{\partial \mathbf{p}} \left( -\frac{\partial H}{\partial \mathbf{q}} \right) + \frac{\partial H}{\partial \mathbf{q}} \left( \frac{\partial H}{\partial \mathbf{p}} \right) + \frac{\partial H}{\partial t} = \frac{\partial H}{\partial t}.$$

The first two terms cancel, proving the result. When $\partial H/\partial t = 0$, we obtain $dH/dt = 0$, so $H$ is constant along trajectories.
