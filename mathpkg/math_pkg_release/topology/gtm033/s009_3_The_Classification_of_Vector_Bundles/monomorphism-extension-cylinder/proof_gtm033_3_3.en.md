---
role: proof
locale: en
of_concept: monomorphism-extension-cylinder
source_book: gtm033
source_chapter: "3"
source_section: "3. The Classification of Vector Bundles"
---

# Proof of Monomorphism Extension on Cylinder (Corollary 3.2)

By the covering homotopy theorem for vector bundles, the two monomorphisms

$$F_0: \eta|_{V \times \{0\}} \to \mathbb{R}^s, \qquad F_1: \eta|_{V \times \{1\}} \to \mathbb{R}^s$$

extend to a $C^r$ monomorphism

$$F': \eta|_U \to U \times \mathbb{R}^s$$

where $U \subset V \times I$ is a neighborhood of $V \times \{0, 1\}$ in $V \times I$. (The covering homotopy theorem guarantees that any bundle map defined on a closed subset can be extended to a neighborhood when the bundle is suitably trivialized; here the two maps at the ends of the cylinder constitute a map defined on the closed set $V \times \{0, 1\}$.)

Now apply Theorem 3.1 with:
- $M = V \times I$ (an $(n+1)$-manifold),
- $A = V \times \{0, 1\}$ (a closed subset of $M$),
- the neighborhood $U$ of $A$ as above,
- the monomorphism $F'$ defined on $\eta|_U$.

The dimension condition is satisfied because $s > k + n$ implies $s \geqslant k + \dim(V \times I) = k + n + 1$? Wait—note that Theorem 3.1 requires $s \geqslant k + \dim M$, and here $\dim M = \dim(V \times I) = n + 1$. The hypothesis of Corollary 3.2 is $s > k + n$, i.e., $s \geqslant k + n + 1 = k + \dim M$. Thus the dimension inequality of Theorem 3.1 holds, and the theorem produces a $C^r$ monomorphism

$$F: \eta \to (V \times I) \times \mathbb{R}^s = \mathbb{R}^s$$

(identifying the trivial bundle $(V \times I) \times \mathbb{R}^s$ with $\mathbb{R}^s$ by projecting away the base) that extends $F'$, and hence extends $F_0$ and $F_1$ as required. $\square$
