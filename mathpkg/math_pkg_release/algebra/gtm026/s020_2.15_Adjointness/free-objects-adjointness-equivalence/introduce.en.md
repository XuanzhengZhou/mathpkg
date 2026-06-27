---
role: introduce
locale: en
content_hash: ""
written_against: ""
---

Theorem 2.18 establishes the fundamental equivalence between the existence of free objects and the existence of an adjointness. Given a functor $U: \mathcal{A} \to \mathcal{K}$, the theorem states that $U$ admits a free object over every object $K$ in $\mathcal{K}$ (in the sense of a universal arrow $K\eta: K \to KFU$) if and only if there exists a functor $F: \mathcal{K} \to \mathcal{A}$ and natural transformations $\eta: \text{id}_{\mathcal{K}} \to FU$, $\varepsilon: UF \to \text{id}_{\mathcal{A}}$ forming an adjointness $(\mathcal{A}, \mathcal{K}, U, F, \eta, \varepsilon)$. The proof constructs $F$ on morphisms using the universal property and defines $\varepsilon$ via the formula $A\varepsilon = (\text{id}_{AU})^{\#}$, while the converse direction uses formula (2.19): $f^{\#} = fF \circ A\varepsilon$ as the definition of the universal arrow.
