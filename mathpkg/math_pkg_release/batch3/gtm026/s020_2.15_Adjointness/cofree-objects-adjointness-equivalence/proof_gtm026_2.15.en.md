---
role: proof
locale: en
of_concept: cofree-objects-adjointness-equivalence
source_book: gtm026
source_chapter: "2"
source_section: "2.15"
---

This theorem follows immediately from the duality principle for adjointness (2.17) applied to Theorem 2.18. Given $F: \mathcal{K} \longrightarrow \mathcal{A}$, consider the opposite functor $F^{\text{op}}: \mathcal{K}^{\text{op}} \longrightarrow \mathcal{A}^{\text{op}}$. By Theorem 2.18, there exists an adjointness of form $(\mathcal{A}^{\text{op}}, \mathcal{K}^{\text{op}}, F^{\text{op}}, U^{\text{op}}, \varepsilon, \eta)$ if and only if for every object $A$ in $\mathcal{A}^{\text{op}}$ there exists a free object over $A$ with respect to $F^{\text{op}}$. By the duality principle (2.17), an adjointness of this form exists if and only if $(\mathcal{A}, \mathcal{K}, U, F, \eta, \varepsilon)$ is an adjointness. Moreover, a free object over $A$ with respect to $F^{\text{op}}$ in $\mathcal{A}^{\text{op}}$ corresponds precisely to a cofree $\mathcal{K}$-object over $A$ with respect to $F$ in the original categories. The result follows. $\square$
