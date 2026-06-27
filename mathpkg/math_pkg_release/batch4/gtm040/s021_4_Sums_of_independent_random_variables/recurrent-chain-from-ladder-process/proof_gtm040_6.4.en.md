---
role: proof
locale: en
of_concept: recurrent-chain-from-ladder-process
source_book: gtm040
source_chapter: "6"
source_section: "4"
---

Let $p'_k = P'_{0k}$ for $k \geq 1$. Since $P'$ is a stochastic matrix (ladder process), we have $\sum_{k=1}^{\infty} p'_k = 1$ (the walk always moves forward from 0).

We construct $P$ to be a basic example (birth-and-death chain on the non-negative integers) with state $s = 0$. The transition probabilities of the basic example are:
$$P_{i,i+1} = p_i, \quad P_{i,i-1} = q_i, \quad P_{00} = q_0,$$
with $p_i + q_i = 1$ for all $i$. Define $eta_0 = 1$ and $eta_n = p_0 p_1 \cdots p_{n-1}$ for $n \geq 1$. In the basic example, the first return probability to state 0 in exactly $n$ steps is
$$ar{F}_{00}^{(n)} = eta_{n-1} q_n = eta_{n-1} - eta_n.$$

We need to choose $\{p_i, q_i\}$ so that $ar{F}_{00}^{(n)} = p'_n$ for all $n$. Define the $q_i$ recursively by:
$$p'_1 = q_1 = eta_0 - eta_1,$$
$$p'_n = p_0 p_1 \cdots p_{n-1} q_n = eta_{n-1} q_n = eta_{n-1} - eta_n \quad 	ext{for } n \geq 2.$$

Summing these relations:
$$\sum_{k=1}^n p'_k = \sum_{k=1}^n (eta_{k-1} - eta_k) = eta_0 - eta_n = 1 - eta_n.$$

Since $\sum_{k=1}^\infty p'_k = 1$, we obtain $\lim_n eta_n = 0$. But $\lim_n eta_n = 0$ is precisely the recurrence condition for the basic example (Proposition 5-8 or the earlier characterization). Hence $P$ is recurrent.

In this constructed chain $P$, we have $\Pr[t_1 - t_0 = k] = ar{F}_{00}^{(k)} = p'_k$ as required, so the return times to state 0 are the outcome functions for $P'$.
