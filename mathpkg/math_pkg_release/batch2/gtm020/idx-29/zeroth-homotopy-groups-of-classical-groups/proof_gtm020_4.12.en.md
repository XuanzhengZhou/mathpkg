---
role: proof
locale: en
of_concept: zeroth-homotopy-groups-of-classical-groups
source_book: gtm020
source_chapter: "4"
source_section: "12"
---

The inequality $0 \leq c(n+1)-3$ holds for all $n \geq 1$ if $c = 2, 4$, and for $n \geq 2$ if $c = 1$.
This means that for the relevant values of $c$ and $n$, Proposition 11.1 gives isomorphisms in low
homotopy degrees, reducing the computation to the low-rank cases.

For the elementary calculations:
- $U(1) \cong S^1$ is connected, so $\pi_0(U(1)) = 0$.
- $SU(1) = \{1\}$ is connected.
- $SO(2) \cong S^1$ is connected, so $\pi_0(SO(2)) = 0$.
- $O(2)$ has two components: $SO(2)$ (the rotations) and matrices of determinant $-1$ (reflections), so $\pi_0(O(2)) = \mathbf{Z}_2$.

Using the stability isomorphisms from the fibration $SO(n) \to SO(n+1) \to S^n$ and the analogous
fibrations for the other classical groups (all obtained as Stiefel manifold fibrations with $k=1$),
the $\pi_0$ result extends from the low-rank cases to all $n \geq 1$:
- $\pi_0(O(n)) = \mathbf{Z}_2$ for all $n \geq 1$ (the determinant distinguishes the two components).
- $\pi_0(SO(n)) = \pi_0(U(n)) = \pi_0(SU(n)) = \pi_0(Sp(n)) = 0$ for all $n \geq 1$.
