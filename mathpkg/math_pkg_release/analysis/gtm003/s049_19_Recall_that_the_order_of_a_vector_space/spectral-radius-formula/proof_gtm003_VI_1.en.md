---
role: proof
locale: en
of_concept: spectral-radius-formula
source_book: gtm003
source_chapter: "VI"
source_section: "1"
---

For $|\lambda| > \|x\|$, the Neumann series gives $(\lambda e - x)^{-1} = \sum_{n=0}^\infty x^n / \lambda^{n+1}$, so $\sigma(x) \subset \{|\lambda| \leq \|x\|\}$. By the spectral mapping theorem, $r(x)^n = r(x^n) \leq \|x^n\|$, so $r(x) \leq \liminf \|x^n\|^{1/n}$. Conversely, the resolvent $R(\lambda, x)$ is analytic on $\rho(x)$, and for $|\lambda| > r(x)$ the Laurent expansion $\sum x^n / \lambda^{n+1}$ converges, giving $\limsup \|x^n\|^{1/n} \leq r(x)$. The equality follows.
