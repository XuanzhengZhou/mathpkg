---
role: proof
locale: en
of_concept: bounded-pseudo-metric
source_book: gtm027
source_chapter: "4"
source_section: "Existence of Continuous Functions"
---

# Proof of Bounded Pseudo-Metric Construction

**Theorem 13.** Let $(X,d)$ be a pseudo-metric space, and let $e(x,y) = \min[1, d(x,y)]$. Then $(X,e)$ is a pseudo-metric space whose topology is identical with that of $(X,d)$. Consequently each pseudo-metric space is homeomorphic to a pseudo-metric space of diameter at most one.

*Proof.* It is straightforward to verify that $e$ satisfies the axioms of a pseudo-metric: $e(x,x) = \min[1,0] = 0$, $e(x,y) = e(y,x)$ by symmetry of $d$, and the triangle inequality $e(x,z) \leq e(x,y) + e(y,z)$ follows from the triangle inequality for $d$ together with the fact that $\min[1, a+b] \leq \min[1,a] + \min[1,b]$ for nonnegative $a,b$.

The family of all open $r$-spheres for $r < 1$ is a base for the pseudo-metric topology. Since this family is the same whether $d$ or $e$ is used as pseudo-metric (because for $r < 1$, $d(x,y) < r$ iff $e(x,y) < r$), the two pseudo-metric topologies are identical. Clearly the $e$-diameter of $X$ is at most one.

