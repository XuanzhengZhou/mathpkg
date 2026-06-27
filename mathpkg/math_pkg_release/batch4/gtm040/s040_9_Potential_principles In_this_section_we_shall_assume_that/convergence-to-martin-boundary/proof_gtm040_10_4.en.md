---
role: proof
locale: en
of_concept: convergence-to-martin-boundary
source_book: gtm040
source_chapter: "10"
source_section: "4"
---

Form the extended chain associated with $\pi$ and $P$. Let $\{\hat{x}_n\}$ be the reverse of this extended chain. Since $K(i, j) = \hat{N}_{ji} / N_{\pi i}$, it suffices to show that in the reverse process $\hat{N}_{\hat{x}_n, i}$ converges for all $i$. 

The function $\hat{N}_{\cdot, i}$ is superregular for the reverse chain. By a downcrossing argument (as in the proof of the martingale convergence theorem), $\hat{N}_{\hat{x}_n, i}$ converges almost surely along the path. Since this holds for all $i$, $K(i, x_n)$ converges for all $i$, which means $x_n$ converges in $S^*$ by Proposition 10-13.
