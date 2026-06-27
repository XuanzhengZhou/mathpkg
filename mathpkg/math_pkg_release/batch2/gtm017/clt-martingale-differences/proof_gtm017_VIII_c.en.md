---
role: proof
locale: en
of_concept: clt-martingale-differences
source_book: gtm017
source_chapter: "VIII"
source_section: "c"
---
Let $S_n = \frac{1}{\sqrt{n}}\sum X_j$, $\sigma_{nk}^2 = \frac{1}{n}E(X_k^2|\mathcal{B}_{k-1})$, $V_{nk}^2 = \sum_{j=1}^k \sigma_{nj}^2$. By ergodicity, $V_{nn}^2 \to 1$ almost surely. Truncate using $V_{nn}^2 \leq 2$ w.p.1 (works asymptotically).

Let $g_t(x) = (e^{itx} - 1 - itx)/x^2$. Then $\sum_{k=1}^n E(g_t(X_{nk}) X_{nk}^2 | \mathcal{B}_{k-1}) \to -t^2/2$ in probability, where $X_{nk} = X_k/\sqrt{n}$. Defining a telescoping exponential martingale:
$$E \exp(it S_n) = E \prod_{k=1}^n \exp(it X_{nk} - E(g_t(X_{nk})X_{nk}^2|\mathcal{B}_{k-1})) + o(1) \to e^{-t^2/2}.$$

Apply the continuity theorem for characteristic functions to get asymptotic normality.
