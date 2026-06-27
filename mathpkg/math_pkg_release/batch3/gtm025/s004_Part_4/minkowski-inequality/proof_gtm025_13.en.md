---
role: proof
locale: en
of_concept: minkowski-inequality
source_book: gtm025
source_chapter: "4"
source_section: "13"
---

First note $|f+g|^p \leq (|f|+|g|)^p \leq 2^p(|f|^p+|g|^p)$, so $f+g \in \mathfrak{L}_p$. For $p=1$, the inequality is immediate. For $p>1$: $\int |f+g|^p d\mu = \int |f+g||f+g|^{p-1} d\mu \leq \int |f||f+g|^{p-1} d\mu + \int |g||f+g|^{p-1} d\mu$. Apply Holder's inequality to each term: $\int |f||f+g|^{p-1} d\mu \leq \|f\|_p (\int |f+g|^{(p-1)p'} d\mu)^{1/p'} = \|f\|_p \|f+g\|_p^{p-1}$. Thus $\|f+g\|_p^p \leq (\|f\|_p + \|g\|_p)\|f+g\|_p^{p-1}$, giving Minkowski's inequality.
