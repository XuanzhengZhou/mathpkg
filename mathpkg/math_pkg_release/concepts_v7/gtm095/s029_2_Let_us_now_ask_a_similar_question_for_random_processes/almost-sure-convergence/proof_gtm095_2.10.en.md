---
role: proof
locale: en
of_concept: almost-sure-convergence
source_book: gtm095
source_chapter: "2"
source_section: "10"
---

# Proof of Theorem 5: Fundamental in Probability Implies Almost Surely Convergent Subsequence

**Theorem 5.** If the sequence $(\xi_n)$ is fundamental (or convergent) in probability, it contains a subsequence $(\xi_{n_k})$ that is fundamental (or convergent) with probability 1.

*Proof.* Let $(\xi_n)$ be fundamental in probability. By Theorem 4 it is enough to show that it contains a subsequence that converges almost surely.

Take $n_1 = 1$ and define $n_k$ inductively as the smallest $n > n_{k-1}$ for which

$$P\{|\xi_t - \xi_s| > 2^{-k}\} < 2^{-k}$$

for all $s \geq n$, $t \geq n$. Such $n_k$ exist because $(\xi_n)$ is fundamental in probability (for any $\delta > 0$ there exists $N$ such that $P\{|\xi_t - \xi_s| > \delta\} < \delta$ for all $s, t \geq N$). Then

$$\sum_{k} P\{|\xi_{n_{k+1}} - \xi_{n_k}| > 2^{-k}\} < \sum_{k} 2^{-k} < \infty$$

and by the Borel--Cantelli lemma

$$P\{|\xi_{n_{k+1}} - \xi_{n_k}| > 2^{-k} \text{ i.o.}\} = 0.$$

Hence for almost all $\omega$, there exists $K = K(\omega)$ such that $|\xi_{n_{k+1}}(\omega) - \xi_{n_k}(\omega)| \leq 2^{-k}$ for all $k \geq K$. Consequently, the series

$$\sum_{k=1}^{\infty} (\xi_{n_{k+1}} - \xi_{n_k})$$

converges absolutely for almost all $\omega$, which means that the subsequence $(\xi_{n_k})$ converges with probability 1. $\square$
