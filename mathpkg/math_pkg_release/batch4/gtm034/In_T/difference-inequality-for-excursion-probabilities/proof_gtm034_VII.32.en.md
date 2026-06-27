---
role: proof
locale: en
of_concept: difference-inequality-for-excursion-probabilities
source_book: gtm034
source_chapter: "VII"
source_section: "32"
---

Choose $m$ so that $|U_{k+1} - U_k| \leq \frac{\epsilon_1}{4} U_k$ for $k \geq m$, and $A$ so large that $P[|S_j| \geq A \text{ for some } j \leq M+1] \leq \frac{\epsilon_1}{4} \min_{m \leq k \leq M+1} U_k$. Decompose $q_n = \sum_{|a| > A} P[S_k = a; T > k] \sum_{j=m}^{M} c_{k,j} d_{n-k,j}$ where $c_{k,j} = P[S_{k+j}=a, S_{k+r} \neq 0 \text{ for } r < j \mid S_k=a]$ and $d_{n-k,j}$ involves $P[T = n-k-j]$. Similarly for $\tilde{q}_{n+1}$ with $c_{k,j+1}$. Then $|q_n - \tilde{q}_{n+1}| \leq \sum_{|a| > A} P[S_k=a; T > k] \sum_{j=m}^{M} |c_{k,j} - c_{k,j+1}| d_{n-k,j}$. Bounding $|c_{k,j+1} - c_{k,j}| \leq \epsilon_1 c_{k,j}$ (via the choices of $m$ and $A$) yields $|q_n - \tilde{q}_{n+1}| \leq \epsilon_1 q_n$.
