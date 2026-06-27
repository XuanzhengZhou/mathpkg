---
role: proof
locale: en
of_concept: free-objects-are-projective
source_book: gtm004
source_chapter: "II"
source_section: "10"
---

# Proof of Free Objects are Projective

Let $\mathfrak{C}$ be a category with a free functor $Fr: \mathfrak{S} \to \mathfrak{C}$, left adjoint to the underlying functor $U: \mathfrak{C} \to \mathfrak{S}$. Thus $Fr \dashv U$, and for any set $S$, $Fr(S)$ is the free object on $S$ in $\mathfrak{C}$.

Assume $U$ maps epimorphisms in $\mathfrak{C}$ to surjections in $\mathfrak{S}$. This hypothesis holds, for example, in $\mathfrak{Ab}$, $\mathfrak{M}_A$, and $\mathfrak{G}$ (groups), where epimorphisms are precisely the surjective homomorphisms.

By Proposition 10.2, since $Fr$ is a left adjoint and $U$ sends epimorphisms to epimorphisms (= surjections in $\mathfrak{S}$), $Fr$ maps projectives to projectives. But every set in $\mathfrak{S}$ is projective (Proposition 10.1). Hence for any set $S$, $Fr(S)$ is a projective object in $\mathfrak{C}$.

Thus every free object is projective. $\square$

**Remark.** The hypothesis on $U$ fails for the category of integral domains: the inclusion $\mathbb{Z} \hookrightarrow \mathbb{Q}$ is an epimorphism that is not surjective, so free objects (polynomial rings) in the category of integral domains may not be projective in the categorical sense.
