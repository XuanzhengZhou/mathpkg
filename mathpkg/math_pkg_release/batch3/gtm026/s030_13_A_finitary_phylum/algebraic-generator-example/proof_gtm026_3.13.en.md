---
role: proof
locale: en
of_concept: algebraic-generator-example
source_book: gtm026
source_chapter: "3"
source_section: "13"
---

We show that for nonempty $n$, the free $T$-algebra $(nT, n\mu)$ is an algebraic generator, i.e., the representable functor

$$\mathbf{Set}^T((nT, n\mu), -): \mathbf{Set}^T \rightarrow \mathbf{Set}$$

is weakly algebraic.

By [Lawvere '63, Chapter III, Section 2], it suffices to show that this representable functor satisfies the Beck condition for certain coequalizers. The key observation is the natural isomorphism

$$\mathbf{Set}^T((nT, n\mu), (X, \xi)) \cong \mathbf{Set}(n, X) \cong X^n$$

coming from the adjunction $F \dashv U$ between the free $T$-algebra functor and the underlying set functor. Here $X^n$ denotes the $n$-fold product of $X$ with itself.

Using Exercises 10 and 11 with respect to the functor $U_3 = (-)^n: \mathbf{Set} \rightarrow \mathbf{Set}$, one verifies that $(-)^n$ is weakly algebraic (as a finite power functor preserves filtered colimits and reflects isomorphisms). Since the isomorphism above is natural, the representable functor inherits the weakly algebraic property.

The condition that $n$ is nonempty ensures that $(-)^n$ is faithful (an $n$-tuple of functions determines each component function when there is at least one coordinate), which is needed for the weakly algebraic condition.
