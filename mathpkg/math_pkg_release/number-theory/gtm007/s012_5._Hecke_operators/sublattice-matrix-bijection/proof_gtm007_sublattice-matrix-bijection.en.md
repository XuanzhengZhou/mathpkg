---
role: proof
locale: en
of_concept: sublattice-matrix-bijection
source_book: gtm007
source_chapter: "VII"
source_section: "5.2"
---
The fact that $\Gamma_\sigma$ belongs to $\Gamma(n)$ follows from $\det(\sigma) = ad = n$.

Conversely, let $\Gamma' \in \Gamma(n)$. Set
$$Y_1 = \Gamma / (\Gamma' + \mathbf{Z}\omega_2) \quad \text{and} \quad Y_2 = \mathbf{Z}\omega_2 / (\Gamma' \cap \mathbf{Z}\omega_2).$$
These are cyclic groups generated respectively by the images of $\omega_1$ and $\omega_2$. Let $a$ and $d$ be their orders. The exact sequence
$$0 \to Y_2 \to \Gamma/\Gamma' \to Y_1 \to 0$$
shows that $ad = n$. Put $\omega'_2 = d\omega_2$; then $\omega'_2 \in \Gamma'$. There exists $\omega'_1 \in \Gamma'$ such that $\omega'_1 \equiv a\omega_1 \pmod{\mathbf{Z}\omega_2}$. It is clear that $\omega'_1$ and $\omega'_2$ form a basis of $\Gamma'$. Write $\omega'_1 = a\omega_1 + b\omega_2$ with $b \in \mathbf{Z}$, uniquely determined modulo $d$. Imposing $0 \leq b < d$ fixes $b$ and thus $\omega'_1$. This associates to each $\Gamma'$ a matrix $\sigma(\Gamma') = \begin{pmatrix} a & b \\ 0 & d \end{pmatrix} \in S_n$, and the maps $\sigma \mapsto \Gamma_\sigma$ and $\Gamma' \mapsto \sigma(\Gamma')$ are inverse to each other.
