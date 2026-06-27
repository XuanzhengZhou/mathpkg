---
role: proof
locale: en
of_concept: partition-decomposition-unique
source_book: gtm013
source_chapter: "5"
source_section: "26"
---

This is an immediate consequence of Theorem (26.5) and Azumaya's Theorem (12.6).

By Theorem (26.5), the decomposition $M = \bigoplus_B N_\beta$ has the property that each $N_\beta$ is itself a direct sum of countably generated submodules that are direct summands of the $M_\alpha$. Since each $M_\alpha$ has a local endomorphism ring, by Azumaya's Theorem (12.6), decompositions of modules that complement direct summands have the property that each $N_\beta$ is isomorphic to a direct sum of some subset of the $M_\alpha$ indexed by a subset $A_\beta \subseteq A$.

Moreover, since $M = \bigoplus_B N_\beta = \bigoplus_B (\bigoplus_{A_\beta} M_\alpha) \cong \bigoplus_A M_\alpha$, the sets $A_\beta$ must form a partition of $A$. Thus there exists a partition $(A_\beta)_{\beta \in B}$ of $A$ with $N_\beta \cong \bigoplus_{A_\beta} M_\alpha$ for each $\beta \in B$.
