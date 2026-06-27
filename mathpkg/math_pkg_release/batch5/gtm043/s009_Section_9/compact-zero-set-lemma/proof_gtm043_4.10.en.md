---
role: proof
locale: en
of_concept: compact-zero-set-lemma
source_book: gtm043
source_chapter: "4"
source_section: "4.10"
---

Necessity is clear: if \(Z\) is compact and belongs to a \(z\)-filter \(\mathcal{F}\), then \(\bigcap \mathcal{F}\) is an intersection of closed subsets of the compact set \(Z\) with the finite intersection property, hence is nonempty; thus \(\mathcal{F}\) cannot be free.

Conversely, let \(\mathcal{B}\) be any family of closed subsets of \(Z\) with the finite intersection property. Extend \(\mathcal{B}\) to a \(z\)-filter \(\mathcal{F}\) (for instance, by taking all zero-sets containing finite intersections of members of \(\mathcal{B}\)). By hypothesis, \(Z\) belongs to no free \(z\)-filter, so \(\mathcal{F}\) must be fixed, i.e., \(\bigcap \mathcal{F} \neq \varnothing\). A fortiori, \(\bigcap \mathcal{B} \neq \varnothing\). Thus every family of closed subsets of \(Z\) with the finite intersection property has nonempty intersection, which is equivalent to \(Z\) being compact.
