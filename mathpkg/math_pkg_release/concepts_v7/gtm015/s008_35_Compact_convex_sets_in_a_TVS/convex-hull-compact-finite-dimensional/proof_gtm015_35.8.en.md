---
role: proof
locale: en
of_concept: convex-hull-compact-finite-dimensional
source_book: gtm015
source_chapter: "35"
source_section: "Compact convex sets in a TVS"
---

# Proof of Convex hull of a compact set in a finite-dimensional TVS is compact

Let $E$ be a finite-dimensional, separated topological vector space over $\mathbb{K}$, and let $S \subset E$ be a compact subset.

**Step 1.** A finite-dimensional separated TVS over $\mathbb{K}$ is isomorphic (as a TVS) to $\mathbb{K}^n$ with its standard topology. Indeed, any linear isomorphism $\varphi : E \to \mathbb{K}^n$ is a homeomorphism (this follows from the fact that on a finite-dimensional vector space, all Hausdorff TVS topologies coincide).

**Step 2.** Let $n = \dim E$. Under the identification $E \cong \mathbb{K}^n$, the set $S$ is a compact subset of $\mathbb{K}^n$. By Carathéodory's theorem (or the standard simplicial representation theorem), every point of $\operatorname{conv} S$ can be written as a convex combination of at most $n+1$ points of $S$.

**Step 3.** Define the continuous map

$$\Phi : S^{n+1} \times \Delta_n \to E$$

by

$$\Phi(s_0, \ldots, s_n, \lambda_0, \ldots, \lambda_n) = \sum_{i=0}^n \lambda_i s_i,$$

where $\Delta_n = \{ (\lambda_0, \ldots, \lambda_n) \in \mathbb{R}^{n+1} : \lambda_i \geq 0,\; \sum \lambda_i = 1 \}$ is the standard $n$-simplex. The domain $S^{n+1} \times \Delta_n$ is compact (product of compact sets), and $\Phi$ is continuous.

**Step 4.** By Carathéodory's theorem, $\operatorname{conv} S$ is precisely the image of $\Phi$. The continuous image of a compact set is compact, so $\operatorname{conv} S$ is compact.

Note: This result contrasts sharply with the infinite-dimensional case, where the convex hull of a compact set need not be compact (or even closed). The finite-dimensional hypothesis is essential.
