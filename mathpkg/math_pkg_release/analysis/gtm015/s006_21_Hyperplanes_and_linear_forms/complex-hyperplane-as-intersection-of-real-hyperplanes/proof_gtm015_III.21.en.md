---
role: proof
locale: en
of_concept: complex-hyperplane-as-intersection-of-real-hyperplanes
source_book: gtm015
source_chapter: "III. Topological Vector Spaces"
source_section: "21. Hyperplanes and linear forms"
---

# Proof of Complex Hyperplanes as Intersections of Real Hyperplanes

Let $E$ be a vector space over $\mathbb{C}$. By restricting scalar multiplication, $E$ is also regarded as a vector space over $\mathbb{R}$.

**Corollary 21.16.** Every $\mathbb{C}$-hyperplane in $E$ is the intersection of two $\mathbb{R}$-hyperplanes in $E$.

*Proof.*

Let $H$ be a $\mathbb{C}$-hyperplane in $E$. By Theorem 21.15(c), there exist a maximal $\mathbb{R}$-linear subspace $M_0$ of $E$ and a vector $z_0 \in E$ such that

$$H = z_0 + (M_0 \cap iM_0).$$

Since translation by $z_0$ distributes over intersection,

$$H = z_0 + (M_0 \cap iM_0) = (z_0 + M_0) \cap (z_0 + iM_0).$$

Now, $M_0$ is a maximal $\mathbb{R}$-linear subspace, so $z_0 + M_0$ is an $\mathbb{R}$-hyperplane by Theorem 21.7. Similarly, $iM_0$ is also a maximal $\mathbb{R}$-linear subspace (multiplication by $i$ is an $\mathbb{R}$-linear automorphism of $E$ that preserves the lattice of subspaces, hence preserves maximality), and therefore $z_0 + iM_0$ is an $\mathbb{R}$-hyperplane.

Thus $H = (z_0 + M_0) \cap (z_0 + iM_0)$ is the intersection of two $\mathbb{R}$-hyperplanes.

**Remarks.**
1. The two $\mathbb{R}$-hyperplanes are related: if the first is determined by the $\mathbb{R}$-linear form $g$ (i.e., $z_0 + M_0 = \{x : g(x) = g(z_0)\}$), then the second is determined by the $\mathbb{R}$-linear form $x \mapsto g(-ix) = -g(ix)$ (i.e., $z_0 + iM_0 = \{x : g(ix) = g(iz_0)\}$).
2. Conversely, an intersection of two $\mathbb{R}$-hyperplanes need not be a $\mathbb{C}$-hyperplane; the condition in Theorem 21.15(b) requires that they come from the *same* maximal $\mathbb{R}$-linear subspace $M_0$.
3. This result is fundamental for the complex Hahn-Banach theorem: to extend a $\mathbb{C}$-linear form controlled by a seminorm, one extends its real part as an $\mathbb{R}$-linear form via the real Hahn-Banach theorem, then reconstructs the $\mathbb{C}$-linear form using Theorem 21.13.
