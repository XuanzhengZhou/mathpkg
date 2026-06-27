---
role: proof
locale: en
of_concept: neumann-series
source_book: gtm055
source_chapter: "12"
source_section: "Bounded linear transformations"
---

If $|\lambda| > \|x\|$ and if we define $r = \|x/\lambda\|$, then $r < 1$ and $\|x^n/\lambda^n\| \leq r^n$ for every positive integer $n$. Hence the series $\sum_{n=0}^{\infty} x^n/\lambda^{n+1}$ converges absolutely in the Banach algebra $\mathcal{A}$. Multiplying this series by $\lambda - x$ gives

$$(\lambda - x) \sum_{n=0}^{\infty} \frac{x^n}{\lambda^{n+1}} = \sum_{n=0}^{\infty} \frac{x^n}{\lambda^n} - \sum_{n=0}^{\infty} \frac{x^{n+1}}{\lambda^{n+1}} = 1_{\mathcal{A}},$$

and similarly for multiplication on the other side, so the sum equals $(\lambda - x)^{-1}$. Therefore every $\lambda$ with $|\lambda| > \|x\|$ belongs to the resolvent set, and $\sigma(x) \subseteq \{\lambda: |\lambda| \leq \|x\|\}$.
