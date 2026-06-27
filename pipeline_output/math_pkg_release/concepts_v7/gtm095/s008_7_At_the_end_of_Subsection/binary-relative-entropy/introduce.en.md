---
role: introduce
locale: en
content_hash: ""
written_against: ""
---

The binary relative entropy $H(a) = a \log(a/p) + (1-a) \log((1-a)/(1-p))$ is the Kullback-Leibler divergence between a Bernoulli$(a)$ distribution and a Bernoulli$(p)$ distribution. It appears naturally as the rate function in Cramér's theorem for Bernoulli sums, governing the exponential decay rate of tail probabilities $P(S_n/n \approx a)$. The function is nonnegative, convex in $a$, and attains its minimum of $0$ at $a = p$. It satisfies the Pinsker-type bound $H(a) \ge 2(a-p)^2$, which leads to the Hoeffding inequality.
