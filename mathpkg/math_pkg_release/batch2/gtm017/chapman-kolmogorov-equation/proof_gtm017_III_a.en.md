---
role: proof
locale: en
of_concept: chapman-kolmogorov-equation
source_book: gtm017
source_chapter: "III"
source_section: "a"
---
For $r < s < t$, by definition of higher-order transition probabilities:
$$p_{i_m, i_{m+r}}^{(m, m+r)} = \sum_{i_{m+1}} p_{i_m, i_{m+1}}^{(m, m+1)} \cdots p_{i_{m+r-1}, i_{m+r}}^{(m+r-1, m+r)}.$$

Splitting the product at time $s$ and summing over intermediate states gives:
$$P^{(r,s)} P^{(s,t)} = P^{(r,t)}.$$

For stationary transition mechanism: $P^{(r,s)} = P^{s-r}$, so $P^{s-r} P^{t-s} = P^{t-r}$, i.e., $P^a P^b = P^{a+b}$.
