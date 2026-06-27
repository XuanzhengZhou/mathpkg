---
role: proof
locale: en
of_concept: holder-inequality
source_book: gtm025
source_chapter: "4"
source_section: "13"
---

If $\|f\|_p = 0$ or $\|g\|_{p'} = 0$, the inequality is trivial. Otherwise, apply (13.3) with $a = |f(x)|/\|f\|_p$ and $b = |g(x)|/\|g\|_{p'}$ at each point $x$, then integrate: $\frac{|f(x)g(x)|}{\|f\|_p\|g\|_{p'}} \leq \frac{|f(x)|^p}{p\|f\|_p^p} + \frac{|g(x)|^{p'}}{p'\|g\|_{p'}^{p'}}$. Integrating over $X$ gives $\int |fg| d\mu / (\|f\|_p\|g\|_{p'}) \leq 1/p + 1/p' = 1$. Equality holds iff $A|f|^p = B|g|^{p'}$ a.e. for constants $A, B$ not both zero.
