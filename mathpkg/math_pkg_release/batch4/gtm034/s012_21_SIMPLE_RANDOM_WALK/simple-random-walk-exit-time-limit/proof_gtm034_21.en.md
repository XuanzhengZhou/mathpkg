---
role: proof
locale: en
of_concept: simple-random-walk-exit-time-limit
source_book: gtm034
source_chapter: "V"
source_section: "21"
---

First, the expected exit time is computed using P4:
$$E_N[T_{2N}] = \sum_{x=0}^{2N} g_{2N}(N,x) = 2(2N+2) \sum_{x=0}^{2N} R\left(\frac{N+1}{2N+2}, \frac{x+1}{2N+2}\right) = (N+1)^2.$$

The distribution of $T_{2N}$ is expressed via
$$P_N[T_{2N} > n] = \sum_{y=0}^{2N} Q_{2N}^n(N,y).$$
Using the spectral decomposition (P1 and P2), one writes
$$P_N[T_{2N} > n] = \sum_{y=0}^{2N} \sum_{k=0}^{2N} \lambda_k^n v_k(N) v_k(y).$$

Substituting the explicit forms of $\lambda_k$ and $v_k$ from P1 and simplifying the sum over $y$ leads to an expression involving powers of cosines. Summing only over odd indices $k = 2j+1$ (since even terms cancel) gives
$$P_N[T_{2N} > n] = \frac{1}{N+1} \sum_{j=0}^{N} \left[ \cos\frac{2j+1}{2N+2}\pi \right]^n (-1)^j \sum_{y=0}^{2N} \sin\left[\frac{2j+1}{2N+2}\pi(y+1)\right].$$

Setting $n = N^2 x$ and using the approximations
$$\left( \cos \frac{2j + 1}{2N + 2} \pi \right)^{N^2 x} \sim \left( 1 - \frac{\pi^2}{8} \frac{(2j + 1)^2}{(N + 1)^2} \right)^{N^2 x} \sim e^{-\frac{\pi^2}{8}(2j+1)^2 x},$$
valid when $j$ is small compared to $N$, and evaluating the sum over $y$ using the cotangent approximation, one obtains the stated limit.
