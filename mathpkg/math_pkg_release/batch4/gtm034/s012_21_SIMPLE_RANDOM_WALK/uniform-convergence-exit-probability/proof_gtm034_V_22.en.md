---
role: proof
locale: en
of_concept: uniform-convergence-exit-probability
source_book: gtm034
source_chapter: "V"
source_section: "22"
---

Using P22.6(b), \(R_N(x) = \frac{x}{N} + \frac{1}{N}\sum_{k=1}^{\infty} k L_N(x,k) - \frac{1}{N}\sum_{k=1}^{\infty} k R_N(x,k)\). By P22.5 and the estimate \(\frac{1}{N}\sum_{k} k R_N(x,k) \leq \frac{M}{N}\sum_{s=0}^{N}(1+s)a(s)\) where \(a(s) = \sum_{k} kP(0,s+k)\), and using \(\sum_{s} a(s) < \infty\) (which follows from \(\sigma^2 < \infty\) and Kronecker's lemma), the error terms vanish uniformly.
