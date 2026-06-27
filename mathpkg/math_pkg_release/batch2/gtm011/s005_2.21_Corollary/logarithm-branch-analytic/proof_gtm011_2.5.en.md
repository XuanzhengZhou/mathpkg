---
role: proof
locale: en
of_concept: logarithm-branch-analytic
source_book: gtm011
source_chapter: "2"
source_section: "5"
---

This follows directly from Proposition 2.20. Let $g(z) = e^z$, which is analytic on all of $\mathbb{C}$ with $g'(z) = e^z \neq 0$ for all $z$. For any branch $f$ of the logarithm, we have $g(f(z)) = e^{\log z} = z$ by definition. Applying Proposition 2.20 with $h(z) = z$ (the identity, which is analytic and one-to-one), we conclude that $f$ is analytic. Moreover,

$$f'(z) = \frac{1}{g'(f(z))} = \frac{1}{e^{\log z}} = \frac{1}{z}.$$

Thus any branch of the logarithm is analytic on its domain of definition and has derivative $z^{-1}$.
