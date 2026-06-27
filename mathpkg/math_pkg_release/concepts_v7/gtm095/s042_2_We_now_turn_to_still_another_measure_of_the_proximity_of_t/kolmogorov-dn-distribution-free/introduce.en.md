---
role: introduce
locale: en
content_hash: ""
written_against: ""
---

This lemma, due to Kolmogorov, is the key observation underlying the Kolmogorov--Smirnov goodness-of-fit tests. It states that the distribution of the maximal deviation $D_N = \sup_x |F_N(x) - F(x)|$ between the empirical and true distribution functions does not depend on the specific continuous distribution $F$ being tested. The proof uses the probability integral transform: the variables $\tilde{\eta}_k = F(\xi_k)$ are i.i.d. Uniform$[0,1]$, and the statistic can be rewritten as $\sup_{t \in [0,1]} |U_N(t) - t|$ where $U_N$ is the empirical distribution function of uniform observations. This distribution-free property is what makes the Kolmogorov--Smirnov test universally applicable for testing any completely specified continuous distribution.
