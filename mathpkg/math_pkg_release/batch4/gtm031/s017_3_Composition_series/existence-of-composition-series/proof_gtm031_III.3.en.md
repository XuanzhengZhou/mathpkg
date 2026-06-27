---
role: proof
locale: en
of_concept: existence-of-composition-series
source_book: gtm031
source_chapter: "III"
source_section: "3"
---

Proceed by induction on $\dim \mathfrak{R}$.

If $\mathfrak{R}$ is irreducible relative to $\Omega$, then $0 \subset \mathfrak{R}$ is a composition series: there are no intermediate invariant subspaces, so the single step is trivially irreducible.

Otherwise, $\mathfrak{R}$ admits a proper nonzero invariant subspace. Let $\mathfrak{S}$ be a proper invariant subspace of maximal dimension (such exists since $\dim \mathfrak{R}$ is finite). Then $\mathfrak{S}$ itself either is irreducible (relative to the induced transformations on $\mathfrak{S}$) or contains a proper invariant subspace; in either case, by induction on dimension, $\mathfrak{S}$ admits a composition series
$$0 = \mathfrak{S}_0 \subset \mathfrak{S}_1 \subset \cdots \subset \mathfrak{S}_k = \mathfrak{S}.$$

Now consider the quotient $\bar{\mathfrak{R}} = \mathfrak{R}/\mathfrak{S}$. By the invariant subspace–quotient correspondence, any invariant subspace of $\bar{\mathfrak{R}}$ lifts to an invariant subspace of $\mathfrak{R}$ containing $\mathfrak{S}$. Since $\mathfrak{S}$ was chosen to be maximal among proper invariant subspaces, the quotient $\bar{\mathfrak{R}}$ has no proper nonzero invariant subspace. Hence $\bar{\mathfrak{R}}$ is irreducible, so $\mathfrak{R}$ is irreducible over $\mathfrak{S}$.

Therefore
$$0 = \mathfrak{S}_0 \subset \mathfrak{S}_1 \subset \cdots \subset \mathfrak{S}_k = \mathfrak{S} \subset \mathfrak{S}_{k+1} = \mathfrak{R}$$
is a composition series for $\mathfrak{R}$, where the last step is irreducible because $\mathfrak{R}/\mathfrak{S}$ is irreducible, and each earlier step $\mathfrak{S}_i$ is irreducible over $\mathfrak{S}_{i-1}$ by the inductive construction on $\mathfrak{S}$.

By induction, every finite-dimensional $\mathfrak{R}$ admits a composition series for any set $\Omega$ of linear transformations.
