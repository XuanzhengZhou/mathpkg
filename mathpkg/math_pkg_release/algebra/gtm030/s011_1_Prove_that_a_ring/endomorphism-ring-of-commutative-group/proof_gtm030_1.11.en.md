---
role: proof
locale: en
of_concept: endomorphism-ring-of-commutative-group
source_book: gtm030
source_chapter: "1"
source_section: "1.11"
---
We verify the ring axioms.

**Additive group structure:** First, if $\eta, \rho \in \mathfrak{E}$, then $\eta + \rho$ (defined pointwise) is an endomorphism because
$$(a+b)(\eta+\rho) = (a+b)\eta + (a+b)\rho = a\eta + b\eta + a\rho + b\rho = a\eta + a\rho + b\eta + b\rho = a(\eta+\rho) + b(\eta+\rho).$$

Associativity of addition: $a(\eta + (\rho + \lambda)) = a\eta + a(\rho+\lambda) = a\eta + a\rho + a\lambda$ and $a((\eta+\rho)+\lambda) = a(\eta+\rho) + a\lambda = a\eta + a\rho + a\lambda$, so $\eta + (\rho+\lambda) = (\eta+\rho)+\lambda$.

Commutativity: $a(\eta+\rho) = a\eta + a\rho = a\rho + a\eta = a(\rho+\eta)$, so $\eta+\rho = \rho+\eta$.

The zero endomorphism $0$ maps every $a$ to $0$. Clearly $0 \in \mathfrak{E}$ and $\eta + 0 = \eta$ for all $\eta$.

The negative $-\eta$ sends $a \mapsto -(a\eta)$. Since $-\eta$ is the resultant of $\eta$ followed by the automorphism $a \mapsto -a$, it is an endomorphism. And $\eta + (-\eta) = 0$.

Thus $\mathfrak{E}, +$ is a commutative group.

**Multiplication (composition):** Composition of mappings is associative, so $\cdot$ is associative. Composition of two endomorphisms is an endomorphism, so $\mathfrak{E}$ is closed under $\cdot$.

**Distributive laws:** For the right distributive law,
$$a(\eta(\rho+\lambda)) = (a\eta)(\rho+\lambda) = (a\eta)\rho + (a\eta)\lambda = a(\eta\rho) + a(\eta\lambda) = a(\eta\rho + \eta\lambda).$$
Hence $\eta(\rho+\lambda) = \eta\rho + \eta\lambda$.

For the left distributive law,
$$a((\eta+\rho)\lambda) = (a(\eta+\rho))\lambda = (a\eta + a\rho)\lambda = (a\eta)\lambda + (a\rho)\lambda = a(\eta\lambda) + a(\rho\lambda) = a(\eta\lambda + \rho\lambda).$$
Hence $(\eta+\rho)\lambda = \eta\lambda + \rho\lambda$.

Therefore $\mathfrak{E}, +, \cdot$ is a ring.
