---
role: proof
locale: en
of_concept: inertia-operator-symmetry
source_book: gtm060
source_chapter: "6"
source_section: "C"
---

By definition of angular momentum of a point mass $m$ at position $\mathbf{q}$ with velocity $\mathbf{v}$:

$$\mathbf{m} = [\mathbf{q}, m\mathbf{v}] = m[\mathbf{q}, [\omega, \mathbf{q}]].$$

In the body frame $K$, this becomes $\mathbf{M} = m[\mathbf{Q}, [\Omega, \mathbf{Q}]]$, defining the linear operator $A\Omega = \mathbf{M}$.

For any $\mathbf{X}, \mathbf{Y} \in K$, using the vector triple product identity $([\mathbf{a}, \mathbf{b}], \mathbf{c}) = ([\mathbf{c}, \mathbf{a}], \mathbf{b})$:

$$(A\mathbf{X}, \mathbf{Y}) = m([\mathbf{Q}, [\mathbf{X}, \mathbf{Q}]], \mathbf{Y}) = m([\mathbf{Y}, \mathbf{Q}], [\mathbf{X}, \mathbf{Q}]).$$

The right-hand side is manifestly symmetric in $\mathbf{X}$ and $\mathbf{Y}$, therefore:

$$(A\mathbf{X}, \mathbf{Y}) = (\mathbf{X}, A\mathbf{Y}).$$

Hence $A$ is a symmetric operator.
