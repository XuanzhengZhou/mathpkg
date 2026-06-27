---
role: proof
locale: en
of_concept: noethers-theorem
source_book: gtm060
source_chapter: "7"
source_section: "14"
---

Let $\Phi : \mathbb{R} \times \mathbb{R} \to M$ be a two-parameter family of curves, where $\Phi(s, \cdot) : \mathbb{R} \to M$ satisfies Lagrange's equations for each fixed $s$. Define the action functional

$$\Phi(s) = \int_{t_0}^{t_1} L(\Phi(s, t), \dot{\Phi}(s, t)) \, dt.$$

If the one-parameter group $h^s$ preserves the Lagrangian, then $\Phi(s)$ is independent of $s$, i.e., $d\Phi/ds = 0$. Computing the derivative:

$$\frac{d\Phi}{ds} = \int_{t_0}^{t_1} \left[ \frac{\partial L}{\partial \mathbf{q}} \mathbf{q}' + \frac{\partial L}{\partial \dot{\mathbf{q}}} \dot{\mathbf{q}}' \right] dt,$$

where $\mathbf{q}' = (d/ds)\Phi(s, t)$ and $\dot{\mathbf{q}}' = (d/ds)\dot{\Phi}(s, t)$.

Since $\Phi(s, \cdot)$ satisfies Lagrange's equation for each $s$,

$$\frac{\partial}{\partial t} \left[ \frac{\partial L}{\partial \dot{\mathbf{q}}} (\Phi(s, t), \dot{\Phi}(s, t)) \right] = \frac{\partial L}{\partial \mathbf{q}} (\Phi(s, t), \dot{\Phi}(s, t)).$$

Let $F(s, t) = (\partial L / \partial \dot{\mathbf{q}})(\Phi(s, t), \dot{\Phi}(s, t))$. Substituting $\partial F / \partial t$ for $\partial L / \partial \mathbf{q}$:

$$\frac{d\Phi}{ds} = \int_{t_0}^{t_1} \left[ \frac{d}{dt} \frac{\partial L}{\partial \dot{\mathbf{q}}} \mathbf{q}' + \frac{\partial L}{\partial \dot{\mathbf{q}}} \frac{d}{dt} \mathbf{q}' \right] dt = \int_{t_0}^{t_1} \frac{d}{dt} \left( \frac{\partial L}{\partial \dot{\mathbf{q}}} \mathbf{q}' \right) dt.$$

Therefore,

$$\frac{d\Phi}{ds} = \left. \left( \frac{\partial L}{\partial \dot{\mathbf{q}}} \mathbf{q}' \right) \right|_{t_0}^{t_1}.$$

If we take variations $\mathbf{q}'(t_0) = \mathbf{q}'(t_1) = 0$, then $d\Phi/ds = 0$, confirming the Lagrangian is preserved. More generally, the quantity

$$I = \frac{\partial L}{\partial \dot{\mathbf{q}}} \mathbf{q}'$$

is conserved along solutions, i.e., $dI/dt = 0$, which follows directly from the computation above.

The value of $I(v)$ is independent of the choice of local coordinates $\mathbf{q}$. Indeed, $I$ is the rate of change of $L(v)$ when the vector $v \in TM_x$ varies inside $TM_x$ with velocity $(d/ds)|_{s=0} h^s x$. Therefore $I(v)$ is well defined as a function of the tangent vector $v \in TM_x$.
