---
role: proof
locale: en
of_concept: identities-for-first-return-probabilities
source_book: gtm040
source_chapter: "4"
source_section: "7. Classification of states"
---

**Proof:** The proofs are all by the strong Markov property (Theorem 4-10).

**(1)** Use induction on $k$. For $k = 0$ the result is trivial; assume that it holds for $k - 1$. Let $p$ be the statement that the process returns to $i$ at least $k$ times, and let $t = \bar{t}_i$ (the first return time to $i$). Then $p'$ is the statement that the process returns to $i$ at least $k - 1$ times.

By the strong Markov property,
$$\Pr_i[p] = \sum_j \Pr_i[x_t = j] \Pr_j[p'].$$

Since $x_t = i$ on returning to $i$, and the probability of returning to $i$ at least once is $\bar{H}_{ii}$, we obtain
$$\Pr_i[p] = \bar{H}_{ii} \cdot (\bar{H}_{ii})^{k-1} = (\bar{H}_{ii})^k$$
by the induction hypothesis.

**(2)** The argument is the same as in (1), using the stopping time $t = \bar{t}_i \land \bar{t}_j$ (the time of first return to $i$ or first hit of $j$). The probability of returning to $i$ before hitting $j$ is ${}_j\bar{H}_{ii}$, and each subsequent return before hitting $j$ is independent by the strong Markov property.

**(3)** Let $p$ be the event that the process returns to $i$ via $j$ (i.e., hits $j$ and then returns to $i$). Take the stopping time $t = \bar{t}_j$ (first hit time of $j$). Then by the strong Markov property,
$$\Pr_i[p] = \Pr_i[\text{hit } j \text{ before returning to } i] \cdot \Pr_j[\text{return to } i] = {}_i\bar{H}_{ij} \cdot H_{ji}.$$

**(4)** The argument is the same as in (3). Use the systems theorem with $t$ equal to the time of the $n$th return to $i$ if the return occurs before $j$ is reached, or $+\infty$ otherwise. The probability of $n$ returns to $i$ before hitting $j$ is $({}_j\bar{H}_{ii})^n$ by part (2), and conditioned on this event, the probability of then hitting $j$ for the first time is ${}_i\bar{H}_{ij}$.

**(5)** The proof is by induction on $n$ and is the same as in (1) except that the random time becomes $t = \bar{t}_j$ (the first return time to $j$). For $n = 1$, the probability of being in $j$ at least once is $H_{ij}$. Assuming the result for $n-1$, we use the strong Markov property at the first hit time of $j$ to obtain the factor $\bar{H}_{jj}$ for each additional visit.
