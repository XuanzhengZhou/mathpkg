---
role: proof
locale: en
of_concept: associativity-of-andre-quasifields
source_book: gtm006
source_chapter: "IX"
source_section: "3"
---

For $x, y, z \in F^*$, compute the two ways of associating the product $x \odot y \odot z$:
\[
(x \odot y) \odot z = (x y^{\alpha_x}) \odot z = (x y^{\alpha_x}) z^{\alpha_{xy}} = x y^{\alpha_x} z^{\alpha_{xy}},
\]
\[
x \odot (y \odot z) = x \odot (y z^{\alpha_y}) = x (y z^{\alpha_y})^{\alpha_x} = x y^{\alpha_x} z^{\alpha_y \alpha_x}.
\]

Associativity requires these to be equal for all $x, y, z$, which gives:
\[
z^{\alpha_{xy}} = z^{\alpha_y \alpha_x} \quad \text{for all } x, y, z \in F^*.
\]

Since the action of $\Gamma$ on $F$ is faithful, this implies $\alpha_{xy} = \alpha_y \alpha_x$ for all $x, y \in F^*$. Thus $\alpha$ must be an anti-homomorphism.

Conversely, if $\alpha$ is an anti-homomorphism, the two expressions coincide and $F_\phi$ is associative. $\square$
