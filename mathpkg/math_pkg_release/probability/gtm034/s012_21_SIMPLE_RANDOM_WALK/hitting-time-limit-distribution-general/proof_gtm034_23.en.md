---
role: proof
locale: en
of_concept: hitting-time-limit-distribution-general
source_book: gtm034
source_chapter: "V"
source_section: "23"
---

The proof proceeds via the method of moments. By a combinatorial identity,
$$\mathbf{T}_N^p = \sum_{j=0}^{\infty} \psi_{N,j} [(j+1)^p - j^p], \quad p \geq 1,$$
where $\psi_{N,j}$ is the indicator that the walk stays in $[-N,N]$ up to time $j$.

The moments are expressed in terms of the Green function via
$$\sum_{y=0}^{2N} g_{2N}^p(N,y) = \frac{1}{(p-1)!} \sum_{k=0}^{\infty} (k+1)(k+2) \cdots (k+p-1) \, \mathbf{E}_0[\psi_{N,k}],$$
where $g_{2N}^p = (I_{2N} - Q_{2N})^{-p}$. From this, the convergence of $\mathbf{E}_0[(\sigma^2 \mathbf{T}_N / N^2)^p]$ to the moments $m_p$ of $F$ is reduced to proving
$$\lim_{N \to \infty} \left( \frac{\sigma^2}{N^2} \right)^p \sum_{y=0}^{2N} g_{2N}^p(N,y) = \frac{m_p}{p!}.$$

This limit is established by iterating Theorem T1 $p$ times, showing that the scaled $p$-th power of $g_N$ converges to the $p$-th iterate $R^p(s,t)$ of the kernel $R(s,t) = \min(s,t) - st$. The convergence of the Riemann approximating sums to the iterated integrals is uniform because $R$ is continuous on $[0,1] \times [0,1]$.

The moment sequence $m_p$ satisfies the uniqueness condition for the moment problem (the series $\sum m_p r^p / p!$ converges for $r < \pi^2/8$). Therefore, convergence of moments implies convergence in distribution.
