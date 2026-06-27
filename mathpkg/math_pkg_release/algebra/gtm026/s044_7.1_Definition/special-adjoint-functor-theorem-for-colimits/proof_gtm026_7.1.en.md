---
role: proof
locale: en
of_concept: special-adjoint-functor-theorem-for-colimits
source_book: gtm026
source_chapter: "7"
source_section: "7.1"
---

*Proof.* This follows the same strategy as Theorem 7.4, but using the Special Adjoint Functor Theorem (2.2.29) in place of the General Adjoint Functor Theorem (2.2.24). By Theorem 7.2, colimits of type $\Delta$ correspond to free objects over the diagram with respect to the embedding functor $(\tilde{\cdot}): \mathcal{K} \to \mathcal{K}^{\Delta}$, i.e., to a left adjoint of $(\tilde{\cdot})$. The Special Adjoint Functor Theorem 2.2.29 guarantees the existence of such a left adjoint when the domain is locally small, complete, well-powered, and has a cogenerator. It is crucial here that $\mathcal{K}^{\Delta}$ be locally small, which follows from the requirement that $\Delta$ be a small diagram scheme. $\square$
