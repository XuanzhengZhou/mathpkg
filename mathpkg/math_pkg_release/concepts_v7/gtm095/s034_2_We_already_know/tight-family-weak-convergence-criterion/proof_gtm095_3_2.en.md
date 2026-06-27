---
role: proof
locale: en
of_concept: tight-family-weak-convergence-criterion
source_book: gtm095
source_chapter: "3"
source_section: "2"
---

# Proof of Tight Family Weak Convergence Criterion

Let $\{P_n\}$ be a tight family of probability measures on $(\mathbb{R}, \mathcal{B}(\mathbb{R}))$. Suppose that every weakly convergent subsequence of $\{P_n\}$ converges to the same probability measure $P$.

We prove that $P_n \xrightarrow{w} P$ by contradiction.

**Proof.** Suppose that $P_n \not\xrightarrow{w} P$. Then there exists a bounded continuous function $f$ on $\mathbb{R}$, a number $\varepsilon > 0$, and a subsequence $\{n_k\}$ such that

$$\left| \int_{\mathbb{R}} f(x) \, P_{n_k}(dx) - \int_{\mathbb{R}} f(x) \, P(dx) \right| \geq \varepsilon \tag{1}$$

for all $k$.

Since $\{P_n\}$ is a tight family, the subsequence $\{P_{n_k}\}$ is also tight. By Prohorov's theorem, there exists a further subsequence $\{P_{n_{k'}}\}$ of $\{P_{n_k}\}$ and a probability measure $Q$ such that

$$P_{n_{k'}} \xrightarrow{w} Q.$$

By hypothesis, every weakly convergent subsequence of $\{P_n\}$ converges to the same probability measure $P$. Hence $Q = P$, and therefore

$$P_{n_{k'}} \xrightarrow{w} P.$$

By the definition of weak convergence, this implies

$$\int_{\mathbb{R}} f(x) \, P_{n_{k'}}(dx) \to \int_{\mathbb{R}} f(x) \, P(dx),$$

which contradicts inequality (1). $\square$

Thus the whole sequence $\{P_n\}$ converges weakly to $P$.
