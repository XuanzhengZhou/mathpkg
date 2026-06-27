---
role: proof
locale: en
of_concept: lebesgue-radon-nikodym-finite
source_book: gtm025
source_chapter: ""
source_section: "19"
---

Let $g$ be from Lemma 19.22. For bounded nonnegative $f$, the function $(1+g+\cdots+g^{n-1})f$ is in $\mathfrak{L}_2(\mu+\nu)$. By 19.22, $\int (1+g+\cdots+g^{n-1})f(1-g) d\nu = \int (1+g+\cdots+g^{n-1})fg d\mu$. The left side simplifies to $\int f(1-g^n) d\nu \to \int f d\nu$ by dominated convergence. The right side $\int f(g+\cdots+g^n) d\mu$ tends to $\int f f_0 d\mu$ where $f_0 = \lim_n \sum_{k=1}^n g^k$ by monotone convergence. Extension to general $f$ is by standard arguments.
