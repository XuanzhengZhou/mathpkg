---
role: proof
locale: en
of_concept: interval-subadditivity-open-cover
source_book: gtm018
source_chapter: "II"
source_section: "8"
---

Let $k_1$ be such that $a_0 \in U_{k_1}$. If $b_{k_1} \leq b_0$, then let $k_2$ be such that $b_{k_1} \in U_{k_2}$; if $b_{k_2} \leq b_0$, then let $k_3$ be such that $b_{k_2} \in U_{k_3}$, and so on by induction. The process stops with $k_m$ if $b_{k_m} > b_0$. There is no loss of generality in assuming that $m = n$ and $U_{k_i} = U_i$ for $i = 1, \cdots, n$, because this state of affairs may be achieved merely by omitting superfluous $U_i$'s and changing the notation. In other words we may (and do) assume that

$$a_1 < a_0 < b_1, \quad a_n < b_0 < b_n,$$

and, in case $n > 1$,

$$a_{i+1} < b_i < b_{i+1} \quad \text{for} \quad i = 1, \cdots, n-1;$$

it follows that

$$b_0 - a_0 < b_n - a_1 = (b_1 - a_1) + \sum_{1 \leq i \leq n-1} (b_{i+1} - b_i) \leq \sum_{i=1}^{n} (b_i - a_i).$$
