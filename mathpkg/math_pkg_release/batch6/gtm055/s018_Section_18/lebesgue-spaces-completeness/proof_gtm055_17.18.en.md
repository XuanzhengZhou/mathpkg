---
role: proof
locale: en
of_concept: lebesgue-spaces-completeness
source_book: gtm055
source_chapter: "17"
source_section: "18"
---

It suffices to show that if a Cauchy sequence $\{f_n\}$ satisfies the added condition

$$\sum_{n=1}^{\infty} \|f_{n+1} - f_n\|_p < +\infty,$$

then the sequence converges. Set $g_n = f_{n+1} - f_n$ (which we may take to be nonnegative). Set $h_n = g_1 + \cdots + g_n$. Then $\|h_n\|_p \leq \|g_1\|_p + \cdots + \|g_n\|_p$ by the Minkowski inequality, and consequently

$$\int_X h_n^p d\mu = \|h_n\|_p^p \leq \left[ \sum_{k=1}^n \|g_k\|_p \right]^p \leq \left[ \sum_{k=1}^{\infty} \|g_n\|_p \right]^p < +\infty.$$

Since $\{h_n^p\}$ is a monotone increasing sequence, it follows from the monotone convergence theorem that the sequence $\{h_n^p\}$ converges a.e. $[\mu]$. Hence $\{h_n\}$ also converges a.e. $[\mu]$, and if we write $g = \lim_n h_n$, then $h_n^p \to g^p$ a.e. as well. But then $\int_X g^p d\mu \leq \left( \sum_{n=1}^{\infty} \|g_n\|_p \right)^p$, and the theorem follows.
