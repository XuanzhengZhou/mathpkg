---
role: introduce
locale: en
content_hash: ""
written_against: ""
---

Corollary 12

A computation similar to the one in the proof of Theorem 12-16 shows that

$$\mu_A^A(\iota) = z^{-1} \exp \left\{ \sum_{B \in \overline{A}: B \cap A \neq \emptyset} V_B(\iota) \right\} = \mu_A^A(\iota')$$

whenever $i_t = i'_t$ for all $t \in \overline{A}$. The claim now follows from the straightforward generalization of Proposition 12-6 obtained by replacing $\{a\}$ with $A$.

Example 12-19: The Markov process case. Let $\{x_n; 0 \leq n \leq N\}$ be a denumerable Markov process viewed from time 0 to time $N$. Suppose that $\{x_n\}$ has starting distribution $\pi$ and one-step transition matrix $P_n$ at time $n$, where

$$P_{n,i_j} = \Pr[x_{n+1} = j \mid x_n = i].$$

If $\pi$ and all the $P_n$ are strictly positive, then $\{x_n\}$ is a Markov field with neighbor system $\partial$, where $\partial 0 = \{1\}$, $\partial N = \{N-1\}$, and $\partial n = \{n-1, n+1\}$ for $1 \leq n < N$. The local characteristics for $\{x_t\}$ are given by

$$\mu_0^T(\iota) = \pi(i_0) P_{0,i_0 i_1} / \sum_{i \in S} \pi(i) P_{0,i_1 i_1}$$

$$\mu_n^T(\iota) = \frac{P_{n-1,i_{n-1} i_n} P_{n,i_n i_{n+1}}}{\sum_{i \in S} P_{n-1,i_{n-1} i_n} P_{n,i_{n+1}}} \quad 1 \leq n < N,$$

$$\mu_N^T(\iota) = P_{N-1,i_{N-1} i_N}$$
