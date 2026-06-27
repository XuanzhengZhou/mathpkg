---
role: proof
locale: en
of_concept: hamiltonian-as-total-energy
source_book: gtm060
source_chapter: "3"
source_section: "15"
---

The proof relies on the following lemma on the Legendre transform of a quadratic form.

**Lemma.** The values of a quadratic form $f(\mathbf{x})$ and of its Legendre transform $g(\mathbf{p})$ coincide at corresponding points: $f(\mathbf{x}) = g(\mathbf{p})$.

*Proof of the Lemma.* By Euler's theorem on homogeneous functions, $(\partial f / \partial \mathbf{x}) \mathbf{x} = 2f$. Therefore,

$$g(\mathbf{p}(\mathbf{x})) = \mathbf{p}\mathbf{x} - f(\mathbf{x}) = (\partial f / \partial \mathbf{x})\mathbf{x} - f = 2f(\mathbf{x}) - f(\mathbf{x}) = f(\mathbf{x}).$$

Returning to the main theorem: the Hamiltonian is defined as the Legendre transform of $L$ with respect to $\dot{\mathbf{q}}$:

$$H(\mathbf{p}, \mathbf{q}, t) = \mathbf{p}\dot{\mathbf{q}} - L(\mathbf{q}, \dot{\mathbf{q}}, t) = \mathbf{p}\dot{\mathbf{q}} - (T - U).$$

Since $T$ is a quadratic form in $\dot{\mathbf{q}}$, by the lemma, $\mathbf{p}\dot{\mathbf{q}} = 2T$. Here $\mathbf{p} = \partial L / \partial \dot{\mathbf{q}} = \partial T / \partial \dot{\mathbf{q}}$, and $T$ is homogeneous of degree 2 in $\dot{\mathbf{q}}$. Thus

$$H = 2T - (T - U) = T + U.$$

For example, with $T = \frac{1}{2} m \dot{x}^2$, we have $p = m\dot{x}$, and the Legendre transform of $T$ is $p^2/2m = \frac{1}{2} m \dot{x}^2 = T$, confirming the lemma.
