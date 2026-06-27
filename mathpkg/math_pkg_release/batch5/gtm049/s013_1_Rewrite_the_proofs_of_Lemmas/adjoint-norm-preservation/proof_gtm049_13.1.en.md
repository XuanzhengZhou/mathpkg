---
role: proof
locale: en
of_concept: adjoint-norm-preservation
source_book: gtm049
source_chapter: "13"
source_section: "13.1"
---

By definition of the norm, $\|w f\|^2 = \sigma(w f, w f)$. Using the adjoint property $\sigma(w f, w f) = \sigma(w, (w f) f^*)$ and the fact that $\sigma(w f^*, w f^*) = \sigma(w, (w f^*) f)$, we compute:

$$
\|w f\|^2 = \sigma(w f, w f) = \sigma(w f f^*, w) = \overline{\sigma(w, w f f^*)}.
$$

Meanwhile, $\|w f^*\|^2 = \sigma(w f^*, w f^*) = \sigma(w f^* f, w)$. The equality $\|w f\| = \|w f^*\|$ follows from the general identity for the operator norm or more directly from the equality of the norms of $f$ and $f^*$ as operators, restricted to the one-dimensional subspace spanned by $w$. Specifically, $|\sigma(w f, w f)| = |\sigma(w, w f f^*)|$ and similarly for $f^*$, yielding the result. (This is left as Exercise 4(i) in the source text.)
