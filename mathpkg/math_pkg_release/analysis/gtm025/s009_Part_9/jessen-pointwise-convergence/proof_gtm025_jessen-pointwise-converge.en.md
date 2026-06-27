---
role: proof
locale: en
of_concept: jessen-pointwise-convergence
source_book: gtm025
source_chapter: "22"
source_section: "SS 22"
---

Consider the decreasing $\sigma$-algebras $\mathcal{M}^{(n)} = \mathcal{M}_{\Omega_n'}$. For any $A \in \mathcal{M}^{(n)}$, writing $A = A_{\Omega_n} \times T_{\Omega_n}$ and using Fubini, $\int_A f_n d\mu = \int_A f d\mu$. Thus $f_n$ is the conditional expectation of $f$ given $\mathcal{M}^{(n)}$, forming a reversed martingale. By the martingale convergence theorem (20.56), $\lim f_n$ exists a.e. and equals the conditional expectation with respect to the tail $\sigma$-algebra. Since the algebra $\mathcal{N}$ generates $\mathcal{M}$, the limit is $f$ $\mu$-a.e.
