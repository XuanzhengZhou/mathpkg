---
role: proof
locale: en
of_concept: zero-integral-iff-zero-a.e.
source_book: gtm018
source_chapter: "V"
source_section: "25"
---
**Proof.** If $f = 0$ a.e., the identically zero sequence is a mean fundamental sequence of simple functions converging in measure to $f$, giving $\int f d\mu = 0$. Conversely, assume $\int f d\mu = 0$ and take a mean fundamental sequence $\{f_n\}$ of non negative simple functions converging in measure to $f$. Then $\lim_n \int f_n d\mu = 0$, so $\{f_n\}$ mean converges to $0$. By Theorem A, $\{f_n\}$ converges to $0$ in measure, so $f = 0$ a.e. by uniqueness of limits in measure (22.C).
