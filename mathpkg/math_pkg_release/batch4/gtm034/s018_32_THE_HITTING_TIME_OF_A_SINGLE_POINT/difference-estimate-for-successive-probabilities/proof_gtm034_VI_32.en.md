---
role: proof
locale: en
of_concept: difference-estimate-for-successive-probabilities
source_book: gtm034
source_chapter: "VI"
source_section: "32"
---

Choose $m$ with $|U_{k+1} - U_k| \leq \frac{\epsilon_1}{4} U_k$ for $k \geq m$, and $A$ large enough that $P[|S_j| \geq A \text{ for some } j \leq M+1] \leq \frac{\epsilon_1}{4} \min_{m \leq k \leq M+1} U_k$.

Define $c_{k,j} = P[S_{k+j} = a, S_{k+r} \neq 0 \text{ for } r < j \mid S_k = a]$ and $d_{n-k,j} = P[T = n-k-j; S_p \neq a \text{ for } p \leq M-j \mid S_0 = a]$. Decomposing $q_n$ and $\tilde{q}_{n+1}$ according to the last revisit time $k+j$:

$$q_n = \sum_{|a| > A} P[S_k = a; T > k] \sum_{j=m}^{M} c_{k,j} d_{n-k,j},$$
$$\tilde{q}_{n+1} = \sum_{|a| > A} P[S_k = a; T > k] \sum_{j=m}^{M} c_{k,j+1} d_{n-k,j}.$$

The difference satisfies $|c_{k,j+1} - c_{k,j}| \leq \epsilon_1 c_{k,j}$ by the estimates on $U_n$. Hence
$$|q_n - \tilde{q}_{n+1}| \leq \epsilon_1 \sum_{|a|>A} P[S_k=a; T>k] \sum_{j=m}^{M} c_{k,j} d_{n-k,j} = \epsilon_1 q_n.$$
