---
role: proof
locale: en
of_concept: long-exact-sequence-of-ext
source_book: gtm052
source_chapter: "III"
source_section: "6"
---

[Note: The proof in the source text is truncated. The standard proof proceeds as follows.]

For fixed $\mathcal{G}$, the functor $T = \operatorname{Hom}(-,\mathcal{G})$ is left exact contravariant on $\operatorname{Mod}(X)$. Given a short exact sequence $0 \to \mathcal{F}' \to \mathcal{F} \to \mathcal{F}'' \to 0$, choose an injective resolution $\mathcal{G} \to I^\bullet$ of $\mathcal{G}$. Apply the left exact contravariant functors $\operatorname{Hom}(-,\mathcal{G})$, $\operatorname{Hom}(-,\mathcal{F})$, and $\operatorname{Hom}(-,\mathcal{F}'')$ to the sequence, obtaining a short exact sequence of complexes of abelian groups:
$$0 \to \operatorname{Hom}(\mathcal{F}'', I^\bullet) \to \operatorname{Hom}(\mathcal{F}, I^\bullet) \to \operatorname{Hom}(\mathcal{F}', I^\bullet) \to 0$$
which is exact because $I^k$ is injective for each $k$, so the contravariant Hom functor preserves exactness when the second argument is injective. Taking cohomology of this short exact sequence of complexes yields the desired long exact sequence. The proof for $\mathcal{E}xt$ sheaves is similar, applying the sheaf Hom functor and using the fact that injective $\mathcal{O}_X$-modules are also injective for the sheaf Hom.
