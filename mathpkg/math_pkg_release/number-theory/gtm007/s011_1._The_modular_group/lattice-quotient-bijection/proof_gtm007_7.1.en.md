---
role: proof
locale: en
of_concept: lattice-quotient-bijection
source_book: gtm007
source_chapter: "VII"
source_section: "1"
---

The quotient $M/\mathbf{C}^*$ is identified with $H$ via $(\omega_1, \omega_2) \mapsto z = \omega_1/\omega_2$. Under this identification, the action of $\mathbf{SL}_2(\mathbf{Z})$ on $M$ given by
$$\begin{pmatrix} a & b \\ c & d \end{pmatrix} (\omega_1, \omega_2) = (a\omega_1 + b\omega_2, c\omega_1 + d\omega_2)$$
transforms into the action of $G = \mathbf{SL}_2(\mathbf{Z})/\{\pm 1\}$ on $H$ via fractional linear transformations. Indeed,
$$\frac{a\omega_1 + b\omega_2}{c\omega_1 + d\omega_2} = \frac{a(\omega_1/\omega_2) + b}{c(\omega_1/\omega_2) + d}.$$

The map $M \to \mathcal{R}$ is surjective, and two pairs in $M$ give the same lattice exactly when they differ by the action of $\mathbf{SL}_2(\mathbf{Z})$ (a change of $\mathbf{Z}$-basis for the lattice). Passing to quotients by $\mathbf{C}^*$, we obtain the claimed bijection $\mathcal{R}/\mathbf{C}^* \cong H/G$.

For elliptic curves: two lattices $\Gamma, \Gamma'$ give isomorphic elliptic curves $\mathbf{C}/\Gamma \cong \mathbf{C}/\Gamma'$ if and only if $\Gamma' = \lambda \Gamma$ for some $\lambda \in \mathbf{C}^*$, i.e. they are homothetic.
