---
role: proof
locale: en
of_concept: complex-measure-radon-nikodym
source_book: gtm025
source_chapter: ""
source_section: "19"
---

Let $\nu = \sum_{k=1}^4 \alpha_k \nu_k$ be the Jordan decomposition. Each $\nu_k \ll \mu$, so by 19.24 there exist $f_k$ with $\int f d\nu_k = \int f f_k d\mu$. Set $f_0 = \sum \alpha_k f_k$. Then for $f \in \mathfrak{L}_1(|\nu|)$, $\int f d\nu = \sum \alpha_k \int f d\nu_k = \sum \alpha_k \int f f_k d\mu = \int f f_0 d\mu$. For (iii), approximate $|f_0|$ by simple functions bounded by 1 and use the definition of $|\nu|$. Equality (iv) follows from (iii) with $A = X$.
