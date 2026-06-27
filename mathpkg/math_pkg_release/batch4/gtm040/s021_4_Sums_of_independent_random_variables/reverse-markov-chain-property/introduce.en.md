---
role: introduce
locale: en
content_hash: ""
written_against: ""
---

Proposition 6-44 addresses the time-reversal of a Markov process over a finite time horizon. Given a denumerable Markov process $\{x_n\}$ observed up to time $N$, the reversed process $y_n = x_{N-n}$ (for $0 \leq n \leq N$) is again a Markov process, though not necessarily a time-homogeneous Markov chain. The proof uses the Markov property to factor the joint probability and shows that the conditional probability $\Pr[y_n = c_n \mid y_0, \ldots, y_{n-1}]$ depends only on $y_{n-1}$. For ergodic chains, a related positive result holds: the reversed transition probabilities have a limit.
