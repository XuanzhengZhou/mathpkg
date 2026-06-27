---
role: proof
locale: en
of_concept: lemma-eigenvalue-form
source_book: gtm049
source_chapter: "6"
source_section: "6.5"
---

Let $c = a + ib$ be an eigenvector of $f$ with given eigenvalue $x$: $cf = xc$. Then $\bar{c}f = \bar{x}\bar{c}$ and hence

$$\sigma'(\bar{c}f, cf) = \sigma'(\bar{x}\bar{c}, xc) = \bar{x}x\sigma'(\bar{c}, c);$$

while

$$\sigma'(\bar{c}f, cf) = \sigma'(\bar{c}, c)$$

because $f$ preserves $\sigma'$ (since $f$ is an automorphism of the euclidean space $(V, \sigma)$, the extended $f$ preserves $\sigma'$). Since $c \neq 0$, $\sigma'(\bar{c}, c) = \sigma(a, a) + \sigma(b, b) > 0$ and hence $\bar{x}x = 1$. Thus $x = e^{i\theta}$ for some real number $\theta$ which may be chosen to satisfy $-\pi < \theta \leq \pi$.
