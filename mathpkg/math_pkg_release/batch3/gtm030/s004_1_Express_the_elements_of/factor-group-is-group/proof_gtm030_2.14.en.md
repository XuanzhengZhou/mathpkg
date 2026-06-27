---
role: proof
locale: en
of_concept: factor-group-is-group
source_book: gtm030
source_chapter: "2"
source_section: "14"
---

Since $\mathfrak{H}$ is invariant, $\mathfrak{H}y = y\mathfrak{H}$ for all $y$. Then
\[
(x\mathfrak{H})(y\mathfrak{H}) = x(\mathfrak{H}y)\mathfrak{H} = x(y\mathfrak{H})\mathfrak{H} = xy\mathfrak{H}\mathfrak{H} = xy\mathfrak{H},
\]
so the product of two cosets is again a coset. Associativity follows from associativity of subset multiplication: $((x\mathfrak{H})(y\mathfrak{H}))(z\mathfrak{H}) = (xy\mathfrak{H})(z\mathfrak{H}) = (xy)z\mathfrak{H} = x(yz)\mathfrak{H} = (x\mathfrak{H})(yz\mathfrak{H}) = (x\mathfrak{H})((y\mathfrak{H})(z\mathfrak{H}))$. The coset $\mathfrak{H} = 1\mathfrak{H}$ is the identity: $\mathfrak{H}(x\mathfrak{H}) = 1\mathfrak{H} \cdot x\mathfrak{H} = x\mathfrak{H}$ and $(x\mathfrak{H})\mathfrak{H} = x\mathfrak{H}$. The inverse of $x\mathfrak{H}$ is $x^{-1}\mathfrak{H}$ since $(x\mathfrak{H})(x^{-1}\mathfrak{H}) = xx^{-1}\mathfrak{H} = \mathfrak{H}$ and $(x^{-1}\mathfrak{H})(x\mathfrak{H}) = x^{-1}x\mathfrak{H} = \mathfrak{H}$. Thus $\mathfrak{G}/\mathfrak{H}$ is a group.
