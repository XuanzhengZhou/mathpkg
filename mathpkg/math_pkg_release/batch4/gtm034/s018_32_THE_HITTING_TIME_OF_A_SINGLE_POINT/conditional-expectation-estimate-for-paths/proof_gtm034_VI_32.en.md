---
role: proof
locale: en
of_concept: conditional-expectation-estimate-for-paths
source_book: gtm034
source_chapter: "VI"
source_section: "32"
---

Define $J_k(A,n) = 1$ if $|S_k| \leq A$ and $T=n$, $L_k(m,M,n) = 1$ if $S_{k+j} \neq S_k$ for $m \leq j \leq M$. The sum is bounded by $E[\sum J_k \mid T=n] + E[\sum L_k \mid T=n]$.

Given $\eta = \epsilon/2$, pick $M$ with $P[S_j \neq 0 \text{ for } m \leq j \leq M] \leq \eta$ (possible by recurrence). Truncating,
$$E[\sum L_k \mid T=n] \leq 2n\eta + \frac{n}{F_n} P[\sum L_k \geq 2n\eta].$$

The $L_k$ depend on disjoint blocks of $M$ increments. By P5.3 (exponential bound for Bernoulli sums),
$$P[\sum L_k \geq 2n\eta] \leq c_1 e^{-c_2 n/M}.$$

Thus $E[\sum L_k \mid T=n] \leq 2n\eta + \frac{Mn}{F_n} c_1 e^{-c_2 n/M}$. For the $J_k$ term, a similar truncation gives an exponential bound. Setting $\eta = \epsilon/2$ and using P5 to dominate $1/F_n$ completes the proof.
