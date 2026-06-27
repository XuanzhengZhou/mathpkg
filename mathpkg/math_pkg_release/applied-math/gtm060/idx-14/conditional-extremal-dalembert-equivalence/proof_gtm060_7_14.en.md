---
role: proof
locale: en
of_concept: conditional-extremal-dalembert-equivalence
source_book: gtm060
source_chapter: "7"
source_section: "14"
---

Consider two curves $\mathbf{x}(t)$ and $\mathbf{x}(t) + \xi(t)$ on $M$, where $\xi(t)$ is a small tangent vector field with $\xi(t_0) = \xi(t_1) = 0$. Compare the values of the action functional $\Phi$ on these two curves. Computing the first variation:

$$\delta_M \Phi = \int_{t_0}^{t_1} \left[ \frac{\partial L}{\partial \mathbf{x}} \xi + \frac{\partial L}{\partial \dot{\mathbf{x}}} \dot{\xi} \right] dt.$$

For $L = \dot{\mathbf{x}}^2/2 - U(\mathbf{x})$, we have $\partial L/\partial \mathbf{x} = -\partial U/\partial \mathbf{x}$ and $\partial L/\partial \dot{\mathbf{x}} = \dot{\mathbf{x}}$. Integrating by parts:

$$\delta_M \Phi = \int_{t_0}^{t_1} \left( -\frac{\partial U}{\partial \mathbf{x}} \xi + \dot{\mathbf{x}} \dot{\xi} \right) dt = \left[ \dot{\mathbf{x}} \xi \right]_{t_0}^{t_1} - \int_{t_0}^{t_1} \left( \ddot{\mathbf{x}} + \frac{\partial U}{\partial \mathbf{x}} \right) \xi \, dt.$$

Since $\xi(t_0) = \xi(t_1) = 0$, the boundary term vanishes, yielding

$$\delta_M \Phi = - \int_{t_0}^{t_1} \left( \ddot{\mathbf{x}} + \frac{\partial U}{\partial \mathbf{x}} \right) \xi \, dt.$$

The condition $\delta_M \Phi = 0$ for all $\xi(t) \in TM_{\mathbf{x}(t)}$ with $\xi(t_0) = \xi(t_1) = 0$ is therefore equivalent to

$$\int_{t_0}^{t_1} \left( \ddot{\mathbf{x}} + \frac{\partial U}{\partial \mathbf{x}} \right) \xi \, dt = 0$$

for all such $\xi$. By the normal field lemma (setting $\mathbf{f} = \ddot{\mathbf{x}} + \partial U / \partial \mathbf{x}$), this integral condition is equivalent to

$$\left( \ddot{\mathbf{x}} + \frac{\partial U}{\partial \mathbf{x}}, \xi \right) = 0, \quad \forall \xi \in TM_{\mathbf{x}},$$

which is precisely D'Alembert's equation.
