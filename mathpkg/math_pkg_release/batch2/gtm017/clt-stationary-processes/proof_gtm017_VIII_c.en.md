---
role: proof
locale: en
of_concept: clt-stationary-processes
source_book: gtm017
source_chapter: "VIII"
source_section: "c"
---
Define $u_r = E(Y_r|\mathcal{B}_0) - E(Y_r|\mathcal{B}_{-1})$. The summability condition ensures $X_0 = \sum_{r=0}^\infty u_r$ is well-defined in $L^2$. Set $X_r = \tau^r X_0$. Then $(X_r)$ is a stationary martingale difference sequence.

Compute $\sigma^2 = EX_0^2 = EY_0^2 + 2\sum_{k=1}^\infty E(Y_k Y_0)$. Let $T_n = \sum_{j=1}^n X_j$, $S_n = \sum_{j=1}^n Y_j$. One shows $n^{-1}E(S_n T_n) \to \sigma^2$ and $E|S_n - T_n|^2/n \to 0$. By the martingale CLT, $T_n/\sqrt{n}\sigma$ is asymptotically $N(0,1)$, hence so is $S_n/\sqrt{n}\sigma$.
