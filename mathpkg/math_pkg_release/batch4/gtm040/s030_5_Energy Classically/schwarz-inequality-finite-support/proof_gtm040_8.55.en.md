---
role: proof
locale: en
of_concept: schwarz-inequality-finite-support
source_book: gtm040
source_chapter: "8"
source_section: "5"
---

From properties (1), (2), and (3), we can prove that Schwarz's inequality holds for $g$ and $\bar{g}$ whenever they have finite support. By Lemma [properties of the bilinear form], the bilinear form satisfies symmetry $(\bar{g}, g) = (g, \bar{g})$, homogeneity $(cg, \bar{g}) = c(g, \bar{g})$, and additivity $(g + g', \bar{g}) = (g, \bar{g}) + (g', \bar{g})$ when the potentials have finite support. Together with the non-negativity of $\mathbf{I}(g) = (g, g)$, the standard proof of Schwarz's inequality applies: for any real $\lambda$, the quadratic form $(g + \lambda\bar{g}, g + \lambda\bar{g}) \geq 0$ implies the discriminant must be non-positive, yielding $(g, \bar{g})^2 \leq (g, g)(\bar{g}, \bar{g}) = \mathbf{I}(g)\mathbf{I}(\bar{g})$.
