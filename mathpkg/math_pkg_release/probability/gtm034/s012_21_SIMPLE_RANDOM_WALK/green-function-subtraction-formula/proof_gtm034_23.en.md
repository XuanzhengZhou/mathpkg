---
role: proof
locale: en
of_concept: green-function-subtraction-formula
source_book: gtm034
source_chapter: "V"
source_section: "23"
---

Let $x_n$ be the random walk with $x_0 = x$, let $T_N$ be the first exit time from $[0,N]$, and let $T$ be the first time that $x_k < 0$. Clearly $T_N \leq T$. Then
$$g_N(x,y) = E_x \sum_{k=0}^{T_N-1} \delta(y, x_k) = E_x \sum_{k=0}^{T-1} \delta(y, x_k) - E_x \sum_{k=T_N}^{T-1} \delta(y, x_k).$$

The first term is $g(x,y)$ by definition. For the second term, apply the strong Markov property at time $T_N$:
$$E_x \sum_{k=T_N}^{T-1} \delta(y, x_k) = E_x \left[ E_{x_{T_N}} \sum_{k=0}^{T-1} \delta(y, x_k) \right] = E_x \, g(x_{T_N}, y).$$

Since $x_{T_N}$ can only take values $N+k$ (with $k \geq 1$) when exiting on the right (exits on the left go below $0$, where $T=0$ and $g=0$), this becomes
$$E_x \, g(x_{T_N}, y) = \sum_{k=1}^{\infty} R_N(x,k) g(N+k, y).$$

Substituting back yields the stated formula.
