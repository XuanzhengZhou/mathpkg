---
locale: en
of_concept: the-only-spheres-with-an-h-space-structure-are-s1-s3-and-s7
role: proof
source_book: gtm020
source_chapter: 16. Vector Fields on the Sphere
source_section: '4'
---

An $H$-space structure $\phi: S^{n-1} \times S^{n-1} \rightarrow S^{n-1}$ is a map of bidegree $(1, 1)$, and the Hopf construction yields a map $S^{2n-1} \rightarrow S^n$ of the Hopf invariant 1 by Theorem (3.5). By (4

CHAPTER 16

Vector Fields on the Sphere

In Chap. 12, Theorem (8.2), we saw that $S^{n-1}$ has $\rho(n) - 1$ orthonormal tangent vector fields defined on it. The object of this chapter is to outline the steps required to prove that $S^{n-1}$ does not have $\rho(n)$ orthonormal tangent vector fields defined on it; in fact, $S^{n-1}$ does not have $\rho(n)$ linearly independent tangent vector fields; see also Adams [6].

To do this, we use several concepts: that of Thom space, $S$-duality, fibre homotopy equivalence, and the spectral sequence in $K$-theory. In this chapter we are able only to sketch the background material. Another way of stating the theorem on the nonexistence of vector fields is that there are no cross sections to the fibre map $V_{\rho(n)+1}(\mathbf{R}^n) \rightarrow V_1(\mathbf{R}^n) = S^{n-1}$, and Theorem 12(8.2) says that there is a cross section to $V_{\rho(n)}(\mathbf{R}^n) \rightarrow V_1(\mathbf{R}^n)$. An important reduction step in proving the nonexistence theorem is a statement that a cross section of $V_k(\mathbf{R}^n) \rightarrow V_1(\mathbf{R}^n)$ exists if and only if there is a map between shunted projective spaces with particular properties.

1. Thom Spaces of Vector Bundles

Let $\xi$ be a real vector bundle with base space $B(\xi)$, associated projective bundle $P(\xi)$, associated sphere bundle $S(\xi)$, and associated unit disk bundle $D(\xi)$ for some riemannian metric on $\xi$. If $\alpha$ is the associated principal $O(n)$-bundle to $\xi$, then $P(\xi)$ is the fibre bundle $\alpha[RP^{n-1}]$, $S(\xi)$ is $\alpha[S^{n-1}]$, and $D(\xi)$ is $\alpha[D^n]$. We consider the following diagram of cofibre maps $f_1, f_2$, and $f_3$,
