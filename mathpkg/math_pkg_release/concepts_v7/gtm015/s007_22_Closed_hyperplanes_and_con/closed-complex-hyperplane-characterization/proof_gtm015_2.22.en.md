---
role: proof
locale: en
of_concept: closed-complex-hyperplane-characterization
source_book: gtm015
source_chapter: "2"
source_section: "22"
---

# Proof of Characterization of closed complex hyperplanes

This follows from the lemma (22.7) in the same way that (21.15) follows from (21.14), on noting that translations are homeomorphisms.

Specifically, let $H \subset E$ be a closed $\mathbb{C}$-hyperplane. By (21.15), $H = z_0 + M$ where $M$ is a maximal $\mathbb{C}$-linear subspace. Since $H$ is closed, $M = H - z_0$ is also closed. By (22.7), $M = M_0 \cap (iM_0)$ with $M_0$ a closed, maximal $\mathbb{R}$-linear subspace. Thus $H = z_0 + M_0 \cap (iM_0)$.

Conversely, if $H = z_0 + M_0 \cap (iM_0)$ with $M_0$ closed, maximal $\mathbb{R}$-linear, then $M = M_0 \cap (iM_0)$ is closed and maximal $\mathbb{C}$-linear by (22.7), hence $H = z_0 + M$ is a closed $\mathbb{C}$-hyperplane.
