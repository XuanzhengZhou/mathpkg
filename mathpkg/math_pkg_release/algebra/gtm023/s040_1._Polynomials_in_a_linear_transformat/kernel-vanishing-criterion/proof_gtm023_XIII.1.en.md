---
role: proof
locale: en
of_concept: kernel-vanishing-criterion
source_book: gtm023
source_chapter: "XIII"
source_section: "§1. Polynomials in a linear transformation"
---

If $f$ and $\mu$ are relatively prime, then Corollary I to Proposition II gives

$$K(f) = K(f) \cap E = K(f) \cap K(\mu) = K(1) = 0.$$

Conversely, suppose $K(f) = 0$. Let $d = \gcd(f, \mu)$. Then $1 \mid d$ and $d \mid \mu$, and by Corollary I to Proposition I,

$$K(d) = K(f) \cap K(\mu) = 0 \cap E = 0 = K(1).$$

If $d$ were a proper multiple of $1$, then $1$ would be a proper divisor of $d$ with $d \mid \mu$, and Proposition III would imply $K(1) \subsetneq K(d)$, contradicting $K(1) = K(d) = 0$. Hence $d = 1$, so $f$ and $\mu$ are relatively prime.
