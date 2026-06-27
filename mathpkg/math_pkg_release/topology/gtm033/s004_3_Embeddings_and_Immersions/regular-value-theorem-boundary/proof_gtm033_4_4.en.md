---
role: proof
locale: en
of_concept: regular-value-theorem-boundary
source_book: gtm033
source_chapter: "4. Manifolds with Boundary"
source_section: "4"
---

# Proof of Regular Value Theorem for Manifolds with Boundary (Theorem 4.1)

**Theorem 4.1.** Let $M$ be a $C^r$ $\partial$-manifold and $N$ a $C^r$ manifold, $r \geqslant 1$. Let $f: M \to N$ be a $C^r$ map. If $y \in N - \partial N$ is a regular value for both $f$ and $f|\partial M$, then $f^{-1}(y)$ is a neat $C^r$ submanifold of $M$.

*Proof.* The source text states: "The proofs of Theorems 4.1 and 4.2 are left to the reader."

We present the proof, which generalizes the regular value theorem (Theorem 1.3.2) for manifolds without boundary.

**Outline of the proof:**

**Step 1: Interior points.** Let $x \in f^{-1}(y) \cap \operatorname{Int} M$. Since $y$ is a regular value of $f$, the derivative $T_x f: T_x M \to T_y N$ is surjective. By the inverse function theorem (or the regular value theorem for manifolds without boundary, Theorem 1.3.2), there is a neighborhood $U$ of $x$ in $\operatorname{Int} M$ such that $f^{-1}(y) \cap U$ is a $C^r$ submanifold of $M$ of dimension $\dim M - \dim N$.

**Step 2: Boundary points.** Let $x \in f^{-1}(y) \cap \partial M$. Take a boundary chart $(\varphi, U)$ with $\varphi(x) = 0$ and $\varphi(U) \subset \mathbb{H}^m = \{(x^1,\ldots,x^m) \in \mathbb{R}^m : x^m \geqslant 0\}$. Let $\psi$ be a chart for $N$ around $y$ with $\psi(y) = 0$. Consider the local representation

$$\tilde{f} = \psi \circ f \circ \varphi^{-1}: \mathbb{H}^m \to \mathbb{R}^n.$$

Choose an extension $\hat{f}: \mathbb{R}^m \to \mathbb{R}^n$ of $\tilde{f}$ to an open neighborhood of $0$ in $\mathbb{R}^m$. (This is possible since $M$ is a $C^r$ manifold with boundary: the definition of $C^r$ map on a half-space includes extendability.)

**Step 3: Using the boundary hypothesis.** The hypothesis that $y$ is a regular value for $f|\partial M$ means that the restriction

$$T_x(f|\partial M): T_x(\partial M) \to T_y N$$

is surjective. In local coordinates, this means that the derivative of $\tilde{f}$ restricted to the hyperplane $\{x^m = 0\}$ is surjective. Consequently, $D\tilde{f}(0)$ is surjective as a map $\mathbb{R}^m \to \mathbb{R}^n$, and its restriction to $\mathbb{R}^{m-1} \times \{0\}$ is also surjective.

**Step 4: The preimage near the boundary.** By the implicit function theorem, $f^{-1}(y)$ is locally diffeomorphic to $\mathbb{R}^{\dim M - \dim N}$ near interior points. Near a boundary point $x \in \partial M \cap f^{-1}(y)$, the extra condition that $y$ is a regular value for $f|\partial M$ implies that $f^{-1}(y)$ meets $\partial M$ transversely at $x$. In local coordinates, after a linear change, we can write

$$\tilde{f}(x^1,\ldots,x^m) = (x^1,\ldots,x^n)$$

with $f^{-1}(y) = \{x^1 = \cdots = x^n = 0\}$ and $\partial M = \{x^m = 0\}$. The transversality condition at the boundary ensures that the subspace $\{x^1 = \cdots = x^n = 0\}$ is not contained in $\{x^m = 0\}$ except along their intersection, which has dimension $m - n - 1$.

**Step 5: Neatness.** The neatness condition follows because $\partial(f^{-1}(y)) = f^{-1}(y) \cap \partial M$, and the intersection is transverse. Thus $f^{-1}(y)$ is a neat $C^r$ submanifold.

$\square$

**Note.** The source text explicitly states that "The proofs of Theorems 4.1 and 4.2 are left to the reader." The above proof is a standard argument generalizing the regular value theorem (Chapter 1, Theorem 3.2) to manifolds with boundary, using the additional hypothesis on $f|\partial M$ to control the behavior at the boundary.
