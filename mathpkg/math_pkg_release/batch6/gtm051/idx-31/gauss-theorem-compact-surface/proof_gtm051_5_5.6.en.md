---
role: proof
locale: en
of_concept: gauss-theorem-compact-surface
source_book: gtm051
source_chapter: "5"
source_section: "5.6"
---

**Proof.** Write the integral over $M$ in terms of some polygonal decomposition $\Pi$ of $M$:
$$\iint_M (\operatorname{div} X) dM = \sum_\rho \iint_{P_\rho} (\operatorname{div} X) dM.$$

Apply Gauss's theorem (5.6.9) to each polygon $P_\rho$:
$$\sum_\rho \iint_{P_\rho} (\operatorname{div} X) dM = \sum_\rho \int_{\partial P_\rho} i_X dM.$$

In the sum over all polygons, each interior edge appears as a boundary curve on exactly two adjacent polygons, but with opposite orientations. Therefore the corresponding line integrals cancel pairwise. The only remaining terms come from boundary edges, but since $M$ is a compact surface without boundary (in the manifold sense), there are no such edges. Hence the total sum is zero. $\square$
