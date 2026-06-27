---
role: proof
locale: en
of_concept: characteristic-class-stability-criterion
source_book: gtm020
source_chapter: "20"
source_section: "2"
---

The first statement says that $\phi$ factors through the group completion $K_F$ if and only if its image is included in a subgroup of $H(X)$ for each $X$. Since in a group every element has an inverse, $\phi(\xi)$ must be invertible for each bundle class $\xi$ if $\phi$ is to factor through $K_F$. Conversely, if every $\phi(\xi)$ is invertible in the semigroup $H(X)$, then the image of $\phi$ lies in the subgroup of invertible elements of $H(X)$, so $\phi$ factors through the group completion.

The second statement follows from the first, because each bundle $\xi$ has an $s$-inverse $\eta$, where $\xi \oplus \eta$ is trivial. Then
$$\phi(\xi \oplus \eta) = \phi(\xi)\phi(\eta)$$
is the neutral element of $H(X)$. If $\phi(\theta^q)$ is the neutral element for each trivial bundle class $\theta^q$, then for the trivial bundle $\xi \oplus \eta$ we have $\phi(\xi)\phi(\eta) = e$. Hence $\phi(\eta)$ is an inverse for $\phi(\xi)$, so $\phi(\xi)$ is invertible. By the first statement, $\phi$ is stable.
