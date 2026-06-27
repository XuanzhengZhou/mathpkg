---
role: introduce
locale: en
content_hash: ""
written_against: ""
---

Linearization replaces a nonlinear differential equation near an equilibrium point with its first-order Taylor approximation. The resulting linear system $\dot{y} = Ay$ can be solved explicitly via the matrix exponential $y(t) = e^{At} y(0)$, providing local information about the behavior of the original nonlinear system. The linear operator $A$ is the Jacobian matrix of $f$ evaluated at the equilibrium.
