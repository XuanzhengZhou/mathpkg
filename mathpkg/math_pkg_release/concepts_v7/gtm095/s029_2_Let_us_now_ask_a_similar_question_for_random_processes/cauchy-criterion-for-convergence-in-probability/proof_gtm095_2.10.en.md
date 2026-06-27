---
role: proof
locale: en
of_concept: cauchy-criterion-for-convergence-in-probability
source_book: gtm095
source_chapter: "2"
source_section: "10"
---

# Proof of Cauchy Criterion for Convergence in Probability

**Theorem 6.** A necessary and sufficient condition for a sequence $(\xi_n)_{n \geq 1}$ of random variables to converge in probability is that it is fundamental in probability.

*Proof.* If $\xi_n \xrightarrow{P} \xi$ then

$$P\{|\xi_n - \xi_m| \geq \varepsilon\} \leq P\{|\xi_n - \xi| \geq \varepsilon/2\} + P\{|\xi_m - \xi| \geq \varepsilon/2\}$$

and consequently $(\xi_n)$ is fundamental in probability.

Conversely, if $(\xi_n)$ is fundamental in probability, by Theorem 5 there are a subsequence $(\xi_{n_k})$ and a random variable $\xi$ such that $\xi_{n_k} \xrightarrow{\text{a.s.}} \xi$. But then

$$P\{|\xi_n - \xi| \geq \varepsilon\} \leq P\{|\xi_n - \xi_{n_k}| \geq \varepsilon/2\} + P\{|\xi_{n_k} - \xi| \geq \varepsilon/2\},$$

from which it is clear that $\xi_n \xrightarrow{P} \xi$. Taking $n$ and $k$ both large enough makes both terms arbitrarily small. This completes the proof. $\square$
