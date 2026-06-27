---
role: proof
locale: en
of_concept: lebesgue-radon-nikodym-sigma-finite
source_book: gtm025
source_chapter: ""
source_section: "19"
---

Decompose $X$ into a countable disjoint family $\{E_n\}$ with $\mu(E_n), \nu(E_n) < \infty$. For each $n$, restrict to $E_n$ and apply 19.23 to obtain $f_n$. Define $f_0 = \sum f_n \xi_{E_n}$. Then $\nu(A) = \sum \nu(A \cap E_n) = \sum \int_{A \cap E_n} f_n d\mu = \int_A f_0 d\mu$.
