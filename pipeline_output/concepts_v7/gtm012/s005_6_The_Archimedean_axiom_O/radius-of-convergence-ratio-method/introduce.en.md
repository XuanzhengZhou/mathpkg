---
role: introduce
locale: en
content_hash: ""
written_against: ""
---

When the limit of successive coefficient ratios exists, the radius of convergence of a power series can be computed directly from the ratio test. If $\lim |a_{n+1}/a_n| = L > 0$, the series converges when $|z - z_0| < 1/L$ and diverges when $|z - z_0| > 1/L$, giving $R = 1/L$. If $L = 0$, the coefficients decay super-exponentially and the series converges for all $z \in \mathbb{C}$ ($R = \infty$). This theorem provides a practical method for computing radii of convergence, though the Cauchy-Hadamard formula using limsup of $|a_n|^{1/n}$ is more general.
