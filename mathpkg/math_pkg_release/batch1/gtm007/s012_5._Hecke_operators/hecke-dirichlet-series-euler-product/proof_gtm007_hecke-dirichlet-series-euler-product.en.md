---
role: proof
locale: en
of_concept: hecke-dirichlet-series-euler-product
source_book: gtm007
source_chapter: "VII"
source_section: "5.4"
---
By formula (79), the function $n \mapsto c(n)$ is multiplicative. Therefore, by Lemma 4 of Chapter VII, \S 3.1, the Dirichlet series factors as an Euler product:
$$\Phi_f(s) = \sum_{n=1}^{\infty} \frac{c(n)}{n^s} = \prod_{p \in \mathcal{P}} \left( \sum_{n=0}^{\infty} \frac{c(p^n)}{p^{ns}} \right).$$
Setting $T = p^{-s}$, it suffices to prove the identity
$$\sum_{n=0}^{\infty} c(p^n)T^n = \frac{1}{1 - c(p)T + p^{2k-1}T^2}.$$
Multiplying both sides by $1 - c(p)T + p^{2k-1}T^2$, the constant term on the left is $c(1) = 1$. The coefficient of $T$ is $c(p) - c(p) = 0$. For $n \geq 1$, the coefficient of $T^{n+1}$ is
$$c(p^{n+1}) - c(p)c(p^n) + p^{2k-1}c(p^{n-1}),$$
which vanishes by the recurrence formula (80). Thus the product equals $1$, establishing the Euler product.
