---
role: proof
locale: en
of_concept: interval-green-function-recurrence-identity
source_book: gtm034
source_chapter: "V"
source_section: "23"
---

Let \(T_N\) be the exit time from \([0,N]\) and \(T\) the first time \(x_k < 0\). Since \(T_N \leq T\), the strong Markov property gives \(g_N(x,y) = E_x \sum_{k=0}^{T_N-1} \delta(y,x_k) = E_x \sum_{k=0}^{T-1} \delta(y,x_k) - E_x[E_{x_{T_N}} \sum_{k=0}^{T-1} \delta(y,x_k)] = g(x,y) - \sum_{k=1}^{\infty} R_N(x,k) g(N+k,y)\).
