---
role: proof
locale: en
of_concept: absolute-continuity-of-the-lebesgue-integral
source_book: gtm040
source_chapter: "1"
source_section: "4"
---
Set $f_n = \min(f, n)$. By Theorem 1-44, $\lim_n \int_X f_n d\mu = \int_X f d\mu$. Since $f$ is integrable, find $N$ such that $\int_X (f - f_N) d\mu < \epsilon/2$. Let $\delta = \epsilon/(2N)$. If $\mu(E) < \delta$, then $\int_E f d\mu = \int_E (f - f_N) d\mu + \int_E f_N d\mu \leq \int_X (f - f_N) d\mu + N\mu(E) < \epsilon$.
