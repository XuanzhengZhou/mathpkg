---
role: introduce
locale: en
content_hash: ""
written_against: ""
---

A Choquet capacity is a non-negative monotone increasing set function such that, for any sets $A_1, A_2, \ldots, A_n$,

$$C(A_1 \cap A_2 \cap \cdots \cap A_n) \leq \sum_i C(A_i) - \sum_{i \neq j} C(A_i \cup A_j)$$

$$+ \sum_{i \neq j \neq k} C(A_i \cup A_j \cup A_k)$$

$$- \cdots - (-1)^n C(A_1 \cup \cdots \

of entering all sets, though in general not the only way. Hence Choquet’s definition is satisfied. Since we may clearly also replace $C(E)$ by $kC(E)$ with $k > 0$, $\pi$ may be any non-negative finite measure.

We shall show from this construction that our Definition 8-31 yields a Choquet capacity on equilibrium sets. For convenience, we will give a proof for $\hat{P}$. For any fixed equilibrium set $F$ of $\hat{P}$, Proposition 8-36 tells us that the capacity of any subset $E$ is $\hat{\eta}^F h^E$. Hence the above argument applies with $\pi = \hat{\eta}^F$. Thus the Choquet conditions hold for all subsets of $F$ and, since $F$ is any equilibrium set, they hold for all equilibrium sets.

A more general method of obtaining a Choquet capacity within our framework is as follows. Let $\pi$ be a measure, and let $h$ be a strictly positive superregular function such that $\pi h < \infty$. Define $C(E) = \pi B^E h$. Forming the $h$-process, we see that $C(E) = \pi^*(B^E)*1 = \pi^*(h^E)*$ with $\pi^*1 = \pi h < \infty$. Thus by the special case $C(E)$ is a Choquet capacity for the $h$-process and hence satisfies the same axioms in the original chain. Moreover, we see that the situation in the earlier case is just the present case with $h = 1$. On the other hand, this more general method includes a second interesting case: If $g$ is a pure potential for which $\pi g$ is finite, then by Lemma 8-17,

$$\pi B^E g = \pi g - \pi^E Nf;$$

$\pi B^E g$ is a Choquet capacity which assumes its maximum value $\pi g$ on all sets $E$ containing the support of $f$. If $\pi 1 = 1$, then $\pi B^E g$ in the game interpretation is the expected gain when and after $E$ is reached.
