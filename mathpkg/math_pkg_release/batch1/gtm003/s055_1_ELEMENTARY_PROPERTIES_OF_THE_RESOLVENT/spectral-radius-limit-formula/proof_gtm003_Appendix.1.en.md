---
role: proof
locale: en
of_concept: spectral-radius-limit-formula
source_book: gtm003
source_chapter: "Appendix"
source_section: "1. Elementary Properties of the Resolvent"
---

This is a well-known result in spectral theory; for a detailed proof see Hille-Phillips [1]. The proof relies on the fact that the resolvent $R(\lambda)$ is given by the Neumann series
$$R(\lambda) = \sum_{n=0}^{\infty} \lambda^{-(n+1)} u^n$$
for $|\lambda| > \limsup \|u^n\|^{1/n}$, which converges precisely for $|\lambda| > r(u)$. The radius of convergence of this Laurent series is exactly $r(u)$, yielding the formula $r(u) = \limsup \|u^n\|^{1/n}$. That this limsup is actually a limit follows from the submultiplicativity of the norm.
