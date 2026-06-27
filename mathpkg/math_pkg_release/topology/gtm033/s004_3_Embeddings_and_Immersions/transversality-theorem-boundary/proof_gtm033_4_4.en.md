---
role: proof
locale: en
of_concept: transversality-theorem-boundary
source_book: gtm033
source_chapter: "4. Manifolds with Boundary"
source_section: "4"
---

# Proof of Transversality Theorem for Manifolds with Boundary (Theorem 4.2)

**Theorem 4.2.** Let $A \subset N$ be a $C^r$ submanifold. Suppose that either $A$ is neat, or $A \subset N - \partial N$, or $A \subset \partial N$. If $f: M \to N$ is a $C^r$ map with both $f$ and $f|\partial M$ transverse to $A$, then $f^{-1}(A)$ is a $C^r$ submanifold and $\partial f^{-1}(A) = f^{-1}(\partial A)$.

*Proof.* The source text states: "The proofs of Theorems 4.1 and 4.2 are left to the reader."

We sketch the proof, which generalizes the transversality theorem (Theorem 3.3) for manifolds without boundary.

**Outline of the proof:**

The proof follows the same local argument as Theorem 3.3, modified to account for the boundary.

**Step 1: Reduction to a local model.** By taking appropriate charts, we may assume $M = \mathbb{H}^m$ (the half-space $\mathbb{R}^{m-1} \times [0,\infty)$), $N = \mathbb{R}^n$, and $A = \mathbb{R}^k \times \{0\} \subset \mathbb{R}^n$ (where $k = \dim N - \dim A$). The transversality condition means that the composition

$$T_x M \xrightarrow{T_x f} T_{f(x)} N \to T_{f(x)} N / T_{f(x)} A$$

is surjective for all $x \in f^{-1}(A)$ (and similarly for $x \in \partial M \cap f^{-1}(A)$ using $T_x(\partial M)$).

**Step 2: The boundaryless case.** For interior points $x \in f^{-1}(A) \cap \operatorname{Int} M$, the standard transversality theorem (Theorem 3.3) applies directly: $f^{-1}(A)$ is a submanifold near $x$ of codimension equal to $\operatorname{codim} A$.

**Step 3: Boundary points.** For $x \in f^{-1}(A) \cap \partial M$, we use the additional hypothesis that $f|\partial M$ is transverse to $A$. In the local model, this means that the restriction of $T_x f$ to $T_x(\partial M) = \mathbb{R}^{m-1} \times \{0\}$ is also surjective onto the normal space. This ensures that near $x$, the preimage $f^{-1}(A)$ meets $\partial M$ transversely, which is exactly the condition for $f^{-1}(A)$ to be a neat submanifold.

**Step 4: The boundary of the preimage.** The equality $\partial f^{-1}(A) = f^{-1}(\partial A)$ follows from the transversality condition at the boundary. For a point $x \in f^{-1}(\partial A)$, the transversality of $f$ to $A$ forces $x \in \partial f^{-1}(A)$. Conversely, the three cases for $A$ (neat, contained in interior, or contained in boundary) ensure that the boundary of $f^{-1}(A)$ behaves as stated.

The three cases for $A$ are:
- If $A$ is neat, then $\partial A = A \cap \partial N$, and transversality ensures $\partial f^{-1}(A) = f^{-1}(\partial A)$.
- If $A \subset N - \partial N$, then $\partial A = \varnothing$, so $f^{-1}(A)$ is a manifold without boundary (in the sense that its boundary is empty).
- If $A \subset \partial N$, then $A = \partial A$, and the result follows similarly.

$\square$

**Note.** The source text explicitly leaves the proofs of Theorems 4.1 and 4.2 as exercises for the reader. The above proof sketch is reconstructed from the general theory of transversality as developed in Chapter 3 of the book, adapted to the boundary setting.
