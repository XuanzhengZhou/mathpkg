---
role: proof
locale: en
of_concept: conditional-borel-cantelli
source_book: gtm046
source_chapter: "IX"
source_section: "32"
---
Let $B_n$ be events and $\mathfrak{B}_n$ be $\sigma$-fields such that $B_n \in \mathfrak{B}_n$. Set $[\nu = n] = [\sup_{k < n} X_k \leq a, X_n > a]$ and $[\nu = \infty] = [\sup X_n \leq a]$. The $\nu$-truncated sequence $X'_n = \sum_{k=1}^n Y'_k$ is a martingale bounded above by $a + 1$, hence $X'_n \xrightarrow{\text{a.s.}} X'$ finite.

Since $0 \leq \sum_{k=1}^n I_{B_k} \uparrow$ and $0 \leq \sum_{k=1}^n P^{\mathfrak{B}_{k-1}} B_k \uparrow$ a.s., both sequences have a.s. a limit (finite or infinite). If one is finite and the other infinite, then $\sup X_n(\omega) = +\infty$ or $\inf X_n(\omega) = -\infty$. Thus both limits are simultaneously either finite or infinite, proving the conditional Borel-Cantelli assertion.
