---
role: proof
locale: en
of_concept: unitification-construction
source_book: gtm015
source_chapter: "VI"
source_section: "49"
---

# Proof of the Unitification of an Algebra

Suppose $A$ is an associative algebra over $\mathbb{C}$ (with or without a unity element). Define $A_1 = A \times \mathbb{C}$ with the following operations:

$$(x, \lambda) + (y, \mu) = (x + y, \lambda + \mu),$$
$$\mu(x, \lambda) = (\mu x, \mu \lambda),$$
$$(x, \lambda)(y, \mu) = (xy + \mu x + \lambda y, \lambda \mu).$$

**Associativity of multiplication:** For $(x, \lambda), (y, \mu), (z, \nu) \in A_1$,
$$[(x,\lambda)(y,\mu)](z,\nu) = (xy + \mu x + \lambda y, \lambda\mu)(z,\nu)$$
$$= ((xy + \mu x + \lambda y)z + \nu(xy + \mu x + \lambda y) + \lambda\mu z, \lambda\mu\nu)$$
$$= (x(yz) + \mu(xz) + \lambda(yz) + \nu x y + \nu\mu x + \nu\lambda y + \lambda\mu z, \lambda\mu\nu).$$

On the other hand,
$$(x,\lambda)[(y,\mu)(z,\nu)] = (x,\lambda)(yz + \nu y + \mu z, \mu\nu)$$
$$= (x(yz + \nu y + \mu z) + \mu\nu x + \lambda(yz + \nu y + \mu z), \lambda\mu\nu)$$
$$= (x(yz) + \nu(xy) + \mu(xz) + \mu\nu x + \lambda(yz) + \lambda\nu y + \lambda\mu z, \lambda\mu\nu).$$

Using associativity in $A$, the two expressions are equal.

**Unity element:** $u = (0, 1)$ satisfies $(x,\lambda)(0,1) = (x + 0 + \lambda \cdot 0, \lambda \cdot 1) = (x, \lambda)$ and $(0,1)(x,\lambda) = (0 + \lambda \cdot 0 + 1 \cdot x, 1 \cdot \lambda) = (x, \lambda)$, so $u$ is a unity element for $A_1$.

**Embedding of $A$:** The mapping $x \mapsto (x, 0)$ is an algebra monomorphism $A \to A_1$; any element of $A_1$ is uniquely representable as $x + \lambda u$ with $x \in A$, $\lambda \in \mathbb{C}$.

**Ideal structure:** The mapping $x + \lambda u \mapsto \lambda$ is an algebra epimorphism $A_1 \to \mathbb{C}$ with kernel $A$, thus $A$ is an ideal of $A_1$ and $A_1/A \cong \mathbb{C}$. Since $\mathbb{C}$ is a field, $A$ is a maximal ideal of $A_1$. $\square$
