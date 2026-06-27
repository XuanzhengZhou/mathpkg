---
role: proof
locale: en
of_concept: narrow-band-pass-filtering-theorem
source_book: gtm017
source_chapter: "IX"
source_section: "d"
---
The time interval $[0,T]$ is divided into alternating large blocks of length $p(T)$ and small blocks of length $q(T)$ where $q/p \to 0$. The contribution from small blocks is negligible in probability. The large block integrals $U_j$ are approximately independent due to uniform mixing: for any $\delta > 0$,
$$|P(\bigcap A_j) - \prod P(A_j)| \leq k g(q(T)).$$

With appropriate choice of $p, q, k, \delta$ satisfying $k\delta \to 0$ and $k(2\tau_k/\delta)^k g(q) \to 0$, the sum of $U_j$ has the same limiting distribution as independent random variables with the same marginals. Lyapunovs condition is verified using the fourth moment condition, so asymptotic normality follows with variance $2\pi \int f(\lambda) dM(\lambda)$.
