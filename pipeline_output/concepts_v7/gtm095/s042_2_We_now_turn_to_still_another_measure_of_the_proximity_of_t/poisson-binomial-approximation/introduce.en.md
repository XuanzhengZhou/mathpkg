---
role: introduce
locale: en
content_hash: ""
written_against: ""
---

This theorem bounds the total variation distance between the distribution $B$ of a sum of independent (but not identically distributed) Bernoulli variables and its Poisson approximation $\Pi$ with the same mean $\lambda = \sum p_k$. The bound $\|B - \Pi\| \leq 2 \sum p_k^2$ is proved via an elementary convolution decomposition $B - \Pi = R_1 + \cdots + R_n$ where $R_k = (B(p_k) - \Pi(p_k)) * F_k$, together with the inequality $\|R_k\| \leq \|B(p_k) - \Pi(p_k)\| = 2p_k(1 - e^{-p_k}) \leq 2p_k^2$. Sharper constants were obtained by Prokhorov ($C_1(\lambda) = 2\min(2,\lambda)$) for equal $p_k$ and by Le Cam ($C_2(\lambda) = 2\min(9,\lambda)$) for the general case. The theorem is fundamental for understanding the quality of the Poisson approximation in rare-event settings.
