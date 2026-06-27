---
role: proof
locale: en
of_concept: infinite-recurrence-in-recurrent-class
source_book: gtm040
source_chapter: "4"
source_section: "7. Classification of states"
---

**Proof:** Suppose the chain is started in state $i \in S'$. For any state $j \in S'$, since $i$ and $j$ are in the same recurrent class, we have $H_{ij} = 1$ and $\bar{H}_{jj} = 1$ by Lemma 4-23 and Proposition 4-24.

By conclusion (5) of Lemma 4-19, the probability of being in state $j$ at least $n$ times is
$$H_{ij}(\bar{H}_{jj})^{n-1} = 1 \cdot 1^{n-1} = 1$$
for every $n$.

By Proposition 2-6, since the event of being in state $j$ at least $n$ times has probability 1 for each $n$, the chain is in state $j$ infinitely often with probability one. This holds for every $j \in S'$, so by Proposition 2-6 again, the chain is in every state of $S'$ infinitely often with probability one.

Consequently, $N_{ij} = \sum_{n=0}^{\infty} (P^n)_{ij} = +\infty$ for all $i, j \in S'$.
