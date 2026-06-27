---
role: proof
locale: en
of_concept: thm-the-following-four-statements-are-equivalent
source_book: gtm034
source_chapter: "3"
source_section: "008"
---

Proof: Setting $z = 1$ in the first two statements of P5, one has

$$1 - \mathbf{E}[t^{\mathbf{T}}] = e^{-\sum_{k=1}^{\infty} \frac{i k}{k} P[S_k > 0]},$$

$$1 - \mathbf{E}[t^{\mathbf{T}'}] = e^{-\sum_{k=1}^{\infty} \frac{i k}{k} P[S_k \geq 0]}.$$

This shows that (a) is equivalent to (c) and (b) to (d). But (c) and (d) will be equivalent if we can show that the series $\sum k^{-1} \mathbf{P}[S_k = 0]$ converges. This follows from the estimate in P7.6 in Chapter II, but we also offer the following direct proof. From (b) in P5, setting $z = 0,$

$$1 - \mathbf{E}[t^{\mathbf{T}'}; S_{\mathbf{T}'} = 0] = e^{-\sum_{k=1}^{\infty} \frac{i k}{k} P[S_k = 0]}.$$

If the series $\sum k^{-1} \mathbf{P}[S_k = 0]$ were divergent, we could conclude that

$$\mathbf{P}[T' < \infty; S_{\mathbf{T}'} = 0] = 1,$$

but this implies that $\mathbf{P}[X_k > 0] = \sum_{k=1}^{\infty} P(0,x) = 0$. By applying the same argument to the reversed random walk it follows that also $\mathbf{P}[X_k < 0] = 0$ so that $P(0,0) = 1$. But this is a degenerate case which we have excluded so that $\sum_{k=1}^{\infty} k^{-1} \mathbf{P}[S_k = 0]$ converges and (a) through (d) are equivalent.

For the last part of the theorem we use results from Chapter I. If $\mu > 0$, then $\lim_{n \to \infty} n^{-1} S_n = \mu > 0$ with probability one (this is P3.4), so that $T < \infty$. When

In the event that $\mu \geq 0$, it follows from T17.1 of the last section that the hitting time $T$ of the right half-line $[1, \infty)$ is a random variable, in other words, that $T < \infty$ with probability one. In this case the expectation of $T$ and also of $S_T$ is of interest—in fact of far greater interest for the theory in the next three chapters than one might guess at this point. We begin with
