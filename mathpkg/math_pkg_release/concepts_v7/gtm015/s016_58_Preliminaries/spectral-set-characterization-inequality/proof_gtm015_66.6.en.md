---
role: proof
locale: en
of_concept: spectral-set-characterization-inequality
source_book: gtm015
source_chapter: "66"
source_section: "Spectral sets"
---

# Proof of Spectral set characterization via norm inequality

Proof. (a) implies (b): If $f \in \mathbb{C}(t)$ and $\|f\|_{\sigma} \leq 1$ then $f$ can have no poles in $\sigma$, i.e., $f \in \mathbb{C}(t; \sigma)$, thus $\|f(T)\| \leq \|f\|_{\sigma} \leq 1$.

(b) implies (a): Assuming $f \in \mathbb{C}(t; \sigma)$, it is to be shown that $\|f(T)\| \leq \|f\|_{\sigma}$. The inequality holds trivially if $\|f\|_{\sigma} = \infty$ (which means that $f$ has a pole in $\bar{\sigma}$); it also holds if $\|f\|_{\sigma} = 0$, since application of (b) to $nf(n = 1, 2, 3, \ldots)$ yields $\|f(T)\| = 0$; and if $0 < \|f\|_{\sigma} < \infty$, the desired inequality results on applying (b) to $\|f\|_{\sigma}^{-1}f$.

Every superset of a spectral set is a spectral set:
