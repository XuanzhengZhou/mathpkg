---
role: proof
locale: en
of_concept: conditional-probability-bound-small-displacement
source_book: gtm034
source_chapter: "VII"
source_section: "32"
---

Define $J_k(A,n) = 1$ if $|S_k| \leq A$ and $T=n$, 0 otherwise; $L_k(m,M,n) = 1$ if $S_{k+j} \neq S_k$ for $m \leq j \leq M$, 0 otherwise. The sum is bounded by $E[\sum J_k \mid T=n] + E[\sum L_k \mid T=n]$. Choose $\eta = \epsilon/2$, pick $M$ so large that $P[S_{k+j} \neq S_k \text{ for } m \leq j \leq M] \leq \eta$. The $L_k$ term $\leq 2n\eta + \frac{Mn}{F_n}c_1 e^{-c_2(n/M)}$ using exponential tail bounds for Bernoulli sums (P5.3). For $J_k$, let $\phi_k = 1$ if $|S_k| \leq A$. Truncation gives $\leq n\eta + \frac{n}{F_n}P[T \geq n \mid \sum \phi_k \geq n\eta]$. Choose $\chi > 0$, $r > 0$ with $\min_{|a| \leq A} P[S_k = a \text{ for some } k < r] \geq \chi$. Then $P[T \geq j+r \mid |S_j| \leq A] \leq 1-\chi$, yielding exponential decay. Both exponential terms decay faster than $F_n$ by P5, proving the result.
