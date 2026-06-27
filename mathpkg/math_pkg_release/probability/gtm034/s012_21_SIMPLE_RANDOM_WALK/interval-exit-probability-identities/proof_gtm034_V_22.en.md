---
role: proof
locale: en
of_concept: interval-exit-probability-identities
source_book: gtm034
source_chapter: "V"
source_section: "22"
---

For (a), rewrite the left side as \(\sum_{y=0}^{N} g_N(x,y)[1 - \sum_{s=0}^{N} P(y,s)]\). Using \(\sum_{y=0}^{N} g_N(x,y)P(y,s) = g_N(x,s) - \delta(x,s)\), the sum telescopes to 1. For (b), transform the left side into \(\sum_{y=0}^{N} g_N(x,y)[\sum_{j=-\infty}^{\infty} jP(y,j) - \sum_{j=0}^{\infty} jP(y,j)]\) and use the martingale property \(\sum_j jP(y,j) = y\) (since \(\mu = 0\)) to obtain the result.
