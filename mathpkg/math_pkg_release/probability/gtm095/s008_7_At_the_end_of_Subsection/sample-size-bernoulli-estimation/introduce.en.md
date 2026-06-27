---
role: introduce
locale: en
content_hash: ""
written_against: ""
---

This result determines how many independent Bernoulli trials are needed to estimate the success probability $p$ within a prescribed margin $\varepsilon$ with confidence $1 - \alpha$. The formula $n \approx \log(2/\alpha) / (2\varepsilon^2)$ follows from the Hoeffding inequality and shows that the required sample size grows only logarithmically in $1/\alpha$, in contrast to the $1/\alpha$ growth from the ordinary Chebyshev inequality. This exponential improvement makes the bound practical for high-confidence estimation.
