---
role: proof
locale: en
of_concept: gch-saturated-models-regular-cardinality
source_book: gtm037
source_chapter: "28"
source_section: "4. Model Theory"
---

Using GCH, the proof follows from Theorem 28.13. Under GCH, for any regular cardinal $\kappa = |\mathrm{Fmla}_{\mathcal{L}}|$, the cardinal arithmetic conditions required by Theorem 28.13 are automatically satisfied. Specifically, GCH implies that for regular $\kappa$, we have $\kappa^{<\kappa} = \kappa$, which is precisely the condition needed to construct a saturated model of size $\kappa$ via an elementary chain of length $\kappa^+$. At each successor step, all types over subsets of size $<\kappa$ from the previous model are realized, and at limit steps the union is taken. The resulting model of size $\kappa$ is $\kappa$-saturated, hence saturated.

Alternative proofs can be given via Lemma (*) and the notions of universal and homogeneous structures (Definition 28.15), which are perhaps more natural and do not require the full machinery of Theorem 28.13.
