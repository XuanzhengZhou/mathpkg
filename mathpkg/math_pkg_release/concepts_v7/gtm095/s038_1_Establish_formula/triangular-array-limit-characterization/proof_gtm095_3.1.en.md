---
role: proof
locale: en
of_concept: triangular-array-limit-characterization
source_book: gtm095
source_chapter: "3"
source_section: "1"
---

# Proof of Limit of Triangular Array Sums is Infinitely Divisible

**Proof.** If $T$ is infinitely divisible, for each $n \geq 1$ there are independent identically distributed random variables $\xi_{n,1}, \ldots, \xi_{n,n}$ such that $T \stackrel{d}{=} \xi_{n,1} + \cdots + \xi_{n,n}$, and this means that $T \stackrel{d}{=} T_n$, $n \geq 1$. Hence $T_n \xrightarrow{d} T$ trivially, and $T$ can be obtained as the limit in distribution of sums $T_n = \sum_{k=1}^n \xi_{n,k}$.

Conversely, let $T_n \xrightarrow{d} T$. Let us show that $T$ is infinitely divisible, i.e., for each $k$ there are independent identically distributed random variables $\eta_1, \ldots, \eta_k$ such that $T \stackrel{d}{=} \eta_1 + \cdots + \eta_k$.

Choose a $k \geq 1$ and represent $T_{nk} = \sum_{i=1}^{nk} \xi_{nk,i}$ in the form $\zeta_n^{(1)} + \cdots + \zeta_n^{(k)}$, where

$$\zeta_n^{(1)} = \xi_{nk,1} + \cdots + \xi_{nk,n}, \quad \ldots, \quad \zeta_n^{(k)} = \xi_{nk,n(k-1)+1} + \cdots + \xi_{nk,nk}.$$

Since $T_{nk} \xrightarrow{d} T$, $n \to \infty$, the sequence of distribution functions corresponding to the random variables $T_{nk}$ is tight. Consequently, the joint distributions of the vectors $(\zeta_n^{(1)}, \ldots, \zeta_n^{(k)})$ are also tight. By the Helly selection principle (or Prokhorov's theorem), there exists a subsequence $\{n_j\}$ and a random vector $(\eta_1, \ldots, \eta_k)$ such that

$$(\zeta_{n_j}^{(1)}, \ldots, \zeta_{n_j}^{(k)}) \xrightarrow{d} (\eta_1, \ldots, \eta_k),$$

and by Theorem 4 of Sect. 12, Chap. 2, $\eta_1, \ldots, \eta_k$ are independent. Clearly, they are identically distributed.

Thus we have

$$T_{n_j k} = \zeta_{n_j}^{(1)} + \cdots + \zeta_{n_j}^{(k)} \xrightarrow{d} \eta_1 + \cdots + \eta_k$$

and moreover $T_{n_j k} \xrightarrow{d} T$. Consequently (Problem 1)

$$T \stackrel{d}{=} \eta_1 + \cdots + \eta_k.$$

This completes the proof of the theorem. $\square$

**Remark 2.** The conclusion of the theorem remains valid if we replace the hypothesis that $\xi_{n,1}, \ldots, \xi_{n,n}$ are identically distributed for each $n \geq 1$ by the condition of their asymptotic negligibility $\max_{1 \leq k \leq n} P\{|\xi_{nk}| \geq \varepsilon\} \to 0$.
