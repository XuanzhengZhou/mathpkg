---
role: proof
locale: en
of_concept: spanning-forest-equivalence
source_book: gtm054
source_chapter: "III"
source_section: "C"
---

Let $E_2 \subset E_1 \subseteq E$ and let $\Gamma_i = \Gamma_{(E+E_i)}$ ($i = 1, 2$). By C6 we have
$$\nu_{-1}(\Gamma_1) \geq \nu_{-1}(\Gamma); \quad \dim(\mathcal{Z}^\perp(\Gamma_1)) \leq \dim(\mathcal{Z}^\perp(\Gamma));$$
$$\dim(\mathcal{Z}(\Gamma_1)) \leq \dim(\mathcal{Z}(\Gamma));$$
and similarly for $\Gamma_2$. Equality must hold or fail simultaneously for the paired inequalities. Furthermore, equality cannot hold in both dimension inequalities for $\Gamma_2$. Finally, equality holds in both if and only if $\Gamma_1 = \Gamma$.

(a) $\Rightarrow$ (b). Let $\Gamma_1 = T$, and note that the second equality in (a) implies $\Gamma$ is a forest. By C9, the first equality in (a) implies $T$ is a spanning forest.

(b) $\Rightarrow$ (c). If $T$ is a spanning forest, then $F$ contains no nonempty cycle. If $T = \Gamma$, we are done. Otherwise, any edge added to $F$ would create a cycle, establishing minimality with respect to meeting every nonempty cocycle.

The remaining equivalences follow from duality and the Exchange Property.
