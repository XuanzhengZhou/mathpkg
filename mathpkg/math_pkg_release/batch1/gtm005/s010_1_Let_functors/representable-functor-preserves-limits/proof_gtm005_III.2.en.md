---
role: proof
locale: en
of_concept: representable-functor-preserves-limits
source_book: gtm005
source_chapter: "III"
source_section: "2"
---

Let $K: D^{\mathrm{op}} \to \mathbf{Set}$ be representable, so $K \cong D(-, r)$. Hom-functors preserve limits: for any limit $\varprojlim X_j$ in $D$,
$$D(d, \varprojlim X_j) \cong \varprojlim D(d, X_j)$$
naturally in $d$. This follows because a cone $\{\ell_j: d \to X_j\}$ corresponds to a unique map $d \to \varprojlim X_j$ by the universal property of the limit.

Since representables preserve limits and $K \cong D(-, r)$, we have
$$K(\varprojlim X_j) \cong D(\varprojlim X_j, r) \cong \varprojlim D(X_j, r) \cong \varprojlim K(X_j).$$
Thus representable functors preserve all limits (they are continuous). Dually, corepresentable functors $D(r, -)$ preserve colimits.
