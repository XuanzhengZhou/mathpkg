---
role: proof
locale: en
of_concept: theorem-14-21-m-standard-transitive-model
source_book: gtm008
source_chapter: "14"
source_section: "14. Another Interpretation of V^{(B)}"
---

This follows from the combination of several results:

1. $M$ is transitive with Boolean value 1 (Theorem 14.10).
2. All ZF axioms relativized to $M$ hold with Boolean value 1 (the simplified verification in the previous theorem).
3. All ordinals belong to $M$: for any ordinal $\alpha$, $[M(\check{\alpha})] = 1$, since $\check{\alpha}$ is a canonical name for an ordinal.

The statement that $M$ is "standard" means it is a transitive $\in$-model, which follows from transitivity. "Containing all ordinals" follows from 3. Together with 2, this gives that $M$ is a standard transitive model of ZF containing all ordinals, with Boolean value 1.
