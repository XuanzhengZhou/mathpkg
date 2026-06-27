---
role: proof
locale: en
of_concept: cauchy-test-convergence-in-pth-mean
source_book: gtm095
source_chapter: "2"
source_section: "10"
---

# Proof of Cauchy Test for Convergence in the $p$-th Mean ($L^p$ Completeness)

**Theorem 7** (Cauchy Test for Convergence in the $p$th Mean). A necessary and sufficient condition that a sequence $(\xi_n)_{n \geq 1}$ of random variables in $L^p$ converges in the mean of order $p \geq 1$ to a random variable in $L^p$ is that the sequence is fundamental in the mean of order $p$.

*Proof.* The necessity follows from Minkowski's inequality:

$$\|\xi_n - \xi_m\|_p \leq \|\xi_n - \xi\|_p + \|\xi_m - \xi\|_p \to 0, \quad n, m \to \infty.$$

For sufficiency, let $(\xi_n)$ be fundamental ($\|\xi_n - \xi_m\|_p \to 0$, $n, m \to \infty$). As in the proof of Theorem 5, we select a subsequence $(\xi_{n_k})$ such that $\xi_{n_k} \xrightarrow{\text{a.s.}} \xi$, where $\xi$ is a random variable with $\|\xi\|_p < \infty$.

Take $n_1 = 1$ and define $n_k$ inductively as the smallest $n > n_{k-1}$ for which

$$\|\xi_t - \xi_s\|_p < 2^{-2k}$$

for all $s, t \geq n$. Then by Markov's inequality

$$P\{|\xi_{n_{k+1}} - \xi_{n_k}| > 2^{-k}\} \leq 2^{kp}\, E|\xi_{n_{k+1}} - \xi_{n_k}|^p < 2^{kp} \cdot 2^{-2kp} = 2^{-kp}.$$

Since $\sum_k 2^{-kp} < \infty$, the Borel--Cantelli lemma gives $P\{|\xi_{n_{k+1}} - \xi_{n_k}| > 2^{-k} \text{ i.o.}\} = 0$. Thus $(\xi_{n_k})$ converges almost surely to some limit $\xi$.

By Fatou's lemma, for any fixed $m$,

$$E|\xi - \xi_m|^p = E \liminf_{k \to \infty} |\xi_{n_k} - \xi_m|^p \leq \liminf_{k \to \infty} E|\xi_{n_k} - \xi_m|^p = \liminf_{k \to \infty} \|\xi_{n_k} - \xi_m\|_p^p.$$

Since the sequence is fundamental in $L^p$, the right-hand side can be made arbitrarily small by choosing $m$ large. Consequently $E|\xi_n - \xi|^p \to 0$, $n \to \infty$. It is also clear that since $\xi = (\xi - \xi_n) + \xi_n$ we have $E|\xi|^p < \infty$ by Minkowski's inequality.

This completes the proof of the theorem. $\square$
