---
role: proof
locale: en
of_concept: ladder-process-from-recurrent-chain
source_book: gtm040
source_chapter: "6"
source_section: "4"
---

Let $t_n(\omega)$ be the time of the $(n+1)$st visit to state $s$ along the path $\omega$. Define $t_0$ as the first time state $s$ is reached (with $t_0 = 0$ if the chain already starts at $s$ and we count that as the first visit).

The differences $y_n = t_n - t_{n-1}$ for $n \geq 1$ are the inter-arrival times between successive visits to $s$. By the strong Markov property (the Markov property applied at the stopping times $t_{n-1}$), the process regenerates at each visit to $s$: the future after $t_{n-1}$ is conditionally independent of the past given $x_{t_{n-1}} = s$, and has the same distribution as the process started at $s$. Consequently, the random variables $y_1, y_2, \ldots$ are independent and identically distributed.

Furthermore, $\Pr[y_n = k] = \Pr_s[ar{t}_s = k] = ar{F}_{ss}^{(k)}$, the first return probability to $s$ in exactly $k$ steps. The process $\{t_n\}$ defined by $t_0 = 0$ (or the first hitting time) and $t_n = t_{n-1} + y_n$ is then precisely a sums of independent random variables process with step distribution $\{p_k = ar{F}_{ss}^{(k)}\}$.

Define $P^*_{ij} = ar{F}_{ss}^{(j-i)}$ for $j > i$, and $P^*_{ij} = 0$ otherwise. Since $P$ is recurrent, $\sum_{k=1}^\infty ar{F}_{ss}^{(k)} = ar{H}_{ss} = 1$, so $P^*$ is a stochastic matrix representing the ladder process on the integers. By recurrence of $P$,
$$(P^*1)_k = \sum_j P^*_{kj} = \sum_j ar{F}_{ss}^{(j-k)} = ar{H}_{ss} = 1,$$
confirming $P^*$ is a sums of independent random variables Markov chain.
