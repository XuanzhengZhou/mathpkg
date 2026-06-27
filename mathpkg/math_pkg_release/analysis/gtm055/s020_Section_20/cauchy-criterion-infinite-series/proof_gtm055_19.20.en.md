---
role: proof
locale: en
of_concept: cauchy-criterion-infinite-series
source_book: gtm055
source_chapter: "19"
source_section: "20"
---

Let $s_N = \sum_{n=0}^{N} x_n$. The series converges if and only if $\{s_N\}$ is a Cauchy sequence in $\mathcal{E}$. But $s_{K+p} - s_{K-1} = \sum_{n=K}^{K+p} x_n$, so the condition $\|\sum_{n=K}^{K+p} x_n\| < \varepsilon$ for all $p$ is precisely the statement that $\{s_N\}$ is Cauchy. Since $\mathcal{E}$ is a Banach space (complete), the Cauchy criterion for sequences gives the result.
