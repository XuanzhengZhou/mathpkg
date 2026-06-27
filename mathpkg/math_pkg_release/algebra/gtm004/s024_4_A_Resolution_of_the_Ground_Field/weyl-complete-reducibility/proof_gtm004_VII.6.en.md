---
role: proof
locale: en
of_concept: weyl-complete-reducibility
source_book: gtm004
source_chapter: "VII"
source_section: "6"
---

# Proof of Weyl's Complete Reducibility Theorem

**Theorem 6.2 (Weyl).** Every finite-dimensional module $A$ over a semi-simple Lie algebra $\mathfrak{g}$ (over a field of characteristic 0) is a direct sum of simple $\mathfrak{g}$-modules. In other words, every finite-dimensional representation of a semi-simple Lie algebra is completely reducible.

**Proof.** The proof uses the First Whitehead Lemma in a way analogous to the cohomological proof of Maschke's Theorem (Theorem VI.16.6).

Let $A$ be a finite-dimensional $\mathfrak{g}$-module and let $B \subset A$ be a submodule. It suffices to show that $B$ admits a $\mathfrak{g}$-module complement in $A$.

Consider the $\mathfrak{g}$-module $\operatorname{Hom}_K(A, B)$ with the $\mathfrak{g}$-action given by

$$(x \cdot f)(a) = x \cdot f(a) - f(x \cdot a), \quad x \in \mathfrak{g}, \; f \in \operatorname{Hom}_K(A, B), \; a \in A.$$

The subspace $\operatorname{Hom}_{\mathfrak{g}}(A, B)$ of $\mathfrak{g}$-module homomorphisms consists precisely of those $f$ with $x \cdot f = 0$ for all $x \in \mathfrak{g}$; that is, $\operatorname{Hom}_{\mathfrak{g}}(A, B) = H^0(\mathfrak{g}, \operatorname{Hom}_K(A, B))$.

Let $\pi : A \to B$ be any $K$-linear projection onto $B$ (i.e., $\pi|_B = 1_B$). Consider the $\mathfrak{g}$-module map

$$\varphi : \mathfrak{g} \to \operatorname{Hom}_K(A, B), \quad \varphi(x) = x \cdot \pi.$$

If $\varphi = 0$, then $\pi$ is already a $\mathfrak{g}$-module homomorphism and $\ker \pi$ is the desired complement.

In general, $\varphi$ is a 1-cocycle (this follows from the Jacobi identity). By the First Whitehead Lemma, $H^1(\mathfrak{g}, \operatorname{Hom}_K(A, B)) = 0$, so $\varphi$ is a coboundary: there exists $\psi \in \operatorname{Hom}_K(A, B)$ such that

$$\varphi(x) = x \cdot \psi \quad \text{for all } x \in \mathfrak{g}.$$

Then $\pi' = \pi - \psi$ satisfies $x \cdot \pi' = 0$ for all $x \in \mathfrak{g}$, so $\pi'$ is a $\mathfrak{g}$-module projection onto $B$. Its kernel $\ker \pi'$ is a $\mathfrak{g}$-submodule complement to $B$ in $A$.

By induction on the length of $A$, we conclude that $A$ decomposes as a direct sum of simple $\mathfrak{g}$-modules. $\square$

The reader should compare this argument with the proof of Maschke's Theorem (Theorem VI.16.6), which uses an averaging argument over a finite group instead of the vanishing of $H^1$.
