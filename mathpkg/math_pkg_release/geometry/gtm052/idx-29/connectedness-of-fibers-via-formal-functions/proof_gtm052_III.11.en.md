---
role: proof
locale: en
of_concept: connectedness-of-fibers-via-formal-functions
source_book: gtm052
source_chapter: "III"
source_section: "11"
---

*Proof.* Suppose to the contrary that $f^{-1}(y) = X' \cup X''$, where $X'$ and $X''$ are disjoint closed subsets. Then for each $n$, we would have
$$
H^0(X_n, \mathcal{O}_{X_n}) = H^0(X_n', \mathcal{O}_{X_n}) \oplus H^0(X_n'', \mathcal{O}_{X_n}),
$$
where $X_n'$ and $X_n''$ are the corresponding thickened subschemes.

By the Theorem on Formal Functions (case $i = 0$), we have
$$
\widehat{\mathcal{O}}_y = (f_* \mathcal{O}_X)_y^{\widehat{\ }} = \varprojlim_{n} H^0(X_n, \mathcal{O}_{X_n}).
$$
Therefore $\widehat{\mathcal{O}}_y = A' \oplus A''$, where
$$
A' = \varprojlim_{n} H^0(X_n', \mathcal{O}_{X_n}), \qquad
A'' = \varprojlim_{n} H^0(X_n'', \mathcal{O}_{X_n}).
$$

But this is impossible, because a local ring cannot be a direct sum of two other rings. Indeed, let $e', e''$ be the unit elements of $A'$ and $A''$. Then $e' + e'' = 1$ in $\widehat{\mathcal{O}}_y$. On the other hand, $e'e'' = 0$, so $e', e''$ are non-units, hence contained in the maximal ideal of $\widehat{\mathcal{O}}_y$, so their sum cannot be $1$ (cf. (II, Ex. 2.19)). $\square$
