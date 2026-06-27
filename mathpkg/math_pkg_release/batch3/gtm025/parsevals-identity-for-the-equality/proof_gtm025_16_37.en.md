---
role: proof
locale: en
of_concept: "parsevals-identity-for-the-equality"
source_book: gtm025
source_chapter: "Integration on Locally Compact Spaces"
source_section: "16.37"
---

This is an immediate consequence of (16.26), (16.3

Proof. This is a trivial consequence of the completeness of $\mathfrak{L}_2$ (13.11). Let

$$f_k(t) = \sum_{j=-k}^{k} \alpha_j \exp(ijt) \quad (k=1, 2, \ldots).$$

Then the equality $\|f_k - f_l\|_2^2 = \sum_{j=-l}^{-k-1} |\alpha_j|^2 + \sum_{j=k+1}^{l} |\alpha_j|^2$ shows that $(f_k)$ is a Cauchy sequence. Let $f$ be the limit in $\mathfrak{L}_2$ of $(f_k)$. We clearly have $f(n) = \lim_{k \to \infty} f_k(n) = \alpha_n$.
