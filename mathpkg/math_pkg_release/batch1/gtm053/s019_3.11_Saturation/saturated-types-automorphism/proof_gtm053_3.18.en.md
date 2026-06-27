---
role: proof
locale: en
of_concept: saturated-types-automorphism
source_book: gtm053
source_chapter: "3"
source_section: "3.18"
---

We prove the left-to-right implication; the converse is trivial since automorphisms preserve types.

Assume $\text{tp}(\bar{a}) = \text{tp}(\bar{b})$. Extend the language $L$ by $n$ constant symbols to name $\bar{a}$ (obtaining $\mathbf{A}_a$) and to name $\bar{b}$ (obtaining $\mathbf{A}_b$). Both expansions remain saturated models in the extended language. Since $\text{tp}_{\mathbf{A}}(\bar{a}) = \text{tp}_{\mathbf{A}}(\bar{b})$, the two expansions are elementarily equivalent. By the uniqueness of saturated models (Theorem 3.12(ii)), there exists an isomorphism $\pi : \mathbf{A}_a \to \mathbf{A}_b$ fixing $L$. This isomorphism satisfies $\pi(\bar{a}) = \bar{b}$ and is an $L$-automorphism of $\mathbf{A}$.
