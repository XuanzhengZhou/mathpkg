---
role: proof
locale: en
of_concept: lagrange-hamilton-equivalence
source_book: gtm060
source_chapter: "3"
source_section: "15"
---

By definition, the Legendre transform of $L(\mathbf{q}, \dot{\mathbf{q}}, t)$ with respect to $\dot{\mathbf{q}}$ is the function

$$H(\mathbf{p}) = \mathbf{p} \dot{\mathbf{q}} - L(\mathbf{q}, \dot{\mathbf{q}}, t),$$

where $\dot{\mathbf{q}}$ is expressed in terms of $\mathbf{p}$ via the relation $\mathbf{p} = \partial L / \partial \dot{\mathbf{q}}$.

The total differential of the Hamiltonian function $H(\mathbf{p}, \mathbf{q}, t) = \mathbf{p} \dot{\mathbf{q}} - L(\mathbf{q}, \dot{\mathbf{q}}, t)$ is

$$dH = \frac{\partial H}{\partial \mathbf{p}} d\mathbf{p} + \frac{\partial H}{\partial \mathbf{q}} d\mathbf{q} + \frac{\partial H}{\partial t} dt.$$

On the other hand, from the definition of $H$:

$$dH = \dot{\mathbf{q}} \, d\mathbf{p} + \mathbf{p} \, d\dot{\mathbf{q}} - \frac{\partial L}{\partial \dot{\mathbf{q}}} d\dot{\mathbf{q}} - \frac{\partial L}{\partial \mathbf{q}} d\mathbf{q} - \frac{\partial L}{\partial t} dt.$$

Since $\mathbf{p} = \partial L / \partial \dot{\mathbf{q}}$, the terms with $d\dot{\mathbf{q}}$ cancel, yielding

$$dH = \dot{\mathbf{q}} \, d\mathbf{p} - \frac{\partial L}{\partial \mathbf{q}} d\mathbf{q} - \frac{\partial L}{\partial t} dt.$$

Comparing the two expressions for $dH$, we obtain:

$$\dot{\mathbf{q}} = \frac{\partial H}{\partial \mathbf{p}}, \qquad \frac{\partial H}{\partial \mathbf{q}} = -\frac{\partial L}{\partial \mathbf{q}} = -\dot{\mathbf{p}}, \qquad \frac{\partial H}{\partial t} = -\frac{\partial L}{\partial t}.$$

Applying Lagrange's equations $\dot{\mathbf{p}} = \partial L / \partial \mathbf{q}$, we obtain Hamilton's equations

$$\dot{\mathbf{p}} = -\frac{\partial H}{\partial \mathbf{q}}, \qquad \dot{\mathbf{q}} = \frac{\partial H}{\partial \mathbf{p}}.$$

Conversely, if $(\mathbf{p}(t), \mathbf{q}(t))$ satisfies Hamilton's equations, then reversing the argument shows that $\mathbf{q}(t)$ satisfies Lagrange's equations. Therefore, the systems are equivalent.
