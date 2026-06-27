---
role: proof
locale: en
of_concept: solution-set-condition-for-colimits
source_book: gtm026
source_chapter: "7"
source_section: "7.1"
---

*Proof.* This is an immediate consequence of the General Adjoint Functor Theorem (2.2.24). By Theorem 7.2, a colimit of $(\Delta, D)$ is precisely a free object over $D$ with respect to the embedding functor $(\tilde{\cdot}): \mathcal{K} \to \mathcal{K}^{\Delta}$. Thus the existence of all colimits of type $\Delta$ is equivalent to the existence of a left adjoint to $(\tilde{\cdot})$. By Proposition 7.3, $(\tilde{\cdot})$ preserves limits, and by Theorem 2.1.22, $\mathcal{K}^{\Delta}$ is locally small (since $\Delta$ is small). The General Adjoint Functor Theorem 2.2.24 then asserts that $(\tilde{\cdot})$ has a left adjoint if and only if it satisfies the solution set condition. $\square$
