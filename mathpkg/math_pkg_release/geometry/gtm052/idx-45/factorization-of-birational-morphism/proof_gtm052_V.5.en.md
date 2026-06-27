---
role: proof
locale: en
of_concept: factorization-of-birational-morphism
source_book: gtm052
source_chapter: "V"
source_section: "5"
---

**Proof.** If $f(C')$ is a point $P$, then $P$ is a fundamental point of $f^{-1}$. By (5.1) the fundamental points of $f^{-1}$ form a finite set, and for each one, its inverse image $f^{-1}(P)$ is a closed subset of $X'$, having only finitely many irreducible components, so the set of curves $C'$ which are mapped to a point is finite.

Now let $P$ be a fundamental point of $f^{-1}$. Then by (5.3) $f$ factors through the monoidal transformation $\pi: \tilde{X} \to X$ with center $P$, i.e., $f = \pi \circ f_1$ for some morphism $f_1: X' \to \tilde{X}$. We will show that $n(f_1) = n(f) - 1$. Indeed, if $f_1(C')$ is a point, then certainly $f(C')$ is a point. Conversely, if $f(C')$ is a point, then either $f_1(C')$ is a point, or $f_1(C') = E$, the exceptional curve of $\pi$. Furthermore, since $f_1^{-1}$ is a morphism except at finitely many points, there is a unique irreducible curve $E'$ in $X'$ with $f_1(E') = E$. Thus $n(f_1) = n(f) - 1$.

Continuing in this fashion, after factoring through $n(f)$ monoidal transformations, we reduce to a morphism with $n(f) = 0$. But by (5.2), such a morphism has no fundamental points, so it is an isomorphism. Thus $f$ is factored into $n(f)$ monoidal transformations.
