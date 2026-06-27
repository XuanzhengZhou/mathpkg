---
role: proof
locale: en
of_concept: killing-form-nondegenerate
source_book: gtm004
source_chapter: "VII"
source_section: "5"
---

# Proof of Non-degeneracy of the Killing Form

**Corollary 5.3.** The Killing form of a semi-simple Lie algebra (over a field of characteristic 0) is non-degenerate.

Recall that the Killing form $\kappa : \mathfrak{g} \times \mathfrak{g} \to K$ is defined by

$$\kappa(x, y) = \operatorname{Tr}(\operatorname{ad} x \circ \operatorname{ad} y),$$

where $\operatorname{ad} : \mathfrak{g} \to \operatorname{End}_K(\mathfrak{g})$ is the adjoint representation.

**Proof.** The structure map $\operatorname{ad} : \mathfrak{g} \to \operatorname{End}_K(\mathfrak{g})$ of the $\mathfrak{g}$-module $\mathfrak{g}$ has the center of $\mathfrak{g}$ as kernel (see Exercise 1.2). Since the center is an abelian ideal and $\mathfrak{g}$ is semi-simple, the center is trivial. Hence $\operatorname{ad}$ is injective; that is, the adjoint representation is faithful.

By Theorem 5.2, if $\mathfrak{g}$ is semi-simple (over a field of characteristic 0) and $A$ is a $\mathfrak{g}$-module whose structure map $\varrho : \mathfrak{g} \to \operatorname{End}_K(A)$ is injective (i.e., a faithful representation), then the associated bilinear form

$$\beta(x, y) = \operatorname{Tr}(\varrho x \circ \varrho y)$$

is non-degenerate.

Applying this to $A = \mathfrak{g}$ with $\varrho = \operatorname{ad}$, we obtain that the Killing form $\kappa = \beta$ is non-degenerate. $\square$
