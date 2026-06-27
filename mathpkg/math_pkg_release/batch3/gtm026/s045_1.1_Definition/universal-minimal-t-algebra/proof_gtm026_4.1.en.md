---
role: proof
locale: en
of_concept: universal-minimal-t-algebra
source_book: gtm026
source_chapter: "4"
source_section: "1"
---

*Proof.* Property 1 is given. For property 2, if $(Y, \theta)$ is a minimal $T$-algebra, then since $(X, \xi)$ is universal minimal, there exists a $T$-homomorphism $f: (X, \xi) \longrightarrow (Y, \theta)$. By Lemma 1.2, since $X$ is nonempty and $(Y, \theta)$ is minimal, $f$ must be onto.

For property 3, let $f: (X, \xi) \longrightarrow (X, \xi)$ be a $T$-endomorphism. Since $X$ is nonempty, $\operatorname{Im}(f)$ is a nonempty subalgebra of the minimal algebra $(X, \xi)$, so $\operatorname{Im}(f) = X$, i.e., $f$ is surjective. To show injectivity: since $(X, \xi)$ is minimal, the kernel pair of $f$ must be trivial (otherwise its equalizer would be a proper nonempty subalgebra), hence $f$ is injective and therefore an isomorphism.

That any algebra satisfying properties 1 and 2 is isomorphic to the universal minimal one follows from the fact that there exist homomorphisms in both directions, and by property 3 applied to the composition, these must be mutual inverses. $\square$
