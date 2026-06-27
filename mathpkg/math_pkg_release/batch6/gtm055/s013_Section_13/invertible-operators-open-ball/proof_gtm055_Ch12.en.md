---
role: proof
locale: en
of_concept: invertible-operators-open-ball
source_book: gtm055
source_chapter: "12"
source_section: "Bounded linear transformations"
---

Let $S = 1_{\mathcal{E}} - T$ with $\|S\| < 1$. Then the series $\sum_{n=0}^{\infty} S^n$ converges absolutely in the Banach algebra $\mathcal{L}(\mathcal{E})$ since $\|S^n\| \leq \|S\|^n$ and $\sum \|S\|^n$ converges (geometric series with ratio $< 1$). Let $R = \sum_{n=0}^{\infty} S^n$. Then

$$RT = R(1_{\mathcal{E}} - S) = \sum_{n=0}^{\infty} S^n - \sum_{n=0}^{\infty} S^{n+1} = 1_{\mathcal{E}},$$

and similarly $TR = 1_{\mathcal{E}}$, so $R = T^{-1}$.
