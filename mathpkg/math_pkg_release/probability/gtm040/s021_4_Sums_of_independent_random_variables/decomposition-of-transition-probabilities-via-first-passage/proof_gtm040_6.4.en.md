---
role: proof
locale: en
of_concept: decomposition-of-transition-probabilities-via-first-passage
source_book: gtm040
source_chapter: "6"
source_section: "4"
---

The first two statements ($P_{ij}^{(0)} = \delta_{ij}$ and $\bar{F}_{ij}^{(0)} = 0$) are obvious from the definitions. For the third identity, we first note that if $\Pr_i[\bar{t}_j = k] > 0$, then for $n \geq k$,

$$\Pr_i[x_n = j \mid \bar{t}_j = k] = \Pr_i[x_n = j \mid x_k = j \land x_{k-1} \neq j \land \cdots \land x_1 \neq j].$$

By Lemma 4-6 (the Markov property applied to the stopping time $\bar{t}_j$), this simplifies to

$$\Pr_i[x_n = j \mid x_k = j] = \Pr_j[x_{n-k} = j] = P_{jj}^{(n-k)}.$$

Hence, regardless of the value of $\Pr_i[\bar{t}_j = k]$, for $n \geq k$ we have

$$\Pr_i[\bar{t}_j = k] \cdot \Pr_i[x_n = j \mid \bar{t}_j = k] = \bar{F}_{ij}^{(k)} P_{jj}^{(n-k)}.$$

Now, the event $x_n = j$ can be partitioned according to the time $k$ of the first visit to $j$ (where $1 \leq k \leq n$):

$$P_{ij}^{(n)} = \Pr_i[x_n = j] = \sum_{k=1}^{n} \Pr_i[\bar{t}_j = k] \cdot \Pr_i[x_n = j \mid \bar{t}_j = k] = \sum_{k=1}^{n} \bar{F}_{ij}^{(k)} P_{jj}^{(n-k)}.$$

This establishes the first equality. The second equality follows by the change of index $m = n-k$:

$$\sum_{k=1}^{n} \bar{F}_{ij}^{(k)} P_{jj}^{(n-k)} = \sum_{m=0}^{n-1} \bar{F}_{ij}^{(n-m)} P_{jj}^{(m)} = \sum_{k=0}^{n-1} P_{jj}^{(k)} \bar{F}_{ij}^{(n-k)}.$$
