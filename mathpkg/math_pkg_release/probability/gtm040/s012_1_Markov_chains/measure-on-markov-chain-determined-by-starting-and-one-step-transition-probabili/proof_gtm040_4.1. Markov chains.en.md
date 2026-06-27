---
role: proof
locale: en
of_concept: measure-on-markov-chain-determined-by-starting-and-one-step-transition-probabili
source_book: gtm040
source_chapter: "4"
source_section: "1. Markov chains"
---

By Proposition 2-8, the measure is determined by starting probabilities $\Pr[x_0 = c_0]$ and transition probabilities $\Pr[x_n = c_n \mid x_0 = c_0 \wedge \cdots \wedge x_{n-1} = c_{n-1}]$. For a Markov chain, the Markov property reduces each transition probability to $\Pr[x_n = c_n \mid x_{n-1} = c_{n-1}]$, and time-homogeneity ensures this value is independent of $n$, depending only on the states involved.
