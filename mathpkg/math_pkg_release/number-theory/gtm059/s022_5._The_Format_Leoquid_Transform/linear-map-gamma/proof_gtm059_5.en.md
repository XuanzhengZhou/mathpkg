---
role: proof
locale: en
of_concept: linear-map-gamma
source_book: gtm059
source_chapter: ""
source_section: "5"
---

In light of the lemma, a power series $f(X)$ has the expression

$$f(X) = \sum_{k=1}^{n-1} \frac{a_k}{n!} \frac{X^k}{k!}.$$

Consequently,

$$\Gamma(f) = \sum_{k=1}^{n-1} \frac{y_k(k)}{n!} \frac{X^k}{(n-1)!} = \sum_{k=1}^{n-1} \frac{a_k}{n!} \Gamma\left(\frac{X^k}{k!}\right).$$

These formulas establish the existence and uniqueness of the linear map $\Gamma: K[X] \to C(\mathbb{Z}, K)$ satisfying the stated equivalent conditions. The map sends a polynomial to the function on $\mathbb{Z}$ obtained by applying the Leopoldt transform to the corresponding power series. The equivalence of the three conditions follows from the properties of the coefficients $y_k$ established in the preceding lemma.
