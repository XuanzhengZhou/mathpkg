---
role: proof
locale: en
of_concept: cw-complex-restriction-criterion
source_book: gtm020
source_chapter: "6"
source_section: "2"
---

The corollary follows from Theorem 2.3 (the cross-section criterion for restriction) together with obstruction theory. By Theorem 2.3, a principal $G$-bundle $\xi$ over $B$ has a restriction to a principal $H$-bundle if and only if the associated bundle $\xi[G \bmod H]$ admits a cross section.

The obstructions to constructing a cross section of $\xi[G \bmod H]$ over a CW-complex $B$ lie in the cohomology groups
$$
H^{i+1}(B; \pi_i(G \bmod H))
$$
for $i \geq 0$. Since by hypothesis $\pi_i(G \bmod H) = 0$ for all $i < \dim B$, all obstruction groups $H^{i+1}(B; \pi_i(G \bmod H))$ vanish for $i+1 \leq \dim B$. Hence all obstructions vanish, and a cross section exists.

By the correspondence established in Theorem 2.3, this cross section determines a restriction of $\xi$ to a principal $H$-bundle.
