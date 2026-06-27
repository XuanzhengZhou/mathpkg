---
role: proof
locale: en
of_concept: cartesian-basis-of-eigenvectors-symmetric
source_book: gtm049
source_chapter: "VI"
source_section: "6.3"
---
By Lemma 2, we can find an eigenvector $$a_1$$ of $$f$$ with real eigenvalue. Since $$\sigma$$ is positive definite, we may choose $$a_1$$ so that $$\sigma(a_1, a_1) = 1$$. The subspace $$[a_1]$$ is non-degenerate with respect to $$\sigma$$, and therefore by Proposition 5 of Chapter V (p. 96),
$$V = [a_1] \oplus [a_1]^{\perp(\sigma)}.$$
The result now follows by Lemma 3 and induction on $$\dim V$$: the restriction of $$f$$ to $$[a_1]^{\perp(\sigma)}$$ is again $$\sigma$$-symmetric, so by the induction hypothesis we obtain a Cartesian basis of eigenvectors there.
