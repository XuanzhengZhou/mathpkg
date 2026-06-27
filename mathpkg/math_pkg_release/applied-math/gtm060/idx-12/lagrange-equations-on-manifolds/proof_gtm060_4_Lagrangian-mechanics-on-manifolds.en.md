---
role: proof
locale: en
of_concept: lagrange-equations-on-manifolds
source_book: gtm060
source_chapter: "4"
source_section: "Lagrangian mechanics on manifolds"
---

The proof follows from the variational principle applied to the action functional on the manifold. Let $\gamma: [t_0, t_1] \to M$ be a smooth curve and consider the action

$$S[\gamma] = \int_{t_0}^{t_1} L(\gamma(t), \dot{\gamma}(t)) \, dt.$$

In local coordinates $q = (q_1, \ldots, q_n)$ on $M$, the tangent vector $\dot{\gamma}(t)$ has coordinates $(\dot{q}_1, \ldots, \dot{q}_n)$, and the Lagrangian is expressed as $L(q, \dot{q})$. A variation $\gamma_\varepsilon$ of $\gamma$ with fixed endpoints corresponds to a variation $q(t) + \varepsilon \delta q(t)$ in coordinates, with $\delta q(t_0) = \delta q(t_1) = 0$. Computing the first variation:

$$\frac{d}{d\varepsilon}\bigg|_{\varepsilon=0} S[\gamma_\varepsilon] = \int_{t_0}^{t_1} \sum_{i=1}^{n} \left( \frac{\partial L}{\partial q_i} \delta q_i + \frac{\partial L}{\partial \dot{q}_i} \delta \dot{q}_i \right) dt.$$

Integrating by parts using $\delta \dot{q}_i = \frac{d}{dt}(\delta q_i)$ and the boundary conditions $\delta q_i(t_0) = \delta q_i(t_1) = 0$:

$$\frac{d}{d\varepsilon}\bigg|_{\varepsilon=0} S[\gamma_\varepsilon] = \int_{t_0}^{t_1} \sum_{i=1}^{n} \left( \frac{\partial L}{\partial q_i} - \frac{d}{dt}\frac{\partial L}{\partial \dot{q}_i} \right) \delta q_i \, dt.$$

Since the variations $\delta q_i$ are arbitrary, the principle of stationary action implies the Euler-Lagrange equations

$$\frac{d}{dt} \frac{\partial L}{\partial \dot{q}_i} = \frac{\partial L}{\partial q_i}, \qquad i = 1, \ldots, n.$$

Although these equations were derived using coordinates, they are invariant under coordinate changes on $M$, as can be verified by the transformation law for the Euler-Lagrange operator.
