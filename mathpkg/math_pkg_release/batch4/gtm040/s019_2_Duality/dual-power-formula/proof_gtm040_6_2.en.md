---
role: proof
locale: en
of_concept: dual-power-formula
source_book: gtm040
source_chapter: "6"
source_section: "2. Duality"
---

The proof of the first assertion is by induction on $n$. The case $n = 1$ is Definition 6-10. Suppose that

$$\hat{P}^{k-1} = D(P^{k-1})^T D^{-1}.$$

Then

$$\hat{P}^k = \hat{P}\hat{P}^{k-1} = (DP^T D^{-1})(D(P^{k-1})^T D^{-1}) = D(P^k)^T D^{-1}.$$

Associativity holds because all the matrices are non-negative. Now

$$\{M_i[\hat{n}_j]\} = \sum_k \hat{P}^k = D \sum_k ((P^k)^T)D^{-1} = D\{M_i[n_j]\}^T D^{-1}.$$

In particular, if $M_j[n_j]$ is infinite, then so is $M_j[\hat{n}_j]$. Hence, by Proposition 6-11, if $P$ is recurrent, so is $\hat{P}$. For the transient case with only transient states, the fundamental matrix is $\hat{N} = \sum_{n=0}^\infty \hat{P}^n = D(\sum_{n=0}^\infty P^n)^T D^{-1} = DN^T D^{-1}$.
